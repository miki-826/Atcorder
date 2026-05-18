N, M = map(int, input().split())
A = list(map(int, input().split()))
B=[0]*M
for i in range(len(A)):
  B[A[i]-1]+=1

for d in range(M):
  if B[d]>1:
    print("No")
    d-=100
    break
  
if d==M-1:
  print("Yes")
  
for j in range(M):
  if B[j]<1:
    print("No")
    j-=100
    break
  
if j==M-1:
  print("Yes")
  

