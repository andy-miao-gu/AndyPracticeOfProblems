"""1. Ask the user to enter the number of students in the class.
2. Create an empty list to store the grades.
3. Use a loop to iterate over the number of students entered by the user.
4. Within the loop, ask the user to enter the grade for each student and append it to the list.
5. Calculate the average grade by summing all the grades and dividing by the total number of students.
6. Print the average grade."""
x=int(input("Enter the number of students \n"))
p=[]
for each in range(x):
    y = int(input(f"tell me the grades of student {each}"+"\n"))
    p.append(y)
if x == """
""":
    x=input("no enters without a number")
avg = float(sum(p)/x)
print(avg)