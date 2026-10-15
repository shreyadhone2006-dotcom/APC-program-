import re

s = "My age is 20 and my marks are 91"
print(re.findall(r'\d', s))