import turtle
import flower
import fractal
import initials

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    
    #Create and draw flover
    my_flower = turtle.Turtle()
    my_flower.shape("turtle")
    my_flower.color("blue")
    my_flower.speed(2)
    my_flower.penup()
    my_flower.goto(-300, 0)
    my_flower.pendown()
    flower.draw(my_flower, 200)
    
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

