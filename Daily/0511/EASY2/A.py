A=int(input())
S= list(map(int, input().split()))
for i in range(A-1):
  print(S[i]*S[i+1],end=" ")