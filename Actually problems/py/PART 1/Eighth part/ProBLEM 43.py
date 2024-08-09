"""
1. how to make a dictionary of fruits and color to
Tuple of fruits and colors
for exmple 
{"k1":10,"k2":66}
((k1,10),(k2,66)) and then find the tuple with maximum number and min number



"""
tup=[]
dictionary={"apple":"red", "orange":"orange","banana":"yellow", "i_don't_know_fruit":"I_don't_know_the_color_of_this"}
for dictu in dictionary:
    tup.append((dictu,dictionary[dictu]))
print(tuple(tup))


   