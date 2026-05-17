H,W = map(int, input().split())
A =[[0] * (W + 1)] + [[0] + list(map(int, input().split())) for _ in range(H)]
C = [[0 for j in range(W+1)] for i in range(H+1)]
D = [[0 for j in range(W+1)] for i in range(H+1)]
for i in range(1,H+1):
  for d in range(1,W+1):
    C[i][d]=A[i][d]+C[i][d-1]


for g in range(1,W+1):
  for f in range(1,H+1):
    D[f][g]=C[f][g]+D[f-1][g]

N=int(input())
for l in range(N):
  E,F,G,I = map(int, input().split())
  print(D[G][I]+D[E-1][F-1]-D[E-1][I]-D[G][F-1])
  