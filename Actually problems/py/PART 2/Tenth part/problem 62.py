import turtle
blap=input("how much rectangles shold i go")
blap=int(blap)
def spin_around(slap):
    for each in range(slap):
        for each in range(3):
            turtle.forward(2*slap)
            turtle.right(90)
            slap-=5
        #turtle.forward(slap-)
spin_around(blap)