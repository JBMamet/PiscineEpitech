import pygame;
from pygame.locals import *;
import turtle;

game = True;
pygame.init();

def stickman(surface) :
    #Tete
    pygame.draw.circle(surface, "purple", (300, 150), 25, 3);
    #Torse
    pygame.draw.line(surface, "purple", (300, 175), (300,300), 3);
    #Bras droit
    pygame.draw.line(surface, "purple", (300, 200), (320,250), 3);#coude
    pygame.draw.line(surface, "purple", (320,250), (350,250), 3);#avant-bras
    pygame.draw.circle(surface, "purple", (357.5, 250), 7.5, 0);#main
    #Bras gauche
    pygame.draw.line(surface, "purple", (300, 200), (280,250), 3);#coude
    pygame.draw.line(surface, "purple", (280,250), (250,250), 3);#avant-bras
    pygame.draw.circle(surface, "purple", (257.5, 250), 7.5, 0);#main
    #Jambe droite
    pygame.draw.line(surface, "purple", (300, 300), (360,310), 3);#cuisse
    pygame.draw.line(surface, "purple", (360,310), (360,355), 3);#mollet
    pygame.draw.line(surface, "purple", (360,355), (375,362), 3);#pied
    #Jambe droite
    pygame.draw.line(surface, "purple", (300, 300), (240,310), 3);#cuisse
    pygame.draw.line(surface, "purple", (240,310), (240,355), 3);#mollet
    pygame.draw.line(surface, "purple", (240,355), (225,362), 3);#pied



fenetre = pygame.display.set_mode((600,600));
#fond = pygame.image.load("images/seaOfStarsWhite.png").convert_alpha();


while game :
    #fenetre.blit(fond, (0,0));
    stickman(fenetre);
    pygame.display.flip();
    pygame.event.wait();
    for event in pygame.event.get() :
        if event.type == MOUSEBUTTONDOWN :
            game = False;
        if event.type == QUIT :
            game = False;