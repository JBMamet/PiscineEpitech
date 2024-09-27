s = input("Rentrer une phrase :");
s = s.lower();
sReverse = s[::-1];

def CatGardenMice(s,sReverse) :
	count = 0;
	count  = s.count("cat") + s.count("mice") + s.count("garden") + sReverse.count("cat") + sReverse.count("mice") + sReverse.count("garden");
	return count;
	
print(str(CatGardenMice(s, sReverse)));
