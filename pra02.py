import pra01
x = int(input("想知道我的名字請輸入1想知道我的學號請輸入2"))
print("您輸入的是{}".format(x))
if(x==1):
	print(pra01.pra01())
if(x==2):
	print(pra01.pra02())
if(x>2):
	print("請不要輸入1或2以外的數字")
