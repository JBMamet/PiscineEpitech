import re;

s = input("Rentrer le texte :\n");
res = "";
temp = "";
phrases = re.split(r'[\.!?]', s);

def premierMot(s) :
	return s.split(" ", 1)[0];

for i in range(len(phrases)) :
	temp = phrases[i].strip(" ");
	res = res + premierMot(temp);
	if i != (len(phrases)-2) :
		res = res + " ";
	else :
		res = res + ".";

print(res.capitalize());
