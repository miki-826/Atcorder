A = list(map(int, input().split()))

if A[1]*A[0]==A[2]:
  print("Yes")
elif A[2]*A[1]==A[0]:
  print("Yes")
elif A[0]*A[2]==A[1]:
  print("Yes")
else:
  print("No")