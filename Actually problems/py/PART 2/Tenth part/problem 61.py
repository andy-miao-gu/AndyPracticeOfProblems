my_large_list = [1, 'apple', 2, 'orange', 3, 'banana', 4, 'grape', 5, 'kiwi',1, 'apple', 2, 'orange', 3, 'banana', 4, 'grape', 5, 'kiwi',6, 'melon', 7, 'cherry', 8, 'pear', 9, 'blueberry', 10, 'mango','cherry', 8, 'pear', 9, 'blueberry', 10, 'mango', 6, 'melon']
# if number is repeating more than 2 and if they are stirng how man letters it has
from collections import Counter
storage=Counter(my_large_list)
storage = dict(storage)
print(storage)
for a,b in storage.items():
    if b >= 2 and type(a) == str:
        print(a,b)
        print(Counter(a))