with open("student.txt", "r") as file:
    content = file.read()

uppercase_content = content.upper()

with open("uppercase.txt", "w") as file:
    file.write(uppercase_content)

print("Uppercase file created successfully.")