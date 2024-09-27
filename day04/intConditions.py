entier = int(input("Rentrer un entier :\n"));
nothing = 0;

print("42 ?");
if entier == 42 :
	print("--> Ok\n");
else :
	print("--> No\n");
	nothing = nothing + 1;
	
print("<= 21 ?");
if entier <= 21 :
	print("--> Ok\n");
else :
	print("--> No\n");
	nothing = nothing + 1;
	
print("Even ?");
if entier/2 == 0 :
	print("--> Ok\n");
else :
	print("--> No\n");
	nothing = nothing + 1;

print("half < 21 ?");
if entier/2 < 21 :
	print("--> Ok\n");
else :
	print("--> No\n");
	nothing = nothing + 1;
	
print("odd and >= 45 ?");
if (entier/2 != 0) and entier >= 45 :
	print("--> Ok\n");
else :
	print("--> No\n");
	nothing = nothing + 1;
	
if nothing == 5 :
	print("--> You got wrong my poor friend !");
