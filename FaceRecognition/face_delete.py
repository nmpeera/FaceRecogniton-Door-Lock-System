import os

name = input("Please Enter User ID:")

Count = 1

for i in range(Count,31):
	file = "./Dataset/User." +str(name) +'.' + str(i) + ".jpg"
	os.remove(file)

