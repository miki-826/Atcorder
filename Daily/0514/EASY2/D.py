S=["a"]*3
S[0]=input()
S[1]=input()
S[2]=input()

A = input()

for i in range(len(A)):
  print(S[int(A[i])-1],end="")