import turtle
from random import randint, random


def recursive_pattern(t, length, depth=8):
    angle = randint(1, 180)
    rgb = (random(), random(), random())

    if depth == 0:
        return
    else:
        depth -= 1
        # Gamer Turtle
        # Forward
        t.pendown()
        t.color(rgb)
        t.forward(length / 3)

        t.penup()
        t.forward(length / 3)

        t.pendown()
        t.color(rgb)
        t.forward(length / 3)
        t.penup()
        # Right
        t.right(angle)
        recursive_pattern(t, length, depth - 1)

        # Left
        t.left(2 * angle)
        recursive_pattern(t, length, depth - 1)

        # Right
        t.right(angle)
        recursive_pattern(t, length, depth - 1)

        # Backward
        t.backward(length)


def draw_shapes(t, length):
    nShapes = 10
    for shape in range(0, nShapes):

        for turn in range(0, shape + 3):
            rgb = (random(), random(), random())

            t.color(rgb)
            t.forward(length)
            t.right(360 / (shape + 3))


def main(drawing_function):
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Set the drawing speed to the fastest

    # Set the initial position and angle
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(180)  # Start facing up

    length = 200  # Adjust the length of each step as needed

    drawing_function(t, length)
    window.exitonclick()


main(draw_shapes)
