import turtle;
from turtle import *;

tortuga = turtle.Screen();
tortuga.bgcolor("black");
##Trace le triangle de base
def Sierpinski(iteration : int, compteur : int,  taille : int, pere,  couleur1 : str, couleur2 : str) :
    if compteur < iteration :
        #init
        triangle = turtle.Turtle();
        triangle.hideturtle();
        triangle.speed("fastest");
        moitie = [];
        #positionnement sur le plan
        triangle.up();
        triangle.goto(pere[0]);
        triangle.down();

        #On dessine le triangle
        triangle.fillcolor(couleur1);
        triangle.begin_fill();
        for i in range(3) :
            pere.append(triangle.pos());
            triangle.forward(taille/2);
            moitie.append(triangle.pos());
            triangle.forward(taille/2);
            triangle.left(120);
        triangle.end_fill();

        #On lance la recursion
        compteur += 1;
        sierpinski(iteration, compteur, int(0), taille/2, pere, moitie, couleur1, couleur2)


##Appel recursif pour tracer les differentes strates de Sierpinski
def sierpinski(iteration : int, compteur : int, pos : int, taille : int,  pere, moitie, couleur1 : str, couleur2 : str) :
    #Init
    tri = turtle.Turtle();
    tri.hideturtle();
    tri.speed("fastest");
    #Si il reste des strates à faire
    if(compteur < iteration) :
        #On place le curseur
        tri.up();
        tri.goto(moitie[int(0)]);
        tri.down();
        tri.left(60);

        #On dessine le nouveau triangle
        tri.fillcolor(couleur2);
        tri.begin_fill();
        for i in range(3) :
            tri.forward(taille);
            tri.left(120);
        tri.end_fill();
    
        #Calcul des nouveaux triangles
        triangles = {
            "t1" : [moitie[0], pere[1], moitie[1]],
            "t2" : [moitie[2], moitie[1], pere[2]],
            "t3" : [pere[0], moitie[0], moitie[2]]
        }
        #Incrementation et recursion
        compteur = compteur +1;

        Sierpinski(iteration, compteur, taille, triangles["t1"], couleur1, couleur2);
        Sierpinski(iteration, compteur, taille, triangles["t2"], couleur1, couleur2);
        Sierpinski(iteration, compteur, taille, triangles["t3"], couleur1, couleur2);

def init(iteration : int, taille : int, couleur1 : str, couleur2 : str) :
    triangle = turtle.Turtle();
    pere = [];
    #positionnement sur le plan
    triangle.up();
    triangle.goto([-taille/2, -(taille/3)]);
    pere.append(triangle.pos());
    #On genere le pere du premier triangle
    for i in range(2) :
        triangle.forward(taille);
        pere.append(triangle.pos());
        triangle.left(120);
    triangle.down();

    Sierpinski(iteration, 0, taille, pere, couleur1, couleur2);
    
init(12, 800, "purple", "olive");
tortuga.exitonclick();