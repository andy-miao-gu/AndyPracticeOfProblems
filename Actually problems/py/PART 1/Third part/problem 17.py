"""i am going to send you a csv file and 
you have to return me that csv file in which 
i will have only those students whos marks 
in maths are more than 95"""
import pandas
v=pandas.read_csv("../../DATA/StudentsPerformance.csv")
indx = v['math score']>95
ms95abve = v[indx]
ms95abve.to_csv("output.csv")
