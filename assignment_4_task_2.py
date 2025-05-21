file_name="output.txt"
enter=input("Enter text to write to the file")
with open(file_name,'w') as file:
    text=file.write(enter+"\n")
    print(f"Data successfully written to'{file_name}' ")
enter2=input("Enter additional text to append")
with open(file_name,'a') as file:
    text2=file.write(enter2+"\n")
    print("Data successfully appended")
with open(file_name,'r') as file:
    f=file.read()
print(f"Final content of {file_name}:\n{f}\n")