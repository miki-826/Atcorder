N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
  if A[i]<M:
    M=A[i]
    print(1)
  else:
    print(0)