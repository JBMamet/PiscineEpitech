def takeAndDelete(list) :
	if len(list) > 1 :
		del list[len(list)-1];
		for l in list :
			print(l);
	else :
		print("La liste est vide !");

myList = [0];
#print(str(myList[0]) + "\n");
#print(str(myList[len(myList)-1]) + "\n");
#myList.append(5);
#for l in myList :
#	print(str(l));
#print();
	
takeAndDelete(myList);
