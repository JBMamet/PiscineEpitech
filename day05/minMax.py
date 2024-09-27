import random;

myList = [];
for i in range(10) :
	myList.append(random.randint(0,100));

print(myList);

def getMinMax(list) :
	print("Le min est : " + str(min(list)) + "\n");
	print("Le max est : " + str(max(list)) + "\n");
	
getMinMax(myList);
