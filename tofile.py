from array import array

a = array('i', [10, 20, 30, 40])

with open("data.bin", "wb") as f:
    a.tofile(f)

print("Array stored in file successfully")