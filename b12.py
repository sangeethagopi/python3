nc=input()
n1=0
n2=0
for i in range(len(nc)):
    if nc[i].isdigit():
        
        n1=n1+1
    elif nc[i].isalpha():
        n2=n2+1
    else:
        n3=0
if n1>=1 and n2>=1:
    print("Yes")
else:
    print("No")
