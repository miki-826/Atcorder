N, K = map(int, input().split())
cnt=0
for i in range(1,N+1):
  for b in range(1,N+1):
      if 0<K-(b+i)<=N:
        cnt+=1
print(cnt)