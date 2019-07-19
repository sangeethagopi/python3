ac,bc=map(int,input().split())
for num1 in range(ac,bc):
  sum=0
  temp=num1
  while(temp>0):
     sum=sum+(temp%10)**3
     temp=temp//10
  if(sum==num1):
     print(num1,end=" ")
