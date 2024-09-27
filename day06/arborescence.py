import os;

def affichage(s) :
    for root, dirs, files in os.walk(s) :
        for name in files :
            print(os.path.join(root, name));
        for name in dirs :
            print(os.path.join(root, name));

s = input();
affichage(s);