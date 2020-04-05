import turtle
from math import pi, sin, cos, sqrt, acos, asin, atan2
from random import random, uniform

def deformation(p, centre, rayon):
    """ Calcul des coordonnées d'un point suite à la déformation 
        engendrée par la sphère émergeante
        Entrées :
          p : coordonnées (x, y, z) du point du dalage à tracer 
             (z = 0) AVANT déformation
          centre : coordonnées (X0, Y0, Z0) du centre de la sphère
          rayon : rayon de la sphère
        Sorties : coordonnées (xprim, yprim, zprim) du point du dallage 
             à tracer APRÈS déformation
    """
    x, y, z = p
    xprim, yprim, zprim = x, y, z
    xc, yc, zc = centre
    if rayon**2 > zc**2:
        zc = zc if zc <= 0 else -zc
        r = sqrt(
            (x - xc) ** 2 + (y - yc) ** 2)  # distance horizontale 
            # depuis le point à dessiner jusqu'à l'axe de la sphère
        rayon_emerge = sqrt(rayon ** 2 - zc ** 2) # rayon de la partie
            # émergée de la sphère
        rprim = rayon * sin(acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge: # calcul de la déformation 
            # dans les autres cas
            xprim = xc + (x - xc) * rprim / r # les nouvelles coordonnées
            # sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = asin(rprim / rayon)
            zprim = zc + rayon * cos(beta)
            if centre[2] > 0:
                zprim = -zprim
    return (xprim, yprim, zprim)


def hexagone(point, longueur, col, centre, rayon,t,width,height,x,y):
    t.speed(0)
    x_center = point[0]
    y_center = point[1]

    is_deformed = False
    # z_center = point[2]
    
    hex1 = (x_center + cos(0) * longueur, y_center,0)
    hex2 = (x_center + cos(pi/3) * longueur, y_center + sin(pi/3) * longueur,0)
    hex3 = (x_center + cos(2*pi/3) * longueur, y_center + sin(2*pi/3) * longueur,0)
    hex4 = (x_center + cos(pi) * longueur, y_center,0)
    hex5 = (x_center + cos(-2*pi/3) * longueur, y_center + sin(-2*pi/3) * longueur,0)
    hex6 = (x_center + cos(-pi/3) * longueur, y_center + sin(-pi/3) * longueur,0)
   
    

    # avec deformation
    new_point = deformation(point,centre,rayon)
    
    # print(centre)
    is_deformed = (
        new_point != point
        )
    # print('is_deformed: ' + str(is_deformed))
    if is_deformed:
        # draw
        point = new_point
        hex1 = deformation(hex1,centre,rayon)
        hex2 = deformation(hex2,centre,rayon)
        hex3 = deformation(hex3,centre,rayon)
        hex4 = deformation(hex4,centre,rayon)
        hex5 = deformation(hex5,centre,rayon)
        hex6 = deformation(hex6,centre,rayon)

        # color
        color0 = (1 - x/width,0,0)
        color1 = (0,1 - y/width,0)
        color2 = (0,0,1-(x/width + y/height)/2)
        
    else:
        color0 = (x/width,x/width,x/width)
        color1 = (y/height,y/height,y/height)
        color2 = ((x/width + y/height)/2,(x/width + y/height)/2,(x/width + y/height)/2)
        # r0 = uniform(0.5,1)
        # r1 = uniform(0.5,1)
        # r2 = uniform(0.5,1)
        # color0 = (r0,r1,r2)
        # color1 = (r0,r1,r2)
        # color2 = (r0,r1,r2)
        pass
    

    
    


    # draw
    # go center , no drawing
    t.penup()
    t.goto(point[0],point[1])

    # begin draw
    t.pendown()

    # color0
    # color0 = col[0]
    # r = random()
    # color0 = (random(),random(),random())
    t.color(color0)
    
    t.begin_fill()
    t.goto(hex1[0],hex1[1])
    t.goto(hex2[0],hex2[1])
    t.goto(hex3[0],hex3[1])
    t.goto(point[0],point[1])
    t.end_fill()
    # color1
    # color1 = col[1]
    # r = random()
    # color1 = (random(),random(),random())
    t.color(color1)

    t.begin_fill()
    t.goto(hex3[0],hex3[1])
    t.goto(hex4[0],hex4[1])
    t.goto(hex5[0],hex5[1])
    t.goto(point[0],point[1])
    t.end_fill()
    # color2
    # color2 = col[2]
    # r = random()
    # color2 = (random(),random(),random())
    t.color(color2)
    
    t.begin_fill()
    t.goto(hex5[0],hex5[1])
    t.goto(hex6[0],hex6[1])
    t.goto(hex1[0],hex1[1])
    t.goto(point[0],point[1])
    t.end_fill()

    t.hideturtle()


def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon,t):
    x_min = inf_gauche
    x_max = sup_droit
    y_min = inf_gauche
    y_max = sup_droit
    marge_x = 3 * longueur

    width = sup_droit - inf_gauche
    height = sup_droit - inf_gauche
    
    loop = 0
    while y_min <= y_max:
        if loop % 2 == 0:
            x_min = inf_gauche
        else:
            x_min = inf_gauche + longueur + longueur/2
        while x_min <= x_max:
            x = x_min - inf_gauche
            y = y_min - inf_gauche
            hexagone((x_min,y_min,0), longueur, col, centre, rayon,t,width,height,x,y)
            x_min += marge_x
        
            # hexagone((x_min,y_min,0), longueur, col, centre, rayon,t)
            
        x_min = inf_gauche
        y_min += sin(pi/3) * longueur
        loop +=1
    

def vasarely(inf_g,sup_d,longueur,col,centre,r):
    t = turtle.Turtle()
    pavage(inf_g,sup_d,longueur,col,centre,r,t) 
    ts = t.getscreen()
    ts.getcanvas().postscript(file="vasarely_isDeformed_gradient_grey_color_3.eps")
    turtle.done()

if __name__ == "__main__": # code de test
    # hexagone((200,200,0),50,('red','black','blue'),0,0) 
    # pavage(-200,200,30,('red','black','blue'),0,0)
    
    vasarely(-150,150,10,((1,random(),random()),(1,random(),random()),(1,random(),random())),(0, 0, 0),500)
    