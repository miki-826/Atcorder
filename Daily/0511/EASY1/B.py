A = list(map(int, input().split()))

if A[1]>A[2] and A[0]-(A[1]+A[2])>A[1]-A[2]:
  print("No")
elif A[2]>A[1] and A[0]-(A[1]+A[2])>A[2]-A[1]:
  print("No")
elif A[1]==A[2]:
  print("No")
else:
  print("Yes")