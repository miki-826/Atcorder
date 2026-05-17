N, Q = map(int, input().split())
A=list(map(int, input().split()))
B=[0]*(N+1)
B[0]=0

for i in range(N):
  B[i+1]=A[i]+B[i]

for d in range(Q):
  N, M = map(int, input().split())
  print(B[M]-B[N-1])