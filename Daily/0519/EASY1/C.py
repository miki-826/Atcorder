N=int(input())
A=[""]*N
cnt=0
for i in range(N):
  D, M =input().split()
  cnt+=int(M)
  A[i]=D
A=sorted(A)

print(A[cnt%int(N)])