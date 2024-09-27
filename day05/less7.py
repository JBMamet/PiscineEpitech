import random;

myList = [];

for i in range(20) :
	myList.append(random.randint(0,9));
	
print(myList);
	
def less7(list) :
	res = [];
	for l in list :
		if l < 7 :
			res.append(l);
	return res;
	
print(less7(myList));
