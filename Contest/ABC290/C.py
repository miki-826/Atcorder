N, K = map(int, input().split())
A = list(map(int, input().split()))
A=list(set(A))
A.sort() 
a=0

if len(A)<K:
  for i in range(len(A)):
    if A[i]==a:
      a+=1
      
else:
  for i in range(K):
    if A[i]==a:
      a+=1
print(a)
