a,b=map(int,input().split())
for num in range(a,b):
  sum=0
  temp=num
  while(temp>0):
     sum=sum+(temp%10)**3
     temp=temp//10
  if(sum==num):
     print(num,end=" ")
