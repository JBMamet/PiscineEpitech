import random
myList = [0,1,2,3,4,5,6,7,8,9];
aList = [];

def reverseList(list) :
	return list[::-1];

def oneOfTwo(list) :
	return list[::2];
	
def add17(list) :
	for i in range(17) :
		list.append(random.randint(0,9));
	return list;
	
	
print(myList[2:6]);
print(reverseList(myList));
print(oneOfTwo(myList));
print(add17(aList));

my_first_list = [7 , 8 , 9]
my_second_list = [4 , 5 , 6]
my_first_list = [* my_first_list , * my_second_list ]
print(my_first_list);
