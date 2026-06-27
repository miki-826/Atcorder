H,W = map(int, input().split())
S=[]
for i in range(H):
  S.append(input())

D=[[1] * W for i in range(H)]

B =[0]*H
C=[0]*W
white=0
for i in range(H):
  for d in range(W):
    if S[i][d] == "#":
      B[i]+=1
      C[d]+=1


t=0
while t<W and C[t]==0 :
  for z in range(H):
    D[z][t]=0
  t+=1
j=0
while j<H and B[j]==0 :
  for x in range(W) :
    D[j][x]=0
  j+=1

c=H-1
while c>=0 and B[c]==0 :
  for v in range(W) :
    D[c][v]=0
  c-=1

k=W-1
while  k>=0 and C[k]==0:
  for l in range(H) :
    D[l][k]=0
  k-=1


for row in range(H):
  for jn in range(W):
    if D[row][jn]==1:
      print(S[row][jn] , end="")
  print("")
