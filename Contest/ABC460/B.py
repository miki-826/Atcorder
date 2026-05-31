T = int(input())

for i in range(T):
  x,y,r,X,Y,R = map(int, input().split())
  
  d = (X-x)**2+(Y-y)**2
  if d <= (r+R)**2 and d >= (abs(r-R))**2:
    print("Yes")
  else:
    print("No")