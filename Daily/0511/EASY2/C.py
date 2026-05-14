A=int(input())
B=[0]*100
for i in range(A):
  A = list(map(int, input().split()))
  if A[0]==2:
    print(B[-1])
    B.pop()
  elif A[0]==1:
    B.append(A[1])

    
