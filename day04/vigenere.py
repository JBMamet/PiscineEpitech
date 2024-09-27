import string

ref = string.printable;
choix = "";
vigenereRes = "";
texteRes = "";

def getVigenerePos(char, keyT, ref) :
	pos = ref.find(char)+ref.find(keyT);
	pos = pos%len(ref);
	return pos;
	
def getTextePos(char, keyT, ref) :
	pos = len(ref) + ref.find(char) - ref.find(keyT);
	pos = pos%len(ref);
	return pos;


while choix == "" :
	choix = input("Encoder ou decoder du Vigenere ?\n");
	if choix.lower() == "encoder" :
		texte = input("Rentrer le texte a encoder :\n");
		key = input("Rentrer la cle :\n");
		for char in range(len(texte)) :
			vigenereRes = vigenereRes + ref[getVigenerePos(texte[char],key[char%len(key)],ref)];
		print(vigenereRes);
		
	elif choix.lower() == "decoder" :
		vigenere = input("Rentrer le texte a decoder :\n");
		key = input("Rentrer la cle :\n");
		for char in range(len(vigenere)) :
			texteRes = texteRes + ref[getTextePos(vigenere[char], key[char%len(key)], ref)];	
		print(texteRes);
	else :
		print("Je n'ai pas compris\n");
		choix = "";	


	

