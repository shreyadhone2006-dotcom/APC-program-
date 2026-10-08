with open("student.txt") as file:
    content=file.read()
line=content.split("\n")
print(len(line))
words=content.split()
print(len(words))
count=0
for s in content:
    if s.isalpha():
        count+=1
print(count)