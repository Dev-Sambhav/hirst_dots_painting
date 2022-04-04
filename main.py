# import colorgram

# colors = colorgram.extract("hirst_img.jpg", 30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append(tuple(color.rgb))

import turtle
import random

colors_list = [(237, 240, 245), (8, 18, 35), (151, 86, 54), (49, 32, 23), (234, 208, 86), (31, 98, 148),
               (195, 139, 122), (94, 5, 19), (151, 65, 96), (205, 97, 74), (162, 160, 45), (97, 162, 202), (23, 93, 62),
               (164, 135, 161), (143, 16, 39), (121, 202, 180), (2, 63, 140), (142, 39, 31), (49, 113, 77), (7, 57, 40),
               (179, 87, 121), (143, 217, 227), (209, 177, 215), (121, 220, 218), (61, 157, 82), (56, 73, 36),
               (57, 133, 200)]

t = turtle.Turtle()
t.speed("fastest")
turtle.colormode(255)
t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)


def hirst_dot():
    for step1 in range(10):
        t.dot(20, random.choice(colors_list))
        t.forward(50)


def set_pos():
    t.backward(500)
    t.left(90)
    t.forward(50)
    t.right(90)


for _ in range(10):
    hirst_dot()
    set_pos()

# hide the turtle at the last
t.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
