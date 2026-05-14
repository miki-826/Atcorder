N, M = map(int, input().split())
D = [0]*N
for i in range(M):
  S = input().split()
  number = int(S[0])-1
  if S[1]=="M" and D[number]==0:
    print("Yes")
    D[number]=1
  else:
    print("No")
    