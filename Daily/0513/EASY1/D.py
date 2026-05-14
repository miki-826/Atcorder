L, R = map(int, input().split())
S = input()
d=int(R)
for i in range(L-1):
  print(S[i],end="")

while d >= L:
  print(S[d-1],end="")
  d-=1
  
for c in range(R+1,len(S)+1):
  print(S[c-1],end="")