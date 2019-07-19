gc1=int(input())
flagc2=0
if(gc1>2):
    for i in range(2,int(gc1/2)+1):
        if gc1%i==0:
            print("yes")
            flagc2=1
            break
if flagc2==0 or gc1==2:
    print("no")
