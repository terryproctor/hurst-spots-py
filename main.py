from colorgram import extract
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.penup()
timmy.speed("fastest")
x = -200
y = -200
timmy.setposition(x, y)

# Extract 6 colors from an image.
colors = extract('images/spots_1.jpg', 40)

rgb_colors = []
for color in colors:
    
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
#don't add white colors
    if r + g + b < 600:
        rgb_colors.append((r, g, b))

line = 0

def move_turtle():
    global x
    global line
    
    for _ in range(10):
        random_col = random.choice(rgb_colors)
        timmy.dot(20, random_col)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    line += 1
    timmy.penup()
    timmy.setposition(x, timmy.ycor() + 50)
    

while line < 10:
    move_turtle()
timmy.hideturtle()
screen.exitonclick()    


move_turtle()
