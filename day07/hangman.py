import random;
import re;

##Variables
mots = [
    'chat', 'chien', 'oiseau', 'voiture', 'maison', 'arbre', 'fleur', 'ordinateur', 'paysage', 'bouteille',
    'soleil', 'mer', 'lune', 'montagne', 'ecole', 'bureau', 'lampe', 'telephone', 'livre', 'stylo',
    'ordinateur', 'elephant', 'arbre', 'bouteille', 'restaurant', 'cheminee', 'piano', 'maillot', 'volcan',
    'bijou', 'grandeur', 'musique', 'reverie', 'printemps', 'mystere', 'batterie'
];
jeu = True;
secretWord = "";
penalties  = 0;
playerWord = "";

##initialisation du jeu pour une nouvelle partie
def initSecret(mots) :
    global secretWord;
    global playerWord;
    global penalties;
    global jeu;

    secretWord = mots[random.randint(0,len(mots)-1)];
    penalties = 0;
    jeu = True;
    for i in range(len(secretWord)) :
        playerWord += "- ";
##calcul le score du joueur en fonction de la lettre ou du mot rentre
def scoring(guess : str) :
    global secretWord;
    global playerWord;
    global penalties;
    global jeu;

    #Si un mot est rentre
    if len(guess) > 1 :
        #Si il est faux : +5penalites
        if guess != secretWord :
            penalties += 5;
            affichage(guess);
        #Sinon le joueur gagne
        else :
            affichage(guess);
    #sinon si c'est une lettre
    else :
        #Qui est dans le mot secret : +1P
        if guess in secretWord :
            penalties += 1;
            affichage(guess);
            
        #Qui n'est pas dans le mot secret : +3P
        else :
            penalties += 3;
            affichage(guess);

##Fait l'affichage et actualise la chaine player si il trouve le mot au une lettre
def affichage(guess : str) :
    global secretWord;
    global playerWord;
    global penalties;
    compteur = 0;
    temp = "";
    
    #Si le mot est trouve, on remplace tous les "-" par les lettres du mot et on affiche le message de victoire
    if guess == secretWord :
        temp += secretWord.upper();            
        playerWord = temp;

        if endGame() :
            print(playerWord);
            print("Felictitations !");
            print("Vous avez trouve le mot en", str(penalties),("penalite" if penalties < 2 else "penalites"));
    
    #Sinon si la lettre existe dans le mot, on remplace dans les "-" correspondants par la lettre
    elif len(guess) == 1 and guess in secretWord :
        for i in range(len(secretWord)) :
            if secretWord[i] == guess :
                compteur += 1;
                temp += secretWord[i].upper() + " ";
            
            else :
                temp += playerWord[i*2] + " ";
        
        playerWord = temp;

        if endGame() :
            print(playerWord);
            print("Felictitations !");
            print("Vous avez trouve le mot en", str(penalties),("penalite" if penalties < 2 else "penalites"));
        
        else :
            print("Il y a", str(compteur), ("occurence" if compteur < 2 else "occurences") + " de", guess);
            print(playerWord);
            print("Vous avez pris", str(penalties),("penalite" if penalties < 2 else "penalites"));
    else :
        print("Il y a", str(compteur), ("occurence" if compteur < 2 else "occurences") + " de \'", guess + "\'");
        print(playerWord);
        print("Vous avez pris", str(penalties),("penalite" if penalties < 2 else "penalites"));

def endGame() :
    global playerWord;
    global jeu;

    if playerWord.find("-") == -1 :
        jeu = False;
        return True;
    else :
        return False;




# print("Voici le jeu du pendu : Vous devez deviner le mot en prenant le moins de penalite.\n1 lettre correcte -> 1 penalite\n1 lettre fausse -> 3 penalites\n 1 mot correct -> gagne !\n 1 mot faux -> 5 penalites");
# initSecret(mots);
# #Boucle de la partie
# while jeu :
#     print(playerWord);
#     guess = input("Rentrer une lettre ou un mot : ('exit' pour quitter le programme)\n").lower();
#     #Tant qu'on ne demande pas de sortir
#     if guess != "exit" :
#         scoring(guess);
#     #Sortie par exit    
#     else :
#         win = True;
#         jeu = False;
#         print("Au revoir !");








