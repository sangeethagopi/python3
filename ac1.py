ac1,bc1=list(map(int,input().split()))
cc1=list(map(int,input().split()))
dc1=[]
for i in cc1:
    if i<=i+1:
        dc1.append(i)
print(dc1[bc1-1])
