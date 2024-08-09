fruit_weights = {
    'apple': 150,
    'banana': 120,
    'orange': 250,
    'strawberry': 15,
    'mango': 300,
    'pineapple': 500,
    'grape': 5,
    'watermelon': 2000,
    'kiwi': 75,
    'pear': 180
}
hiiiiii=[]
hiiii2 = []
eaaaaaa = []
for each_fruit in fruit_weights:
    hiiiiii.append(fruit_weights[each_fruit])
    hiiii2.append(each_fruit)
maxind = hiiiiii.index(max(hiiiiii))
miniss = hiiiiii.index(min(hiiiiii))
print(f"The max of of the list is {max(hiiiiii)} and the fruit is {hiiii2[maxind]} the min of the list is {min(hiiiiii)} and the fruit is {hiiii2[miniss]}")
