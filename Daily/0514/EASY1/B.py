A=int(input())
S=input()
f=0
for i in range(A-2):
  if S[i]=="#" and S[i+2]=="#" and S[i+1]==".":
    f+=1
print(f)