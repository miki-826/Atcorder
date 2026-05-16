A = list(map(int, input().split()))
C=input()

if C == "Blue":
  A.pop(2)
  print(min(A))
elif C == "Green":
  A.pop(1)
  print(min(A))
elif C == "Red":
  A.pop(0)
  print(min(A))
