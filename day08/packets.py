import pyjokes;
import turtle;

print(pyjokes.get_joke("en","chuck"))


# turtle.color('blue');
# turtle.width(5);
# turtle.forward(100);
# turtle.left(90);
# turtle.forward(100);
# turtle.left(90);
# turtle.forward(100);
# turtle.left(90);
# turtle.forward(100);

# toto = turtle.Screen()
# toto.bgcolor( "black" )
# titi = turtle.Turtle()
# titi.color( "red" )
# for i in range(3) :
#     titi.right(90)
#     titi.circle(42)
# toto.exitonclick()

toto = turtle.Screen()
toto.bgcolor( "black" )

def drawPolygon(sides) :
    poly = turtle.Turtle();
    poly.color("purple");
    poly.width(5);

    for i in range(sides) :
        poly.right(360/sides);
        poly.forward(100);

#La taille est un multiple de 90
def drawSpiral(taille, angle) :
    pirulo = turtle.Turtle();
    pirulo.width(3);
    pirulo.color("green");

    for i in range(taille * 90) :
        pirulo.circle(i, angle); 


#drawPolygon(6);
drawSpiral(2, 40);
toto.exitonclick();