"""
1. A Robot moves in a Plane starting from the origin point (0,0). The robot can move
toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given
following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after directions are steps. Write a program to compute the
distance current position after sequence of movements.
Hint: Use math module.
"""

from math import sqrt

"""set the x and y value for robot position"""
x, y = 0, 0

while True:
    rbs = input("type in 'UP 00' and press enter then type 'DOWN 00' press enter repeat for LEFT and RIGHT:")

    if rbs == "":
        print("\n")
        break

    else:
        steps = rbs.split()
        thi = steps[0]
        dist = int(steps[1])

        if thi == 'UP':
            y = y + dist
        elif thi == 'DOWN':
            y = y - dist
        elif thi == 'RIGHT':
            x = x + dist
        elif thi == 'LEFT':
            x = x - dist

print("x, y position of robot is:", x, y, "\n")

location = sqrt(x ** 2 + y ** 2)
print("Distance of robot from initial position is:", location)
