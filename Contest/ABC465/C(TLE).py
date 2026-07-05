N = int(input())
S=input()
A=[]
for g in range(N):
  A.append(g+1)
  if S[g]=="o":
    A.reverse()
    
for d in range(N):
  print(A[d],end=" ")
  