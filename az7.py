new1,mew1=map(int,input().split())
pro=new1*mew1
yeah=0
for i in range(0,pro+1):
	if i**2==pro:
		yeah=1
		break
print("yes" if yeah==1 else "no")
