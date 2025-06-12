# main.py for the AI agent

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from schemas import *
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

if len(sys.argv) == 1:
    raise Exception("You need to provide a prompt.")
request = sys.argv[1]
verbose = False
if len(sys.argv) > 2:
    verbose = sys.argv[2] == "--verbose"

messages = [types.Content(
    role="user", 
    parts=[types.Part(text=request)]
)]

MAX_ITERATIONS = 20

if verbose:
    print("User prompt: " + request)

for i in range(MAX_ITERATIONS):
    function_called = False
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        )
    )

    if response.candidates is not None:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if response.function_calls is not None:
        function_called = True
        for call in response.function_calls:
            result = call_function(call, verbose)
            if hasattr(result.parts[0], "function_response") and hasattr(result.parts[0].function_response, "response"):
                messages.append(result)
                if verbose:
                    print(f"-> {result.parts[0].function_response.response}")
                else:
                    print(f"{result.parts[0].function_response.response["result"]}")
            else:
                raise Exception("The response doesn't have a response.  It should have a response.")
    if verbose:
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

    if not function_called:
        print(response.text)
        break