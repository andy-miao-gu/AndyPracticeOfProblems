### run a for loop over 1 to length

x = [5,1,5,2,1,4,5,6,7,20,9,8,2,21,21,21,2,12,1,12,2,12,21,12,12,21,1,12,12,12,21,12,21]
def bubble_sort(xi):
    for each in range(100):
        for i in range(1, len(xi)):
            if xi[i] < xi[i-1]:
                q = xi[i-1]
                p = xi[i]
                xi[i] = q
                xi[i-1] = p
                print(xi)
bubble_sort(x)
## if x[i] < x[-1]:
# switch
