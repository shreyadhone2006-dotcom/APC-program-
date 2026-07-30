n=int(input("enter a number:"))
root=int(n**0.5)
count=0
for i in range(1,root+1):
    if root%i==0:
        count=count+1
print("Square root=",root)
if count==2:
    print("Sqaure root is prime")
else:
    print("square root is not prime")