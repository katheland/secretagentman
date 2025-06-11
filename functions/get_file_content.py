# get_file_content

import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    if file_path == None:
        file_path = ""
    if file_path.startswith("/") or file_path.startswith("../") or file_path.startswith("~/"):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'
    path = os.path.join(working_directory, file_path)
    if not os.path.isfile(path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) == MAX_CHARS:
            file_content_string = file_content_string + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f'Error: {e}'