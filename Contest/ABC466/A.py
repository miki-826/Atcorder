N = int(input())

A = list(map(int, input().split()))
cnt=0
for i in range(N):
  if A[i]<0:
    cnt+=1


if cnt>=N:
  print("Yes")
else:
  print("No")