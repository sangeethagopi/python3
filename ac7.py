ma=int(input())
prashu=list(map(int,input().split()))
flag1=0
rrr=[]
for i in range(0,ma):
	if(prashu[i]==i):
		temp=prashu[i]
		flag1=1
		rrr.append(temp)
		rrr=sorted(rrr)
print(*rrr)
if(flag1==0):
	print(-1)
