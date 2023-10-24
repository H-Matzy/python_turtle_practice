import turtle
from random import randint, random
def recursive_pattern(t, depth, length, angle):
    if depth == 0 :
        return
    else:
        colorValue1 = random()
        colorValue2 = random()
        colorValue3 = random()

        # Gamer Turtle
        # Forward
        t.pendown()
        t.color(colorValue1,colorValue2,colorValue3)
        t.forward(length/3)

        t.penup()
        t.forward(length/3)

        t.pendown()
        t.color(colorValue2,colorValue3,colorValue1)
        t.forward(length/3)
        t.penup()
        # Right
        t.right(angle)
        recursive_pattern(t, depth - 1, length,  angle)

        # Left
        t.left(2* angle)
        recursive_pattern(t, depth - 1, length,  angle)


        # Right
        t.right(angle)
        recursive_pattern(t, depth - 1, length,  angle)


        # Backward
        t.backward(length)

def draw_shapes(t,length, nShapes):

    for shape in range(0, nShapes):

        for turn in range(0, shape + 3):
            r = random()
            g = random()
            b = random()
            t.color(r, g, b)
            t.forward(length)
            t.right(360/ (shape + 3))
def main():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Set the drawing speed to the fastest

    # Set the initial position and angle
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.setheading(90)  # Start facing up

    depth = 8  # Adjust the depth as needed
    length = 200  # Adjust the length of each step as needed
    right_angle = randint(1,90)
    left_angle = randint(1,90)
    random_angle = randint(1,180)
    draw_shapes(t, length, 5)
    window.exitonclick()


main()