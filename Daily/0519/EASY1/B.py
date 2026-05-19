N=int(input())
A = list(map(int, input().split()))
ans=0
for i in range(1,N+1,2):
  ans+=A[i-1]
print(ans)