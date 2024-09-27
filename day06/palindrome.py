import string;
import re;

def formatage(s) :
    ponctuation = f"[{re.escape(string.punctuation)}]";
    res = s.lower();
    res = res.replace(" ","");
    res = re.sub(ponctuation, "", res);
    return res;

def palindrome(s, lettreDeb = 0, palin = True) :
    if len(s) > 1 :
        if palin and (lettreDeb <= len(s)/2) :
            if s[lettreDeb] == s[len(s)-lettreDeb-1] :
                palindrome(s, lettreDeb+1, True);
            else :
                palindrome(s, lettreDeb+1, False);
        elif palin and (lettreDeb > len(s)/2):
            print("C'est un palindrome !");
        else :
            print("Ce n'est pas un palindrome.");
            
    else :
        print("La chaine est trop courte pour etre un palindrome.\n");

s = input("Rentrer la phrase a verifier :\n");
sformat = formatage(s);
palindrome(formatage(s));

     
    

