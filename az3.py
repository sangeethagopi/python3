z111=input()
n21=len(z111)
if n2%2!=0:
    z111=z111[:int(n2/2)]+'*'+z111[int(n2/2)+1:n2]
else:
    z111=z111[:int(n2/2)-1]+'**'+z111[int(n2/2)+1:n2]
print(z111)
