N, M = input().split()
cnt=0
for i in range(int(N)):
  S = input()
  if M=="A":
    if S[0]=="o":
      cnt+=1
  elif M=="B":
    if S[1]=="o":
      cnt+=1
  elif M=="C":
    if S[2]=="o":
      cnt+=1
  elif M=="D":
    if S[3]=="o":
      cnt+=1
  elif M=="E":
    if S[4]=="o":
      cnt+=1

if cnt>=1:
  print("Yes")
else:
  print("No")