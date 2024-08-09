homework ="""
1. From fifth part load a json file

its structure is like

{"user": {"name": "rating"},

"user2": {"name": "rating"},
}

your taks is to find all movies names in one ist
## all ratings in one list

### find unique movie names by converting movie names to set...

find the length of list of movies name and the length of set


"""
import json
with open('/Users/andygu/Desktop/preply_umair/Problem Solving/Actually problems/Sixth part/books_dataset.json', 'r') as file:
    data = json.load(file)
for each in data:
    new = data[ each]
    for e2 in new:
        print(e2,"<--movie     rating--->",new[e2])