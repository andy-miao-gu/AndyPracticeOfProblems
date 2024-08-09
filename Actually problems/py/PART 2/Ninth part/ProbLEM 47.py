"""Home work:  
Find third largest and third smallest number."""

def find_third_smallest_and_biggest(lst):
    smallest = float('inf')
    second_smallest = float('inf')
    third_smallest = float('inf')
    biggest = float('-inf')
    second_biggest = float('-inf')
    third_biggest = float('-inf')

    for num in lst:
        if num < smallest:
            third_smallest = second_smallest
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            third_smallest = second_smallest
            second_smallest = num
        elif num < third_smallest and num != smallest and num != second_smallest:
            third_smallest = num
        
        if num > biggest:
            third_biggest = second_biggest
            second_biggest = biggest
            biggest = num
        elif num > second_biggest and num != biggest:
            third_biggest = second_biggest
            second_biggest = num
        elif num > third_biggest and num != biggest and num != second_biggest:
            third_biggest = num

    return third_smallest, third_biggest

# Example usage:
my_list = [1,412,34,5,12,56,5,56,35,6,3,7,7,3,7,65,4,7,23,7,]
third_smallest, third_biggest = find_third_smallest_and_biggest(my_list)

print("Third smallest:", third_smallest)
print("Third biggest:", third_biggest)
