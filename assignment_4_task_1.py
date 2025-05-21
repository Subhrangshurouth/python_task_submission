
import os
filename = "sample.txt"

if os.path.exists(filename):
    with open(filename, 'r') as file:
        filename=file.read()
        print(filename)
else:
    print(f"Error: The file '{filename}' does not exist.")