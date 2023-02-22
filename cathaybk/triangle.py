n = int(input("請輸入正三角形邊長:"))

for i in range(n):
  print(" "*(n-i-1), end="")
  if i==0:
    print("*"*(2*i+1))
  elif 0<i and i<n-1:
    print("*"+" "*(2*i-1)+"*")
  else:
    for j in range(2*n-1):
      if j%2==0:
        print("*", end="")
      else:
        print(" ", end="")
    print()
