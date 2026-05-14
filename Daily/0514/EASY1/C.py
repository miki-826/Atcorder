N = int(input())
S=["a"]*N
D=[0]*N
a=0
for i in range(N):
  S[i]=input()
  D[i]=len(S[i])
a=max(D)
  
for j in range(N):
  for d in range ((a-len(S[j]))//2):
    print(".",end="")
  print(S[j],end="")
  for g in range ((a-len(S[j]))//2):
    print(".",end="")
  print("")
  