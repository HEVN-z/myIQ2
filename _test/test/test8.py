# https://www.youtube.com/watch?v=v7W9-xSkyQo

import turtle
turtle.shapesize(10,20)
turtle.shape("triangle")

def turnleft(x,y):
    turtle.left(180)

def turnright(x,y):
    turtle.right(180)

turtle.onclick(turnleft,1)
turtle.onrelease(turnright,1)


turtle.mainloop()