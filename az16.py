arr1=list(input())
yeah1=1
for i in range(len(arr1)):
	for j in range(i+1,len(arr1)):
		if arr1[i]==arr1[j]:
			print("No")
			yeah1=0
			exit()
		else:
			pass
if yeah1==1:
	print("Yes")
