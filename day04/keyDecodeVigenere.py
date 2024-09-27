###IMPORTS
import string

###Variables
ref = string.printable;

###Fonctions
def getTextePos(char, keyT, ref) :
	pos = len(ref) + ref.find(char) - ref.find(keyT);
	pos = pos%len(ref);
	return pos;

def decodeVigenere(vigenere, key) :
    for char in range(len(vigenere)) :
        texteRes = texteRes + ref[getTextePos(vigenere[char], key[char%len(key)], ref)];	
        print(texteRes);

def decoupeVigenere(vigenere, keySize) :
    parts = "";
    for i in range(keySize) :
         parts += vigenere[i:len(vigenere):keySize];
    if i != (keySize-1) :
         parts += ",";
    return parts;
        

###Main
vigenere = input("Rentrer le texte a decoder :\n");
keySize = int(input("Rentrer la taille de la cle :\n"));

vigenereParts = decoupeVigenere(vigenere, keySize);
print(vigenereParts);




	
