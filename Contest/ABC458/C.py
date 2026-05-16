S = list(input())
cnt=0
i=1
for g in range(len(S)):
  if S[g]=="C":
    if g<len(S)//2:
      cnt+=g+1
    elif g>=len(S)//2:
      cnt+=len(S)-(g+1)+1
    S[g]=[0]
print(cnt)
