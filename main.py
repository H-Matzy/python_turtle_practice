import turtle
from random import randint, random
def recursive_pattern(t, depth, length, angle):
    if depth == 0 :
        return
    else:
        r = random()
        g = random()
        b = random()

        # Gamer Turtle
        t.color(r,g,b)
        # Forward
        t.pendown()
        t.forward(length/3)
        t.penup()
        t.forward(length/3)
        t.pendown()
        t.forward(length/3)
        t.penup()
        # Right
        t.right(angle)
        recursive_pattern(t, depth - 1, length * 0.6,  angle)

        # Left
        t.left(2* angle)
        recursive_pattern(t, depth - 1, length * 0.6,  angle)


        # Right
        t.right(angle)
        recursive_pattern(t, depth - 1, length * 0.6,  angle)


        # Backward
        t.backward(length)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Set the drawing speed to the fastest

    # Set the initial position and angle
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.setheading(90)  # Start facing up

    depth = 8  # Adjust the depth as needed
    length = 300  # Adjust the length of each step as needed
    right_angle = randint(1,90)
    left_angle = randint(1,90)
    random_angle = randint(1,180)
    recursive_pattern(t, depth, length, random_angle)

    window.exitonclick()


main()