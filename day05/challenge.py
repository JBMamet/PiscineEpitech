import time;
import random;

startingTime = time.time();

###Generation de la liste
myList = [];
for i in range(1000000) :
	myList.append(random.randint(0,2147483647));

###Quicksort : tri recursif sur un partionnement de la liste
##Fonction de tri de la partition
def partition(alist, bas, haut) :
	#On place le pivot : dernier element de la liste
	pivot = alist[haut];
	#On place le plus petit element
	i = bas - 1;
	
	#On parcours la liste dans l'intervalle [bas;haut]
	for j in range(bas, haut) :
		#Si l'élément est plus petit= que notre pivot
		if alist[j] <= pivot :
			#On met a jour la pos du plus petit
			i = i+1;
			#On echange le plus petit  avec cet element
			(alist[i], alist[j]) = (alist[j], alist[i]);
			#On echange le pivot avec le plus grand element alors stocke apres i
	(alist[i+1], alist[haut]) = (alist[haut], alist[i+1]);

	#On renvoie l'emplacement du pivot de la partition
	return (i+1);
	
##Fonction de partionnement, quickSort
def quickSort(alist, bas, haut) :
	#On verifie que la partition a suffisement d'elements
	if bas < haut :
		#On trie la partition actuelle et on recupere le pivot
		pivot = partition(alist, bas, haut)
		#On appelle le tri pour la gauche du pivot
		quickSort(alist, bas, pivot -1);
		##On appelle le tri pour la droite du pivot
		quickSort(alist, pivot +1, haut)

quickSort(myList, 0, len(myList)-1);
#print(myList);

duration = time.time()- startingTime;
print(duration);
