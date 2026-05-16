S=list(input())
A=int(input())
for i in range(A):
  S.pop(0)
  S.pop(-1)

for n in range(len(S)):
  print(S[n],end="")