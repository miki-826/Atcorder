A = list(input())
B = list(input())
C = list(input())
all = len(A)+len(B)+len(C)
for i in range(all):
    if i ==0:
        a=A[0]
        A.pop(0)

    if a == "a":
        if not A  :
            print("A")
            break

        else:
            a=A[0]
            A.pop(0)

    elif a == "b":
        if not B :
            print("B")
            break
        else:
            a=B[0]
            B.pop(0)

    elif a == "c":
        if not C :
            print("C")
            break
        
        else:
            a=C[0]
            C.pop(0)
    
print(A,B,C)