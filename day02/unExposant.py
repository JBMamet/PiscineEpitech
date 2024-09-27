nbUn = input('Combien de 1 ?\n');
pow = input('A quel exposant ?\n');
chaine = "";

for i in range(int(nbUn)) :
	chaine = chaine + "1";
	
print(int(chaine)**int(pow))
