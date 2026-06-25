import re
S = input()
r = re.sub(r'\D', '', S)
print(r)