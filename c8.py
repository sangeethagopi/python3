pc=int(input())
bc=[]
for i in range(pc):
  c=input()
  bc.append(c)
d=[]
for i in zip(*cb):
  if(i.count(i[0])==len(i)):
    d.append(i[0])
  else:
    break
print(''.join(d))
