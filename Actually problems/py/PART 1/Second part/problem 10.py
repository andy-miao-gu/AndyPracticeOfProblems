"""Question: Write a Python program to find the maximum of three numbers.
Example:
Input: num1 = 10, num2 = 7, num3 = 14
Output: Maximum = 14"""
num=input("enter all numbers with spaces")
num=num.split(" ")
num2 = []
for i in num:
    num2.append(float(i))
maxi=max((num2))
sumi=sum((num2))
mini=min((num2))
avei=sum(num2)/len(num2)
print("maximum =",maxi)
print("sum all =",sumi)
print("minimum =",mini)
print("average =",avei)

