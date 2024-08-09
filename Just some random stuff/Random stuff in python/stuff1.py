import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colors=['purple','yellow','blue','red','orange','green','pink','white']
sides=2
for x in range(500):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/300)