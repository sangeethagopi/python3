ac=list(input())
bc=list(ac)
count=0
b.reverse()
for i in range(len(ac)):
    if(ac[i]==bc[i]):
        count=count+1
if(count==(len(ac))):
    print("yes")
else:
    print("no")
