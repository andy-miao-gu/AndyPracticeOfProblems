import numpy
import math
r = 1.25
L=5.5
h=r*2
Vf=L*(numpy.arccos((r-h)/r)*r**2-(r-h)*math.sqrt(2*r*h-h**2))
percent=0.2
numberfrompercent=Vf*percent
print(numberfrompercent)
# keep on decresign heigh h = h - 0.1
# if voulme becomes < numberfrompercent then stop and print 
# tenk is going to end soon
while(Vf>numberfrompercent):
    h-=0.1
    Vf=L*(numpy.arccos((r-h)/r)*r**2-(r-h)*math.sqrt(2*r*h-h**2))
print(f"The tank is gonna end soon prepare for refilling hight is now {h} volume is {Vf}")
