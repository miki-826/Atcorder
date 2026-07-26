N = int(input())
A = list(map(int, input().split()))
g=0
for i in range(N-2):
  if A[i+1]>A[i] and A[i+1]>A[i+2] and A[i]>=1 and A[i]<=N-2:
    g+=1
print(g)