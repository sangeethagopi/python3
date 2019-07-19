ac=int(input())
bc=list(map(int,input().split()))
for i in bc:
	if bc.count(i)==1:
		print(i)
		break
