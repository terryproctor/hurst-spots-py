from colorgram import extract
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed("fastest")
x = -200
y = -200
timmy.setposition(x, y)
timmy.penup()

# Extract colors from an image.
colors = extract('images/spots_1.jpg', 80)

rgb_colors = []
for color in colors:
    
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
#don't add white colors
    if r + g + b < 600:
        rgb_colors.append((r, g, b))


def move_turtle():
    global x
    
    for _ in range(10):
        random_col = random.choice(rgb_colors)
        timmy.dot(20, random_col)
        timmy.forward(50)
        
    timmy.penup()
    timmy.setposition(x, timmy.ycor() + 50)

for _ in range(10):
    move_turtle()
screen.exitonclick()    


move_turtle()
