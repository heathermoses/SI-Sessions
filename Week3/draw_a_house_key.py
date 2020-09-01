"""
Week 3 SI Session B
Author: Heather Moses (hlm8500@rit.edu)
Date: 9/1/20
Course: SWEN/CSEC-123-11

This program is the key to the draw_a_house activity
"""
import turtle
import math

def init():
    """
    Initializes the position of turtle to bottom left corner of canvas
    """
    turtle.up()
    turtle.back(300)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.down()


def draw_rectangle(height, width):
    """
    Draws a rectangle
    Precondition: turtle starts down in the bottom left corner of rectangle
    Postcondition: turtle ends in the same position as precondition
    Parameter height means the height of the rectangle
    Parameter width means the width of the rectangle
    """
    turtle.down()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

def draw_roof(height, width):
    """
    Draws an isosceles triangle (roof)
    Precondition: Turtle starts down in the bottom left corner of the triangle
    Postcondition: Turtle ends in the same position as the precondition
    Parameter base refers to the base of the triangle
    Parameter height refers to the height of the triangle
    Hypotenuse refers to the hypotenuse of the triangle (roof)
    Angle refers to the angle of the triangle (roof)
    """
    hypotenuse = math.sqrt(((width/2)**2)+(height)**2)
    angle = (math.atan((2*height)/width))*(180/math.pi)
    turtle.down()
    turtle.forward(width)
    turtle.left(180 - angle)
    turtle.forward(hypotenuse)
    turtle.left(180 - (180-(2*angle)))
    turtle.forward(hypotenuse)
    turtle.left(180 - angle)

def draw_a_house(height, width):
    draw_rectangle(height, width)
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    draw_roof(height, width)
    turtle.done()

def main():
    init()
    draw_a_house(250, 500)

main()