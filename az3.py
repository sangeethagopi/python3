ss=input()
n2=len(ss)
if n2%2!=0:
    ss=ss[:int(n2/2)]+'*'+ss[int(n2/2)+1:n2]
else:
    ss=ss[:int(n2/2)-1]+'**'+ss[int(n2/2)+1:n2]
print(ss)
