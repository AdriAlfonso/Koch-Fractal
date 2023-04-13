import turtle

def koch_recursive(t, depth, length):
    """
    Recursive function for painting the Koch fractal.
    :param t: The turtle used for drawing the scene.
    :param depth: The complexity of the Koch curve (more depth, more detail).
    :param length: The length the turtle is traveling between koch curves.
    :return: No return.
    """
    if depth == 0:
        # If the depth reaches 0, then the turtle moves forward.
        t.forward(length)
    else:
        # If the depth != 0, then we call recursively the Koch function for drawing each curve.
        for angle in [60, -120, 60, 0]:
            koch_recursive(t, depth - 1, length / 3)
            t.left(angle)

def main():
    """
    Now we configure our Koch enviroment using turtle.
    """
    # Screen
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Koch's Fractal")

    # Turtle
    koch = turtle.Turtle()
    koch.color("red")
    koch.speed(0)
    koch.hideturtle()

    # Draw the Koch fractal
    koch.penup()
    koch.goto(-100, 50)
    koch.pendown()

    # 3 are the minimum lines we need to draw Koch's fractal. Change the depth to see more detail.
    for _ in range(3):
        koch_recursive(koch, 2, 250)
        koch.right(120)

    """
    In this animation you will be able to watch the difference between different depths in the Koch's curve.
    koch_recursive(koch, 1, 250)
    koch.right(120)
    koch_recursive(koch, 2, 250)
    koch.right(120)
    koch_recursive(koch, 3, 250)
    koch.right(120)
    """
    wn.exitonclick()

if __name__ == '__main__':
    main()
