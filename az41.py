bc1,bc2=map(int,input().split())
char=input().split()
fc=[]
for yc in char:
	if(int(yc)%2!=0):
		fc.append(yc)
print(fc[bc2-1])
