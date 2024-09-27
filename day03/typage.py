inp = input("Rentrer un nombre entier :\n");

try :
	inp = int(inp);
except :
	print("Ce n'est pas un nombre entier !");

print(type(inp));
