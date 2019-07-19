ac=int(input())
kc=list(map(int,input().split()))
sc=0
hc=len(kc)
for i in range(hc):
    sc+=kc[i]
qc=sc//hc
print(qc)
