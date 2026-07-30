n=int(input("Enter number of elements:"))
i=1
smallest=int(input("Enter number:"))
while i<n:
    num=int(input("Enter number:"))
    if num<smallest:
        smallest=num
    i+=1
print(smallest)
