# Author: Willow Traylor
# Date: 09/09/2025
# Your student id: 67975434
# Your email: wtraylor@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): n/a
from turtle import *
def draw_circle(turtle,x,y,color,radius):
    turtle.penup()
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(turtle,x,y,color,len1,len2):
    turtle.penup()
    turtle.goto(x,y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.pendown()
    for i in range(2):
        turtle.forward(len1)
        turtle.left(90)
        turtle.forward(len2)
        turtle.left(90)
    turtle.end_fill()


def draw_triangle(turtle,x,y,color,len):
    turtle.penup()
    turtle.pensize(5)
    turtle.goto(x,y)
    turtle.color(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(len)
        turtle.right(120)
    turtle.end_fill()


def draw_aquarium(turtle):
    draw_rectangle(turtle, -400,-400,'burlywood2',800,100)#Sand

    draw_circle(turtle,0,0,'deeppink',50) #Fish 1
    turtle.setheading(180)
    draw_triangle(turtle,100,50,'deeppink',100)
    draw_circle(turtle,-20, 80,'white',10)
    draw_circle(turtle,-20, 70,'black',5)

    draw_circle(turtle,-220,-70,'coral',50) #Fish 2
    turtle.setheading(180)
    draw_triangle(turtle,-230,-150,'coral',100)
    draw_circle(turtle,-210, -100,'white',10)
    draw_circle(turtle,-210, -105,'black',5)

    draw_circle(turtle,200,50,'darkseagreen',50) #Fish 3
    turtle.setheading(180)
    draw_triangle(turtle,190,0,'darkseagreen',100)
    draw_circle(turtle,210, 20,'white',10)
    draw_circle(turtle,210, 15,'black',5)

def draw_W(turtle,x,y):
    turtle.penup()
    turtle.color('black')
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.right(60)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(25)
    turtle.right(120)
    turtle.forward(25)
    turtle.left(120)
    turtle.forward(50)

def draw_T(turtle,x,y):
    turtle.penup()
    turtle.pensize(5)
    turtle.color('black')
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()
    turtle.goto((x+25),y)
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(50)


def main():
    space = Screen()
    t1 = Turtle()
    space.setup(400,400)
    space.bgcolor('skyblue')
    t1.setheading(0)
    t1.pensize(1)
    draw_aquarium(t1)
    draw_W(t1,200,-250)
    draw_T(t1,300,-250)
    exitonclick()


if __name__ == '__main__':
    main()