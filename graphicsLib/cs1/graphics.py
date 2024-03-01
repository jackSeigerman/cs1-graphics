import turtle
import atexit

h = 0


def open_canvas(width, height):
    turtle.Screen().setup(width=width, height=height)
    h = height


def set_background_color_rgb(r, g, b):
    turtle.bgcolor((int(r / 255), int(g / 255), int(b / 255)))


def set_color_rgb(r, g, b):
    turtle.colormode(255)
    turtle.color((r, g, b))


def set_color(color):
    turtle.color(color)


def set_background_color(color):
    turtle.bgcolor(color)


def set_line_thickness(thickness):
    turtle.width(thickness)


def draw_filled_circle(centerx, centery, radius):
    turtle.penup()
    turtle.setpos(centerx, h - (centery - radius))
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_filled_rect(x, y, width, height):
    turtle.penup()
    turtle.setpos(x, h - y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()


def draw_filled_polygon(x1, y1, x2, y2, x3, y3, x4, y4):
    turtle.penup()
    turtle.setpos(x1, h - y1)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x2, h - y2)
    turtle.goto(x3, h - y3)
    turtle.goto(x4, h - y4)
    turtle.goto(x1, h - y1)
    turtle.end_fill()


def draw_oval(x, y, width, height):
    turtle.penup()
    turtle.setpos(x, h - (y - height))
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(45)
    for _ in range(2):
        turtle.circle(width / 2, 90)
        turtle.circle(height / 2, 90)
    turtle.end_fill()


def draw_rect(x, y, width, height):
    turtle.penup()
    turtle.setpos(x, h - y)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)


def draw_filled_oval(x, y, width, height):
    turtle.penup()
    turtle.setpos(x, h - (y - height))
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(45)
    for _ in range(2):
        turtle.circle(width / 2, 90)
        turtle.circle(height / 2, 90)
    turtle.end_fill()


def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.setpos(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


def draw_circle(centerx, centery, radius):
    turtle.penup()
    turtle.setpos(centerx, centery - radius)
    turtle.pendown()
    turtle.circle(radius)


def close():
    turtle.Screen().exitonclick()


atexit.register(close)
