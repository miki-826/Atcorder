H,W= map(int, input().split())
a = [ list(map(int,input().split(" "))) for _ in range(H)]

for i in range(H):
  for d in range(W):
    if a[i][d]==0:
      print(".",end="")
    if a[i][d]>0:
      print(chr(a[i][d]+64),end="")
    
  print("")

