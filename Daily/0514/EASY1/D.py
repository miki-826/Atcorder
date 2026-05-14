N, M = map(int, input().split())
A=[0]*N
for i in range(M):
  e,f = map(int, input().split())
  if e == 1:
    A[f-1]+=1
  elif e == 2:
    A[f-1]+=2
  elif e == 3:
    if A[f-1]>=2:
      print("Yes")
    else:
      print("No")