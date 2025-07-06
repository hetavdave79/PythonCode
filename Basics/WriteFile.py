''' overwrite a file
from pathlib import Path

# Define the file path
file_path = Path.home() / "MyFiles" / "MyOutputFile.txt"

# Write content to the file
with open(file_path, "w") as file:
    file.write("Hello, world!\n")
    file.write("This file was created using Python.\n")
'''
from pathlib import Path

# Define the file path
file_path = Path.home() / "MyFiles" / "MyOutputFile.txt"

# Append to the file
with open(file_path, "a") as file:
    file.write("\nThis is a new line added to the existing file.")