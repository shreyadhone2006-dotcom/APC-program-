n=int(input("Enter number of elements:"))
i=1
largest=int(input("Enter number:"))
while i<n:
    num=int(input("Enter number:"))
    if num>largest:
        largest=num
    i+=1
print(largest)
