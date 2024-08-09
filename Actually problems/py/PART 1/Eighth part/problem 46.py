"""Problem: 😭💔

Find the second minimum and second maximum from list 😢"""
Clue_list=[]
x = [21,33,23,3123,32,3,23,233,23]
clue = -1000000
for each in x:
    if clue <each:
        clue = each
        Clue_list.append(each)
print("max is",clue)
print(Clue_list)