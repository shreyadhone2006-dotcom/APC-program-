with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total number of words:", len(words))