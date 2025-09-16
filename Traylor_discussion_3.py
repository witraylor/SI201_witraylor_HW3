# Author: Willow Traylor
# Date: 09/10/2025
# Class: SI206 Discussion 3
# Usage: use turtle to draw an emoji
from turtle import *

### write all new functions here ###
def draw_circle(turtle,color, xpos, ypos, radius):
    turtle.penup()
    turtle.goto(xpos,ypos)
    turtle.color(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()

def draw_arc(turtle,color,xpos,ypos,radius,extent,thickness):
    turtle.penup()
    turtle.goto(xpos,ypos)
    turtle.color(color)
    turtle.pensize(thickness)
    turtle.pendown()
    turtle.circle(radius,extent)





def draw_emoji(turtle):
    turtle.setheading(0)
    draw_circle(turtle, 'yellow', 0, -100, 200)
    draw_circle(turtle, 'black', -100, 100, 25)
    draw_circle(turtle, 'black', 100, 100, 25)
    turtle.right(90)
    draw_arc(turtle,'red',-100,50,100,180,50)
    exitonclick()
    """
    Write a function to draw an emoji.
    """

    pass

def main():
    space = Screen()
    t1 = Turtle()
    space.bgcolor('blue')
    draw_emoji(t1)
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_emoji.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.

    """

    pass


if __name__ == '__main__':
    main()


