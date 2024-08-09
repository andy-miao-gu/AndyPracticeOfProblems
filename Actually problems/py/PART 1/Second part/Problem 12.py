"""Question: Write a Python program to calculate the factorial of a number.
Example:
Input: num = 5
Output: Factorial = 120"""
def factorial(num):
    x=1
    for each in range(1,num+1):
        print(each,"*",x ,"= ",end="")
        x*=each
        print(x)
numy=int(input("num\n"))
factorial(numy)