import bisect
N, M = map(int, input().split())

A=list(map(int, input().split()))
B=list(map(int, input().split()))
A=sorted(A,reverse=True)
B=sorted(B)

cnt=0
for i in range(N):
  target_a=A[i]*2
  r_min = bisect.bisect_right(B,target_a)-1

  if r_min >= 0:
    cnt += 1
    B.pop(r_min)

print(cnt)
