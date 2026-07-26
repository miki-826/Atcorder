M,D = map(int, input().split())
A=input()
G=[0]*M
g=0
for i in range(M):
 if A[i]=="G":
  G[i]=1
  for f in range(D):
    if i-(f+1)>=0:
      G[i-(f+1)]=1
    if i+(f+1)<M:
      G[i+(f+1)]=1
  f=0

for j in range(M):
  if G[j]==0:
    g+=1
print(g)