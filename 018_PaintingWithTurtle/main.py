from turtle import Turtle, Screen
import random
import colorgram


ninja = Turtle()
ninja.shape("arrow")
ninja.pensize(2)
ninja.speed("fastest")

direction = [0, 90, 180, 270]

#made from pick color output
color_list = [(198, 165, 118), (144, 80, 55), (221, 202, 136), (60, 95, 122), (168, 151, 50), (135, 162, 181), (133, 33, 21), (51, 120, 87), (74, 37, 29), (193, 95, 80), (145, 177, 150), (105, 74, 78), (166, 146, 156), (19, 92, 69), (27, 59, 77), (227, 176, 166), (59, 43, 46), (138, 27, 33), (180, 203, 178), (26, 84, 89), (86, 148, 129), (12, 70, 58), (43, 64, 89), (180, 97, 102), (219, 179, 183), (182, 191, 204)]

screen = Screen()
screen.colormode(255)

def pick_color():
    colors = colorgram.extract("image.jpeg", 30)
    color_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_list.append((r,g,b))


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    ninja.color(R, G, B)

def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        change_color()
        ninja.circle(100)
        ninja.setheading(ninja.heading() + gap)
#draw_spirograph(5)

def draw_Hirst_painting():
    for _ in range(10):
        for _ in range(10):
            color = random.choice(color_list)
            #print(color)
            #ninja.color(color[0],color[1],color[2])
            ninja.pendown()
            ninja.color(color)
            ninja.fillcolor(color)
            ninja.begin_fill()
            ninja.circle(5)
            ninja.end_fill()
            ninja.penup()
            ninja.forward(20)

        ninja.backward(200)
        ninja.left(90)
        ninja.forward(20)
        ninja.right(90)

draw_Hirst_painting()


screen.exitonclick()
