sa10,pa10=map(int,input().split())
maxima=max(sa10,pa10)
while(1):
 if(maxima%sa10==0 and maxima%pa10==0):
  print(maxima)
  break
 maxima+=1
