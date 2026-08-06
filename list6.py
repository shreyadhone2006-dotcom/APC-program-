a=[22,16,18,27,23]
large=a[0]
small=a[0]
for i in a:
    if large<i:
        large=i
    if small>i:
        small=i
print(large)
print(small)
    