import turtle

def draw_flover(some_turtle, size):
    for _ in range(1, 21):
        some_turtle.forward(size)
        some_turtle.left(162)
    some_turtle.forward(size / 2)
    some_turtle.right(90)
    some_turtle.forward(size)

def draw_fractal(some_turtle, size, color):
    def __draw_triangle(some_turtle, size):
        for _ in range(1, 4):
            some_turtle.forward(size)
            some_turtle.left(120)

    some_turtle.begin_fill()
    some_turtle.fillcolor(color)

    for _ in range(1, 9):
        __draw_triangle(some_turtle, size / 8)
        some_turtle.forward(size / 8)

    some_turtle.left(120)
    some_turtle.forward(size / 8)

    some_turtle.tilt(120)
    for _ in range(1, 8):
        __draw_triangle(some_turtle, size / 8)
        some_turtle.forward(size / 8)

    some_turtle.left(120)
    some_turtle.forward(size / 8)

    for _ in range(1, 7):
        __draw_triangle(some_turtle, size / 8)
        some_turtle.forward(size / 8)
    '''
    some_turtle.left(120)
    some_turtle.forward(size / 8)

    some_turtle.left(120) 
    some_turtle.forward(size / 8)

    some_turtle.right(120) 
    some_turtle.forward(size / 4)

    some_turtle.left(120) 
    some_turtle.forward(size / 8)

    some_turtle.left(120) 
    some_turtle.forward(size / 8)
    '''
    some_turtle.end_fill()
    

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    
    #Create and draw flover
    flover = turtle.Turtle()
    flover.shape("turtle")
    flover.color("blue")
    flover.penup()
    flover.goto(-300, 0)
    flover.pendown()
    #draw_flover(flover, 200)
    
    #Create and draw fractal
    fractal = turtle.Turtle()
    fractal.shape("turtle")
    fractal.color("green")
    fractal.penup()
    fractal.goto(-100, -50)
    fractal.pendown()
    draw_fractal(fractal, 200, "green")

    window.exitonclick()
'''
    #Create and draw initials
    my_initials = turtle.Turtle()
    my_initials.shape("turtle")
    my_initials.color("green")
    my_initials.speed(4)
    initials.draw(my_initials)
'''
    

draw_art()

