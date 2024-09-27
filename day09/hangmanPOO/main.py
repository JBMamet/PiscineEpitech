import random;
import sys;
import os;
from player import Player;
#from hangman import Hangman;

secours = [
    'chat', 'chien', 'oiseau', 'voiture', 'maison', 'arbre', 'fleur', 'ordinateur', 'paysage', 'bouteille',
    'soleil', 'mer', 'lune', 'montagne', 'ecole', 'bureau', 'lampe', 'telephone', 'livre', 'stylo',
    'ordinateur', 'elephant', 'arbre', 'bouteille', 'restaurant', 'cheminee', 'piano', 'maillot', 'volcan',
    'bijou', 'grandeur', 'musique', 'reverie', 'printemps', 'mystere', 'batterie'
];
jeu = True;
player1 = Player.__init__("test");
print(player1.getPenalties());