a = "abcd"
# output-> aaaabbbbccccdddd

"""a = a*132
a = sorted(a)
print("".join(a))"""




# if you have length = 10 and witdth = 20, then find area of rectangular, 
length = int(input("length\n"))
width = int(input("width\n"))
if length != width:
    print("The area of the rectangle is",length*width)
else:
    print("The area of the square is",length*width)
# find area triangle 
# if you have angle 60, a = 90 , b = 30 ...and find hypothenuse
a = int(90)
b = int(30)
c = int((a**2 + b**2)**(1/2))
print(c)
print("the area of the right triangle is",a*b/2)
### new if you have radius then find the area of circle, find for radius 2,5,10,
rad=int(3.5)
print("the radius is",(rad**2) * 3.1415829)
### i sent you gui coode ,... which has perimeter your task is to replace permitor to find hypothenus