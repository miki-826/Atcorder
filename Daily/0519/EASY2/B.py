S=list(input())
for i in range(len(S)):
  if S[i]==".":
    S[i]=""
for g in range(len(S)):
  print(S[g],end="")