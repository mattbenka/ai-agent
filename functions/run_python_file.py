import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not target_file.endswith(".py"):
        f'Error: "{file_path}" is not a Python file.'
    
    try:
        command = []
        command.append("python")
        command.append(target_file)
        for arg in args:
            command.append(arg)
        completed_process = subprocess.run(command, cwd=abs_working_dir, timeout=30, capture_output=True, text=True)
        if completed_process.returncode != 0:
            return f"Process exited with code {completed_process.returncode}"
        if completed_process.stdout is None:
            return "No output produced."
        return f"STDOUT: {completed_process.stdout} STDERR: {completed_process.stderr}"
    except Exception as e:
        f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=f"Runs a python file, with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the python file to execute."),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
    ),
)