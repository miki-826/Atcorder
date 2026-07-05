X,Y,L,R,A,B = map(int, input().split())
ans=0
if B<=L:
  ans+=(B-A)*Y

if A<L and B>L:
  ans+=(L-A)*Y
  
  
if A>=R:
  ans+=(B-A)*Y
if A<R and B>R:
  ans+=(B-R)*Y


if A<= L and B>=R:
  ans+=(R-L)*X

if A<=L and L<B<R:
  ans+=(B-L)*X
  
if L<A<R and B>=R:
  ans+=(R-A)*X
  
if L<A and B<R:
  ans+=(B-A)*X

print(ans)
