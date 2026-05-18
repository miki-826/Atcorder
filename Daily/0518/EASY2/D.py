X,Y = map(int, input().split())
cnt=0
ans=0
for i in range(1,7):
  for d in range(1,7):
    if i+d >=X:
      cnt+=1
    if abs(i-d)>=Y:
      ans+=1
      if abs(i-d)>=Y and i+d >=X:
        ans-=1
print((cnt+ans)/36)