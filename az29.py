#B
sc=int(input())
ddc=list(map(int,input().split()))
for i in range(sc-1):
    if(ddc[i]>ddc[i+1]):
        print(i)
