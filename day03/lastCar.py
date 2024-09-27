s = input("Rentrer une chaine de caractères :\n");
print("Le dernier caractère est : ", s[len(s)-1]);

if len(s) < 10 :
	print("La chaine est trop courte !");
else :
	print("Les caractères 5 à 10 sont : ", s[4:9]);

