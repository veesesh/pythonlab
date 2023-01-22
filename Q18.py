'''Question :
a. Write a function called draw_rectangle that takes a Canvas and a Rectangle as arguments and draws a representation of the Rectangle on the Canvas.
b. Add an attribute named color to your Rectangle objects and modify draw_rectangle so that it uses the color attribute as the fill color.
c. Write a function called draw_point that takes a Canvas and a Point as arguments and draws a representation of the Point on the Canvas.
d. Define a new class called Circle with appropriate attributes and instantiate a few Circle objects. Write a function called draw_circle that draws circles on the canvas.
'''

# import swampy pakage
from swampy.TurtleWorld import *


class Point(object):
    "represents a point in 2-D space"


p = Point()
p.x = 60
p.y = 15


class Rectangle(object):
    "Represents a rectangle"


box = Rectangle()
box.color = 'blue'
box.bbox = [[-100, -60], [100, 60]]


class Canvas(object):
    """Represents a canvas.
    attributes: width, height, background color"""


a_canvas = Canvas()
a_canvas.width = 500
a_canvas.height = 500


class Circle(object):
    """Represents a circle.
    attributes: center point, radius"""


c = Circle()
c.radius = 50
c.center = Point()
c.center.x = 20
c.center.y = 20


def draw_rectangle(canvas, rectangle):
    drawn_canvas = world.ca(canvas.width, canvas.height)
    drawn_canvas.rectangle(rectangle.bbox, fill=rectangle.color)


def draw_point(canvas, point):
    bbox = [[point.x, point.y], [point.x, point.y]]
    drawn_canvas = world.ca(canvas.width, canvas.height)
    drawn_canvas.rectangle(bbox, fill="black")


def draw_circle(canvas, circle):
    drawn_canvas = world.ca(canvas.width, canvas.height)
    drawn_canvas.circle([circle.center.x, circle.center.y], circle.radius)

# function for national flag of the Czech Republic


def draw_czech_republic_flag(canvas):
    drawn_canvas = world.ca(canvas.width, canvas.height)
    drawn_canvas.rectangle([[-100, 60], [100, 60]], outline=None, fill='white')
    drawn_canvas.rectangle([[-100, -60], [100, 0]], outline=None, fill='red2')
    points = [[-100, -60], [-100, 60], [0, 0]]
    drawn_canvas.polygon(points, fill='blue3')


# creates World object and calls the mainloop method
world = World()
draw_czech_republic_flag(a_canvas)
world.mainloop()
