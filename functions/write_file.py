# write_file

import os

def write_file(working_directory, file_path, content):
    if file_path == None:
        file_path = ""
    if file_path.startswith("/") or file_path.startswith("../") or file_path.startswith("~/"):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory.'
    
    try:
        path = os.path.join(working_directory, file_path)
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        with open(path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'