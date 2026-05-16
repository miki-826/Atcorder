H,W = map(int, input().split())
cnt=0
for h in range(H):
  for w in range(W):
    if h-1>=0 and h-1<H:
      cnt+=1
    if h+1>=0 and h+1<H:
      cnt+=1
    if w-1>=0 and w-1<W:
      cnt+=1
    if w+1>=0 and w+1<W:
      cnt+=1
    print(cnt,end=" ")
    cnt=0
  print("")
    
