n = eval(input("請輸入正三角形邊長:"))

for x in range(-n,0):
  for y in range(-n,n):
    if abs(x)+abs(y) == n -1:
        print("*",end=' ')
    else:
        print(" ",end=' ')
  print()
for i in range(n):
    print('  ',end = '')
    print("*",end= ' ')
