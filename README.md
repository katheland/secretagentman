# secretagentman
This is an agent based on the Gemini LLM that is able to do basic reading, writing, and analysis of files in its working directory.  (Its current working directory is a basic calculator that renders itself in a rectangle in the command prompt.)

# Setup
You'll want to create a virtual environment at the top of the project directory using `python3 -m venv venv`.  Activate it with `source venv/bin/activate`, and install the requirements with `pip install -r requirements.txt`.

You'll need your own Gemini API Key.  Put it in a .env file.  `GEMINI_API_KEY="your_api_key_here"`

# How To Use
`python3 main.py "your prompt here"`

Optional: `python3 main.py "your prompt here" --verbose` also prints the user prompts, the number of tokens used in the prompt and response, and full details of the response.

Make sure your virtual environment is active!