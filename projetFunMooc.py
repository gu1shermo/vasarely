import turtle
from math import pi, sin, cos, sqrt, acos, asin, atan2


def hexagone(point, longueur, col, centre, rayon):
    t = turtle.Turtle()
    t.speed(1)
    coord_x = point[0]
    coord_y = point[1]
   



    t.setpos(coord_x,coord_y)
    # t.goto(coord_x,coord_y)
    # dessin face nord est
    t.color('red')

    t.begin_fill()
    t.fd(longueur)
    t.lt(120)
    t.fd(longueur)
    t.lt(60)
    t.fd(longueur)
    t.lt(120)
    t.fd(longueur)
    
    t.end_fill()
    # dessin face nord ouest
    t.lt(180)
    t.color('black')
    t.begin_fill()
    t.fd(longueur)
    t.lt(120)
    t.fd(longueur)
    t.lt(60)
    t.fd(longueur)
    t.lt(120)
    t.fd(longueur)
    
    t.end_fill()

    # dessin face sud est
    t.lt(180)
    t.color('blue')
    t.begin_fill()
    t.fd(longueur)
    t.lt(120)
    t.fd(longueur)
    t.lt(60)
    t.fd(longueur)
    t.lt(120)
    t.fd(longueur)
    
    t.end_fill()
    



if __name__ == "__main__": # code de test
    hexagone((50,50),100,0,0,0) 