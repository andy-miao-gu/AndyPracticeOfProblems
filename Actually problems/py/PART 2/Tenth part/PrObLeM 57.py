task="""
when i write a number for exmple 15
you have to arrange your list like this
0 15 1 14 2 13 3 12 .....
until the end 15 0
"""
lst=[]
def defy(num):
    cn = num
    for eahc in range(0,num+1):
        lst.append((eahc,cn))
        cn -= 1
    return lst
print(defy(15))