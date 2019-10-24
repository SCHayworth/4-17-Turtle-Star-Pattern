# Program 4-17 Turtle Graphics: Star Pattern
# Shaun Hayworth
# CIS 2
# 10-24-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/4-17-Turtle-Star-Pattern

# Creates an 8-pointed star pattern using the turtle graphics library.

# Import the turtle module
import turtle

# Raise the pen
turtle.penup()

# Initialize variables for the starting X and Y coordinates
# Change these to adjust the starting position of the turtle
x_start = -100
y_start = -50

# Send the turtle to its starting position.
turtle.goto(x_start, y_start)

# Lower the pen
turtle.pendown()

# Draw the pattern using a loop
for lines in range(8):

    # Move the turtle forward 200 pixels and rotate left 45 degrees
    turtle.forward(200)
    turtle.left(45)

# Hide the Turtle
turtle.hideturtle()

# Keep the turtle window open
turtle.done()
