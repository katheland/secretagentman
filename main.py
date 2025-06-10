# main.py for the AI agent

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

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

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages
)

if verbose:
    print("User prompt: " + request)
print(response.text)
if verbose:
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))