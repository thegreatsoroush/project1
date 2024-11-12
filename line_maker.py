# برای مثلث منتظم از زاویه 120 استفاده میکنیم
from time import sleep
import turtle
line = turtle.Turtle()

def draw(numside,angle,colors,styles=None):
    for i in range(numside):
        line.color(colors[i])
        line.pensize(styles[i])
        line.forward(100)
        line.left(angle)
        

draw(3,120,["red","green","blue"],[1,3,5])
turtle.done()
