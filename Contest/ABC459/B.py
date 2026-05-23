A=int(input())
S =list(input().split())
cnt=""

for i in range(len(S)):
  if S[i].startswith(("a", "b", "c")):
    cnt+="2"
  elif S[i].startswith(("d", "e", "f")):
    cnt+="3"
  elif S[i].startswith(("g", "h", "i")):
    cnt+="4"
  elif S[i].startswith(("j", "k", "l")):
    cnt+="5"
  elif S[i].startswith(("m", "n", "o")):
    cnt+="6"
  elif S[i].startswith(("q", "r", "s","p")):
    cnt+="7"
  elif S[i].startswith(("t", "u", "v")):
    cnt+="8"
  elif S[i].startswith(("x", "y", "z","w")):
    cnt+="9"
print(cnt)