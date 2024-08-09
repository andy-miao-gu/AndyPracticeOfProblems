task="""
when i write a number N then you have to tell 
all possible 2**n to the N number
for example
if N = 2000
then you have to tell all possible 2**0 ,,, 2**1 until you reach N
"""
N = 2000
ind = 0
blu = 2**ind
while(blu < N):
    blu = 2**ind
    print(2**ind)
    ind += 1
ind = ind-2
print("final answer is",2**ind)
