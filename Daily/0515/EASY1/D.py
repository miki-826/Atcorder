N,M,K = map(int, input().split())
ans=[0]*N
for i in range(K):
  A, B = map(int, input().split())
  ans[A-1]+=1
  if ans[A-1] >= M:
    print(A,end=" ")