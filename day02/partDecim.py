inp = input("Rentrer un nombre :\n");
res = "";
boucle = 0;

while boucle < len(inp) :
	if inp[boucle] == '.' :
		boucle = boucle + 1;
		break;
	else :
		boucle = boucle + 1;
		
for i in range(len(inp) - boucle) :
	res = res + inp[boucle + i];

print("La partie decimale est : ", res);
