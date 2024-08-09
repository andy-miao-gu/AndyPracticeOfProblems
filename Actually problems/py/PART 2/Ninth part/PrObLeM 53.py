#Suppose you're planning a trip to a country that uses a different temperature scale, and you need to convert temperatures between Fahrenheit and Celsius. You can use Python to create a simple temperature conversion tool.

#Here are the formulas for converting between Fahrenheit (F) and Celsius (C):

#To convert from Fahrenheit to Celsius: C = (F - 32) * 5/9                           To convert from Celsius to Fahrenheit: F = (C * 9/5) + 32 

C=input("degree cel")
C=int(C)
f=(C * 9/5) + 32
print(f"the celsius {C}° for fahrenheit{f}")




F=input("degree fah")
F=int(F)
c=(F - 32) * 5/9

print(f"the fahrenheit {F}° for celsius {c}")