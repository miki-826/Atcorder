N = int(input())
A = list(map(int, input().split()))

B=list(sorted(A,reverse=True))

print(A.index(B[1])+1)