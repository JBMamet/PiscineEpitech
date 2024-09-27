entier = int(input("Entrer un entier :\n"));

for i in range(2, entier//2 + 1) :
	compteur = 1;
	res = "";
	while i*compteur < entier :
		res = str(i*compteur) + " " + res;
		compteur += 1;
	print(res);
