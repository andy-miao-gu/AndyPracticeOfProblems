import json
with open('/Users/andygu/Desktop/preply_umair/Problem Solving/Actually problems/Fifth part/books_dataset.json', 'r') as file:
    data = json.load(file)

for each in data:
    print(each,data[each])
    for e2 in data[each]:
        print("{"+e2,[data[each][e2]]+"}")