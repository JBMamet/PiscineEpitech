inp = input("Rentrer un nombre :\n");
res = "";
boucle = 0;

while boucle < len(inp) :
	if inp[boucle] == '.' :
		break;
	else :
		res = res + inp[boucle];
		boucle = boucle + 1;

print("La partie entiere est : ", res);
