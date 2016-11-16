import turtle

def draw(some_turtle, size):
    for _ in range(1, 21):
        some_turtle.forward(size)
        some_turtle.left(162)
    some_turtle.forward(size / 2)
    some_turtle.right(90)
    some_turtle.forward(size)
    
