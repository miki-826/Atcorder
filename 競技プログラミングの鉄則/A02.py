a ,b = map(int,input().split())
A = list(map(int, input().split()))
cnt = 0
for i in range (a):
  if A[i] == b:
    cnt += 1
  else:
    pass
if cnt>0:
  print("Yes")
else:
    print("No")