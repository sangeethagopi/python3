nc,mc=list(map(int,input().split()))
low=nc
if mc<nc:
	low=m
else:
	pass
for i in range(1,low+1):
	if nc%i==0 and mc%i==0:
		k=i
print(k)
