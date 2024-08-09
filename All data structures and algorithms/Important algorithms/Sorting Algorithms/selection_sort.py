
# Search on youtube without using chatgpt .. make 
# andy selection sort working algorithm

# write for loop if x[i] < current_min update current minimum with i
def andysSortMethod(x:list):
    for andy in range(len(x)):
        current_min = andy
        for i in range(andy,len(x)):
            if x[i] < x[current_min]:
                current_min = i
        #
        t = x[andy]
        q = x[current_min]
        x[andy] = q
        x[current_min] = t

        print(x)
#
x = [9,432,423,423,423,423,4235,4,3,6,9,2]
andysSortMethod(x)
#