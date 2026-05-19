N, M = map(int, input().split())
C=input().split()
D=input().split()
P= list(map(int, input().split()))
ans=0
t=0
for i in range(len(C)):
  for d in range(len(D)):
    if C[i]==D[d]:
      ans+=P[d+1]
      break
    else:
      t+=1
    if t == len(D):
      ans+=P[0]
  t=0
print(ans)
