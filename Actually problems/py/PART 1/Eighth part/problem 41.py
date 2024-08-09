## define a function which will tell 
## largest and smallest numberr from a SET


def largest_and_smallest(y):
    largest = max(y)
    smallest = min(y)
    return largest, smallest





x = {3123,123,23,2432,43,3,23,2,32,3,23,4,2,5,112,2,5}
a,b = largest_and_smallest(x)

print(a,b)