import turtle

def recursive_pattern(t, depth, length, angle):
    if depth == 0:
        return
    else:
        # Forward
        t.forward(length)

        # Right
        t.right(angle)
        recursive_pattern(t, depth - 1, length * 0.6, angle)  # Reduce length for smaller segments

        # Left
        t.left(2 * angle)
        recursive_pattern(t, depth - 1, length * 0.6, angle)  # Reduce length for smaller segments

        # Right
        t.right(angle)
        recursive_pattern(t, depth - 1, length * 0.6, angle)  # Reduce length for smaller segments

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
    angle = 70  # Adjust the angle for interesting patterns

    recursive_pattern(t, depth, length, angle)

    window.exitonclick()


main()