import turtle
import flower
import fractal
import initials

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    my_flower = flower.create("blue")
    flower.draw(my_flower)

    my_fractal = fractal.create("green")
    fractal.draw(my_fractal)

    my_initials = initials.create("red")
    initials.draw(my_initials)
    
    window.exitonclick()

draw_art()

