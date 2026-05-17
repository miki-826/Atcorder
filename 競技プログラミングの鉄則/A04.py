a = int(input())
b=len(str(format(a, 'b')))
for i in range (10-b):
  print("0",end="")
print(format(a, 'b'))
