ac2,cc2=input("").split()
cc2=int(cc2)
b=ac2[len(ac2)-cc2]
for i in range(len(ac2)-(cc2-1),len(ac2)):
  b+=ac2[i]
print(b)
