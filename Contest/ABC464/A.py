S = input()
E=0
W=0
for i in range(len(S)):
  if S[i]=="E":
    E+=1
  elif S[i]=="W":
    W+=1
    
if E>W:
  print("East")
else:
  print("West")