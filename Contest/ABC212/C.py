import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = abs(A[0]-B[0])

A.sort()
B.sort()

for i in range(N):
  r_min=bisect.bisect(B,A[i])
  
  if  r_min > 0 :
    a =  min(abs(A[i]-B[r_min-1]),a)
  
  if r_min < M:
    a = min(abs(A[i]-B[r_min]),a)
print(a)