T,X = map(int, input().split())
A = list(map(int, input().split()))
cnt=A[0]
print(0,cnt)
for i in range(1,T+1):
  if abs(A[i]-cnt)>=X:
    cnt=A[i]
    print(i,cnt)