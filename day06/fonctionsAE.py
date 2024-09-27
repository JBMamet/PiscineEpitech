import re;
import string;

def nbLower(s : str, n : int) :
    lower = re.sub(r'[^a-z]', "", s);
    if len(lower) < n :
        return False;
    else :
        return True;

def nbUpper(s : str, n : int) :
    upper = re.sub(r'[^A-Z]', "", s);
    if len(upper) < n :
        return False;
    else :
        return True;

def nbChar(s : str, n : int) :
    if len(s) < n :
        return False;
    else :
        return True;

def nbNumber(s : str, n : int) :
    upper = re.sub(r'[^0-9]', "", s);
    if len(upper) < n :
        return False;
    else :
        return True;

def nbSpecial(s : str, n : int) :
    spec = re.sub(f'[^{string.punctuation}]', "", s);
    if len(spec) < n :
        return False;
    else :
        return True;

s = input("Rentrer une chaine de caracteres :\n");
#i = int(input("Rentrer un nombre :\n"));

def checkPassword(function, s : str, i : int) :
    return function(s,i);

if (checkPassword(nbLower, s, 4)) == True and (checkPassword(nbSpecial, s, 2)) == True :
    print("Ok");
else :
    print("No");