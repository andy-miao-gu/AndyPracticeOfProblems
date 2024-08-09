### homework = 
"""
Sure! Here's a challenging question in Python for you:

Question:
Given a list of integers, write a Python function to find the longest subarray where the sum of its elements is equal to zero. The function should return the starting and ending indices of this subarray. If there are multiple subarrays with the same maximum length, return the one that appears first.

For example, given the list: [-2, -1, 1, 2, -3, 4, -1, 2, 1, -5, 4], the function should return (2, 5) since the subarray [1, 2, -3, 4] has a sum of zero and is the longest subarray with this property."""
x = [-2, -1, 1, 2, -3, 4, -1, 2, 1, -5, 4]
def function(xy):
    for i in range(len(xy)-1):
        print("the sum of",xy[i:i+4],"is",sum(xy[i:i+3]))
function(x)