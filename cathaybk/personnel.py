n=int(input("請輸入總人數："))

a=list(range(1,n+1))
count=0

while len(a)>1:
	b=a[:]
	for i in range(len(b)):
		count+=1
		if count%3==0:
			a.remove(b[i])
print(a[0])
