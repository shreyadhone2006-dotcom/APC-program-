letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input("Enter the value of n: "))

for i in range(n,-1,-1):
    for j in range(i):
        print(letters[j], end=" ")
    print()