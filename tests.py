from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info

result = get_file_content("calculator", "main.py")
print(result)

result = get_file_content("calculator", "pkg/calculator.py")
print(result)

result = get_file_content("calculator", "/bin/cat")
print(result)

result = get_file_content("calculator", "pkg/does_not_exist.py")
print(result)




'''
result = get_file_content("calculator", "lorem.txt")
print(result)

print("Current dir test")
result = get_files_info("calculator", ".")
expected_result = "Result for current directory:    - main.py: file_size=576 bytes, is_dir=False    - tests.py: file_size=1343 bytes, is_dir=False - pkg: file_size=92 bytes, is_dir=True"
print(result)

print("pkg dir test")             
result = get_files_info("calculator", "pkg")
expected_result = "Result for 'pkg' directory:    - calculator.py: file_size=1739 bytes, is_dir=False    - render.py: file_size=768 bytes, is_dir=False"
print(result)

print("bin dir test")        
result = get_files_info("calculator", "/bin")
expected_result = "Result for '/bin' directory: Error: Cannot list \"/bin\" as it is outside the permitted working directory"
print(result)

print("Parent dir test")      
result = get_files_info("calculator", "../")
expected_result = "Result for '../' directory: Error: Cannot list \"../\" as it is outside the permitted working directory"
print(result)

print("Not a dir test")      
result = get_files_info("calculator", "3413fsaw")
expected_result = "Result for '../' directory: Error: Cannot list \"../\" as it is outside the permitted working directory"
print(result)
'''