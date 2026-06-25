N = int(input())
C = [[] for _ in range(N+1)]
for i in range(N):
  A = list(map(int, input().split()))
  for d in range(A[0]):
    C[A[d+1]].append(i+1)

for g in range(1,N+1):
  if len(C[g])==0:
    print("0")
  else:
    print(len(C[g]),end="")

  for i in range(len(C[g])):
    if i == len(C[g])-1:
      print(" ",C[g][i])
    else:
      print(" ",C[g][i],end="")
  