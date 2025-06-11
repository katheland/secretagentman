import os

def get_files_info(working_directory, directory=None):
    if directory == None:
        directory = ""
    if directory.startswith("/") or directory.startswith("../") or directory.startswith("~/"):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'
    path = os.path.join(working_directory, directory)
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory.'
    
    try:
        dirlist = os.listdir(path=path)
        output = ""
        for entry in dirlist:
            fullpath = os.path.join(path, entry)
            output += f'- {entry}: file_size={os.path.getsize(fullpath)} bytes, is_dir={os.path.isdir(fullpath)}\n'
            return output
    except Exception as e:
        return f'Error: {e}'