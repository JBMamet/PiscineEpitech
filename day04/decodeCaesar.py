import string
caesar = input("Rentrer le texte a decoder :\n");
key = int(input("Rentrer la clef de cryptage :\n"));
ref = string.printable;
s = "";

def posRewindCaesar(char, key, ref) :
	return ((ref.find(char)-key)%len(ref));
	
for char in range(len(caesar)) :
	s = s + ref[posRewindCaesar(caesar[char],key,ref)];

print(s);
