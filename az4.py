new1=int(input())
yeah1=1
for i in range(2,new):
	if new1%i==0:
		yeah1=0
		break
print("yes" if yeah1==0 else "no")
