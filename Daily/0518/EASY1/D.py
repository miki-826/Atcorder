N, A = map(int, input().split())
B = list(map(int, input().split()))
C=A+B[0]
print(C)
for i in range(1,N):

  if B[i]>C:
    print(B[i]+A)
    C=B[i]+A
  elif B[i]<=C:
    print(C+A)
    C=C+A
  