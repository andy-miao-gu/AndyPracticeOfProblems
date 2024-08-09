"""Question: Write a Python program to find the average of a list o_f numbers.
Example:y
Input: [5, 10, 15, 20]
Output: Average = 12.5"""
lst=[1,1,1,1,1,1,1]
x=0
y = 0
for each in range(len(lst)):
    x+=1
    y = y + lst[each]
avg = y/x
print(avg)