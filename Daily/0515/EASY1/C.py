H,W = map(int, input().split())
S,F = map(int, input().split())
S=S-1
F=F-1
D = [list(input()) for _ in range(H)]
A = list(input())

for i in range(len(A)):
  if A[i]=="L" and F-1>=0 :
    if D[S][F-1] == ".":
      F=F-1
    
  elif A[i]=="R" and F+1<=W-1:
    if D[S][F+1] == ".":
      F=F+1
      
  elif A[i]=="U" and S-1>=0:
    if D[S-1][F] == ".":
      S=S-1
      
  elif A[i]=="D" and S+1<=H-1:
    if D[S+1][F] == ".":
      S=S+1
      
print(S+1,F+1)