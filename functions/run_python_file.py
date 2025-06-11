# run_python_file

import os
import subprocess

def run_python_file(working_directory, file_path):
    if file_path == None:
        file_path = ""
    if file_path.startswith("/") or file_path.startswith("../") or file_path.startswith("~/"):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'
    path = os.path.join(working_directory, file_path)
    if not os.path.isfile(path):
        return f'Error: File "{file_path}" not found'
    if not path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        output = subprocess.run(["python3", path], capture_output=True, timeout=30)
        stdout = f'STDOUT: {output.stdout}'
        if output.stdout == "" or output.stdout == None:
            stdout = "No output produced"
        stderr = f'STDERR: {output.stderr}'
        code = ""
        if output.returncode != 0:
            code = f'\nProcess exited with code {output.returncode}'
        return stdout + "\n" + stderr + code
    except Exception as e:
        return f'Error: {e}'