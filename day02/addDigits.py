digits = input("Rentrer la chaine de chiffres à additionner :\n");

res = 0;

for i in range(len(digits)) :
	res = res + (int(digits[i]));

print("La somme de ", digits, " = "+ str(res));
