def quickSort(array, start, end):
    if start < end:
        # Partition the array and get the pivot
        pivot = partition(array, start, end)

        # Recursively sort elements before and after the pivot
        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)

def partition(array, start, end):
    # Choose the rightmost element as the pivot
    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i = i + 1
            # Swap the elements
            array[i], array[j] = array[j], array[i]

    # Swap the pivot element with the element at (i+1), which is its correct position
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1

javaarray = [8, 2, 5, 3, 9, 4, 7, 6, 1]
print("Original Array:")
for i in javaarray:
    print(i, end=" ")

quickSort(javaarray, 0, len(javaarray) - 1)
print("\nSorted Array:")
for i in javaarray:
    print(i, end=" ")
