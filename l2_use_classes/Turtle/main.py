import turtle

def draw_flover(some_turtle, size):
    for _ in range(1, 21):
        some_turtle.forward(size)
        some_turtle.left(162)
    some_turtle.forward(size / 2)
    some_turtle.right(90)
    some_turtle.forward(size)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    
    #Create and draw flover
    flover = turtle.Turtle()
    flover.shape("turtle")
    flover.color("blue")
    flover.speed(2)
    flover.penup()
    flover.goto(-300, 0)
    flover.pendown()
    draw_flover(flover, 200)
    
    window.exitonclick()
'''
    #Create and draw fractal
    my_fractal = turtle.Turtle()
    my_fractal.shape("turtle")
    my_fractal.color("green")
    my_fractal.speed(3)
    fractal.draw(my_fractal)

    #Create and draw initials
    my_initials = turtle.Turtle()
    my_initials.shape("turtle")
    my_initials.color("green")
    my_initials.speed(4)
    initials.draw(my_initials)
'''
    

draw_art()

