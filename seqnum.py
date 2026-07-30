n=int(input("Enter value of n:"))
sum=1.0
fact=1
for i in range(1,n+1):
    fact*=i
    sum+=1/fact
print("Sum of the series=",sum)
