####its about string

#### make a function to count strings which are complete
### () is 2
#### ()( is 2
### ()() is 4
### ()()( is also 4 because end one is not complete brackets
def countstringbrackets(x):
    counter = 0
    start = 0
    counter2 = 0
    start2 = 0
    counter3 = 0
    start3 = 0
    counter4 = 0
    start4 = 0
    for each in x:
        if "(" == each:
            start = start +1
        if ")" == each and start != 0:
            counter = counter + 2
            start = start - 1
        if "[" == each:
            start2 = start2 +1
        if "]" == each and start2 != 0:
            counter2 = counter2 + 2
            start2 = start2 - 1
        if "{" == each:
            start3 = start3 +1
        if "}" == each and start3 != 0:
            counter3 = counter3 + 2
            start3 = start3 - 1 
        if "|" == each:
            start4 = start4 +1
        if "7" == each and start4 != 0:
            counter4 = counter4 + 2
            start4 = start4 - 1 
    return (counter,counter2,counter3,counter4)
print(countstringbrackets(input(" put () not in one ()\n")))
