pre=int(input())
pc=0
rc=1
gc=1
for i in range(pre):
	print(gc,end=' ')
	gc=pc+rc
	pc=rc
	cr=gc
