A=int(input())
B = list(map(int, input().split()))
C=sorted(B)

print(B.index(C[A-2])+1)