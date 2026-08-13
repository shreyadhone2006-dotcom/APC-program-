import array as arr
a=arr.array('i',[1,2,3])
for i in range(0,len(a)):
    print(a[i],end=" ")
a.insert(1,4)
print("\nafter inserting element:")
for i in a:
    print(i, end=" ")