N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
  D = list(map(int, input().split()))
  if D[0]==1:
    A[D[1]-1] = D[2]
  elif D[0]==2:
    print(A[D[1]-1])
