
def insert_sort(array):
    for i in range(len(array)):
        
        temp = array[i]
        j = i-1
        while j>=0 and array[j]>temp:
            array[j+1] = array[j]
            j-=1
        array[j+1] = temp
    return array
javaarray=[9,1,8,2,7,3,6,5,4]
for i in javaarray:
    print(i, end = " ")
print()
print(insert_sort(javaarray))