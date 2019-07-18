a=input("")
a=a.casefold()
ss=reversed(a)
if list(a) == list(ss):
    print("yes")
else:
    print("no")
