### you have to fin the power.... if device has 10 volts and current is 1.5 amp 
#Power = Volt * ElectricCurrent ### what is this??? 

"""
volratge in japan is 100.... how much power if
juicer = 20amp *10
motor = 500amp*2
light = 10amp*5
fan = 15amp*2
"""

def fu(volt,eltri):
    power=volt*eltri
    print(power,"powaaaaa")
    return power
list_ofhome_watt = []
list_ofhome_watt.append( fu(100,0.2) * 10)
list_ofhome_watt.append( fu(100,0.15) * 2)
list_ofhome_watt.append( fu(100,0.1) * 5)
list_ofhome_watt.append( fu(100,0.4) * 2)
print("total home electrcial bill" ,sum(list_ofhome_watt) * 20,"PKR" )


### 1000 watt then 5 usd bill