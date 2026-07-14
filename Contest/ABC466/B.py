N, M = map(int, input().split())
list=[-1]*M
max=0

for i in range(N):
  C,S = map(int, input().split())
  if list[C-1]<S:
    list[C-1]=S
    
    
for d in range(M):
  print(list[d],end=" ")

