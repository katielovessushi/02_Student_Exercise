"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the first vertex, number of sides, side length, color,
        line width, angle, and an internal turtle.Turtle object.
        Reject sides < 3, side_length <= 0, and pen_size <= 0.
        """
        # TODO: initialize your object's state and its own turtle.Turtle()
        if side_length <= 0 or sides < 3 or pen_size <= 0:
            raise ValueError("size must be positive")
        self._x = x
        self._y = y
        self._size = pen_size
        self._color = color
        self._length = side_length
        self._sides = sides
        self._angle = angle
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._pen.speed(0)

    def draw(self):
        """Draw a regular polygon using left(360 / sides)."""
        # TODO: lift pen; go to starting vertex; set heading/color/pensize;
        #       lower pen; draw sides; lift pen.
    def draw(self):
        self._pen.pensize(self._size)
        self._pen.penup()
        self._pen.goto(self._x, self._y)
        self._pen.setheading(self._angle)          # tilt the whole polygon
        self._pen.pencolor(self._color)
        self._pen.pendown()
        for _ in range(self._sides):
            self._pen.forward(self._length)
            self._pen.left(360 // self._sides)      # turn the right amount
        self._pen.penup()

    def move_to(self, x, y):
        """Update the starting vertex; clear only this polygon; redraw."""
        # TODO: update this object's position, then clear and redraw.
        self._x = x
        self._y = y
        self._pen.clear()
        self.draw()
