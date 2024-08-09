import turtle
import math

screen = turtle.Screen()
screen.title('Heart Animation - PythonTurtle.Academy')
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
turtle.speed(0)
turtle.hideturtle()

screen.tracer(0, 0)
turtle.color('red')

def draw_heart(alpha, d):
    turtle.color('red')
    r = d / math.tan(math.radians(180 - alpha / 2))
    turtle.up()
    turtle.goto(0, -d * math.cos(math.radians(45)))
    turtle.seth(90 - (alpha - 180))
    turtle.down()
    turtle.begin_fill()
    turtle.fd(d)
    turtle.circle(r, alpha)
    turtle.left(180)
    turtle.circle(r, alpha)
    turtle.fd(d)
    turtle.end_fill()
    turtle.left(152)
    turtle.forward(650)
    turtle.color('blue')
    turtle.write("我爱妈妈", font=("Playfair Display", 30, "normal"))
    
turtle.color('red')
a = 220
sign = -1
size = 1000  # Initial heart size
size_change = 10  # Amount by which the size changes

def animate():
    global a, sign, size
    turtle.clear()
    draw_heart(a, size)
    screen.update()
    a += sign
    if a < 215:
        sign = 1  # Reverse the size change direction
    elif a > 220:
        sign = -1  # Change the size of the heart
    screen.ontimer(animate, 50)

animate()

# Add the following line to keep the window open
turtle.mainloop()
