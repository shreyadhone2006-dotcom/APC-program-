from array import array

a = array('i', [1, 2, 3, 4])

print("Before:", a)

a.byteswap()

print("After:", a)