## you can not use max 
## you can not use min function
x = [321,3,4,4,3,233,2,342,324,23,767,5,25,33,53,54,343]
# use a for loop
## it will test all numbers
## make a threshold
## if any number is bigger than your number then updte your number
## else ignore that number
clue = x[0]
for each in x:
    if clue <each:
        clue = each
print("max is",clue) 
clue2 = x[0]
for each in x:
    if clue > each:
        clue = each
print("min is",clue) 
