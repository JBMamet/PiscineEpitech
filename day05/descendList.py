import random;

myList = [];

for i in range(20) :
	myList.append(random.randint(0,9));
	
print(myList);

print(sorted(myList, reverse = True));
