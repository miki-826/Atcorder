D = int(input())
N = int(input())
A=[0]*(D+2)
A[0]=0
for i in range(N):
  L, R = map(int, input().split())
  A[L]+=1
  A[R+1]-=1

for d in range(1,D+1):
  print(A[d]+A[d-1])
  A[d]+=A[d-1]

