S = list("HelloWorld")
A=int(input())

S[A-1]=""
for i in range(len(S)):
  print(S[i],end="")