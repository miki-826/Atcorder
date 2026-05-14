a=int(input())
S = list(map(int, input().split()))
B=list()
for i in range(a-1):
  B.append(S[i])
  C=abs(S[i]-S[i+1])
  if C != 1:
    if S[i]>S[i+1]:
      for d in range(1,C):
        B.append(S[i]-d)
    elif S[i]<S[i+1]:
      for c in range(1,C):
        B.append(S[i]+c)
B.append(S[a-1])
print(*B)