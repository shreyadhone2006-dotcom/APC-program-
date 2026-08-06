l=[22,16,45,14,32,33,99,89,77,67,18,90,44,35,12]
print(l)
ec=0
oc=0
for i in l:
    if i%2==0:
        ec+=1
    else:
        oc+=1
print("Even elements:",ec)
print("Odd elements:",oc)
