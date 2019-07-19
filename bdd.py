start,end=map(int,(input().split()))
for n2 in range (start,end):
    n1=n2
    s=0
    while n2!=0:
        r=n2%10
        s=s+r**3
        n2=n2//10
    if s==n1:
      print(n1,end="")
