uc=int(input())
if uc!=0:
	print(1,end=' ')
	oc=1
	kc=0
	for i in range(1,uc):
		zc=kc+oc
		print(zc,end=' ')
		kc=oc
		oc=zc
else:
	print(0)
