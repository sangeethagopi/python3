n1,n2=input().split()
n1=int(n1)
n2=int(n2)
for i in range(n1+1,n2):
    for j in range(2,i):
         if(i%j==0):
           break
    else:
        print(i,end=" ")
