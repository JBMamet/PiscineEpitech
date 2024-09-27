import string
s = input("Rentrer le message a encoder :\n");
key = int(input("Rentrer la clef d'encodage :\n"));
ref = string.printable;
caesar = "";

def posAfterCaesar(char, key, ref) :
	return ((ref.find(char)+key)%len(ref));
	
for char in range(len(s)) :
	caesar = caesar + ref[posAfterCaesar(s[char],key,ref)];

print(caesar);
