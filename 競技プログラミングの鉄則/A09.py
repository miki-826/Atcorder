H,W,N = map(int, input().split())
list = [[0] * (W+2) for i in range(H+2)]
for i in range(N):
  A,B,C,D = map(int, input().split())
  list[A][B]+=1
  list[C+1][D+1]+=1
  list[A][D+1]-=1
  list[C+1][B]-=1

for j in range(1,H+1):
  for d in range(1,W+1):
    list[j][d]=list[j][d]+list[j][d-1]
    

for m in range(1,W+1):
  for k in range(1,H+1):
    list[k][m]=list[k][m]+list[k-1][m]

for w in range(1,H+1):
    for h in range(1,W+1): 
      print(list[w][h],end=" ")
    print("")