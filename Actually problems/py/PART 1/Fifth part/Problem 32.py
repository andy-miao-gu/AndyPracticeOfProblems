import random
import pandas as pd
# Generate random data
students = ['John', 'Emma', 'Michael', 'Sophia', 'Daniel', 'Olivia', 'James', 'Emily', 'Benjamin', 'Isabella', 'Jacob', 'Mia', 'William', 'Ava', 'Alexander']
student_data = {}

# Populate the dictionary with random toy counts
for student in students[:15]:
    toy_count = random.randint(0, 20)
    student_data[student] = toy_count

# Display the dictionary
print(student_data)
for each in student_data:
    if student_data[each] > 15:
        print(each)