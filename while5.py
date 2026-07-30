sum=0
n=int(input("enter number:"))
i=0
while i<=n:
    if i%2!=0:
        sum=sum+i
    i+=1
print(sum)