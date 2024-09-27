import random

myList = [];

for i in range(10) :
	myList.append(random.randint(1,9));
	
print(myList);
	
def addList(list) :
	res = list[0];
	for i in range(len(list)-1) :
		res = res * list[1+1];
	return res;
	
print(addList(myList));
