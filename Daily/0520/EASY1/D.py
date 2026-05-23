H,W = map(int, input().split())
A = [list(input()) for _ in range(H)]
cnt=0
ans=0

for h in range(H):
  for w in range(W):
    if A[h][w]=="#":
      if h-1>=0 and h-1<H:
        if A[h-1][w]=="#":
          cnt+=1
          
      if h+1>=0 and h+1<H:
        if A[h+1][w]=="#":
          cnt+=1
          
      if w-1>=0 and w-1<W:
        if A[h][w-1]=="#":
          cnt+=1
          
      if w+1>=0 and w+1<W:
        if A[h][w+1]=="#":
          cnt+=1
          
      if cnt==2 or cnt==4:
        ans+=1
        cnt=0
        
    elif A[h][w]==".":
      ans+=1

if ans>=H*W:
  print("Yes")
else:
  print("No")
      