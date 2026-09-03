with open("natural.py", "r") as file:
    lines = file.readlines()

with open("without_comments.py", "w") as file:
    for line in lines:
        if "#" not in line:
            file.write(line)
        else:
            file.write(line.split("#")[0] + "\n")

print("Comments removed successfully.")