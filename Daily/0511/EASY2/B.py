N ,X ,Y ,Z = map(int, input().split())
cnt=0
if X>Y:
  for i in range(Y,X):
    if i==Z:
      cnt+=1
elif Y>X:
  for i in range(X,Y):
    if i==Z:
      cnt+=1
elif X==Y:
  if X==X:
    cnt+=1

if cnt>0:
  print("Yes")
else:
  print("No")
