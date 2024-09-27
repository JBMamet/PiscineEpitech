imp = 1;
count = 1;
tic = True;
pi = 0;
txt = "{:.6f}";

while txt.format(4*pi) != "3.141593"  :
	if tic :
		pi = pi + 1/imp;
		imp = imp+2;
		count = count +1;
		tic = False;
	else :
		pi = pi - 1/imp;
		imp = imp+2;
		count = count +1;
		tic = True;
		
		
print("On obtient ", txt.format(4*pi), "avec ", str(count), "divisions");
