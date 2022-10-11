def square (y):
		print("{}的平方是{}".format(y,y*y))


x = int(input("請輸入一個數字"))
print ("您輸入的是{}".format(x))
if(x==0):
	print("您輸入的是0不能平方")
else:
	print("您輸入的是正數")
	for i in range(x):
		square (i)

	
