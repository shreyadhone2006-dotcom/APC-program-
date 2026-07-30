a=0
b=1
n=int(input("Enter number"))
print(a)
print(b)
c=a+b
while c<=n:
    print(c)
    a=b
    b=c
    c=a+b
    