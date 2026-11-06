import turtle

t = turtle.Turtle()
t.speed(3)

# Function to draw a triangle
def draw_triangle():
    for i in range(3):
        t.forward(100)
        t.left(120)

# Function to draw a rectangle
def draw_rectangle():
    for i in range(2):
        t.forward(150)
        t.left(90)
        t.forward(80)
        t.left(90)

# Function to draw a polygon
def draw_polygon():
    sides = 6
    for i in range(sides):
        t.forward(70)
        t.left(360 / sides)

# Function to draw a circle
def draw_circle():
    t.circle(50)

# Function to draw a square
def draw_square():
    for i in range(4):
        t.forward(100)
        t.left(90)

# Draw all shapes
draw_triangle()

t.penup()
t.goto(150, 0)
t.pendown()
draw_rectangle()

t.penup()
t.goto(-200, -150)
t.pendown()
draw_polygon()

t.penup()
t.goto(100, -150)
t.pendown()
draw_circle()

t.penup()
t.goto(300, -150)
t.pendown()
draw_square()

turtle.done()
