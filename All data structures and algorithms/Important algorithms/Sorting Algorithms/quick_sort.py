
def quickSort(array,start,end):
    for i in range(start,end):
        if end <= start:
            return array
        pivot=partition(array,start,end)
        quickSort(array,start,pivot-1)
        quickSort(array,pivot+1,end)

    return array
def partition(array,start,end):
    pivot=array[end]
    i=start-1
    for j in range(start,end-1):
        if array[j]<pivot:
            i = i + 1
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
            
    i+=1

    temp=array[i]
    array[i]=array[end]
    array[end]=temp
    return i
javaarray=[8,2,5,3,9,4,7,6,1]
for i in javaarray:
    print(i, end = " ")
print()
print(quickSort(javaarray,0,len(javaarray)-1))
#quickSort(javaarray,0,len(javaarray)-1)