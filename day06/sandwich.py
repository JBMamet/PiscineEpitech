def bread () :
    print( " <////////// > " )
def lettuce () :
    print( " ~~~~~~~~~~~~ " )
def tomato () :
    print( " O O O O O O " )
def ham () :
    print( " ============ " )

def lettuceTomatoDoubleHam() :
    bread();
    ham();
    tomato();
    ham();
    lettuce();
    bread();

def lettuceTomato() :
    bread();
    tomato();
    lettuce();
    tomato();
    lettuce();
    bread();

def serviceTime(nb, type = "LTDH") :
    if nb > 0 :
        if type.lower() == "ltdh" :
            for i in range(nb) :
                lettuceTomatoDoubleHam();
                print("\n");
        elif type.lower() == "vege" or type.lower() == "vegetarien" :
            for i in range(nb) :
                lettuceTomato();
                print("\n");
        else :
            print("Je ne connais pas cette recette");
    else :
        print("Il n'y a pas de commandes !");
        
nbSandwich = int(input("Il faut combien de sandwichs ?\n"));
recette = input("le LTDH ou le vegetarien ?\n");

if recette == "" :
    serviceTime(nbSandwich);
else :
    serviceTime(nbSandwich,recette);