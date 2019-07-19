numer12=int(input())
l,rc=map(int,input().split())
l+=1
yeah=0
if numer12 in range(l,rc):
	yeah=1
print("yes" if yeah==1 else "no")
