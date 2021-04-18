# import necessary modules
import colorgram
import random
from turtle import Turtle, Screen
import turtle

# Get user input and validation
print("Color Extractor")
image = input("Enter the path of the target image: ")
num = int(input("Enter the number of colors to extract from the image: "))
print()
print(f"You have chosen to extract the {num} most common colors from the target image.")
print("Your list will be output to terminal. The hues selected will be displayed.")

# Extraction
colors = colorgram.extract(image, num)
rgb_colors = []
for color in colors:  # iterate through list of colors
    # find the r, g, b values
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)  # create new tuple
    rgb_colors.append(new_color)  # append tuple to rgb_colors list

print(rgb_colors)

# copy the printed rgb_colors list. paste it into your program with the
# variable name you choose. ex: colors_to_use = [PASTE HERE]

# Turtle Object Attributes
turtle.colormode(255)
picasso = Turtle()
picasso.penup()
picasso.hideturtle()
picasso.setheading(225)
picasso.forward(300)
picasso.setheading(0)

# Screen Object Attributes
screen = Screen()
screen.bgcolor("gray40")

# Display selected hues against neutral gray (40%) background
hues = rgb_colors
for count in range(1, 101):
    picasso.dot(40, random.choice(hues))
    picasso.forward(50)
    if count % 10 == 0:
        picasso.setheading(90)
        picasso.forward(50)
        picasso.setheading(180)
        picasso.forward(500)
        picasso.setheading(0)
# Exit screen
screen.exitonclick()
