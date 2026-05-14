A,B,C,X = map(int, input().split())
if X<=B and X>A:
  print(C/(B-(A)))
elif X<=A:
  print(1.000000000000)
elif X>B:
  print(0.000000000000)