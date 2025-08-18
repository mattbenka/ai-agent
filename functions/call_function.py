from enum import Enum
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

WORKING_DIRECTORY = "./calculator"

FUNCTION = Enum("Function", ["get_file_content", "get_files_info", "run_python_file", "write_file"])

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    print(f"Trying to find function {function_call_part.name}")
    match function_call_part.name:
        case FUNCTION.get_file_content.name:
            function_result = get_file_content(WORKING_DIRECTORY, **function_call_part.args)                 
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": function_result},
                    )
                ],
            )
        case FUNCTION.get_files_info.name:
            function_result = get_files_info(WORKING_DIRECTORY, **function_call_part.args)                 
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": function_result},
                    )
                ],
            )
        case FUNCTION.run_python_file.name:
            function_result = run_python_file(WORKING_DIRECTORY, **function_call_part.args)                 
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": function_result},
                    )
                ],
            )
        case FUNCTION.write_file.name:
            function_result = write_file(WORKING_DIRECTORY, **function_call_part.args)                 
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": function_result},
                    )
                ],
            )
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Unknown function: {function_call_part.name}"},
                    )
                ],
            )
            