# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles
import turtle


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius

    def __repr__(self):
        return f"The circle has a radius of {self.radius} and a diameter of {self.diameter}"

    def __add__(self, circle):
        new_radius = self.radius + circle.radius
        return Circle(new_radius)

    def __gt__(self, circle):
        if self.radius > circle.radius:
            return True
        else:
            return False

    def __eq__(self, circle):
        if self.radius == circle.radius:
            return True
        else:
            return False

    def circle_list(self, *args):
        self.circles = []
        for item in args:
            self.circles.append(item)
        for i in range(0, len(self.circles)):
            for j in range(0, len(self.circles) - i - 1):
                if self.circles[j].radius > self.circles[j + 1].radius:
                    temp = self.circles[j]
                    self.circles[j] = self.circles[j + 1]
                    self.circles[j + 1] = temp
        for i in self.circles:
            turtle.circle(i.radius)
        return self.circles


circle1 = Circle(3)
circle2 = Circle(5)
circle3 = circle1 + circle2
# print(circle3)
# print(circle1 == circle2)
circle1.circle_list(circle2, circle3, Circle(4), Circle(6))
print(circle1.circles)
