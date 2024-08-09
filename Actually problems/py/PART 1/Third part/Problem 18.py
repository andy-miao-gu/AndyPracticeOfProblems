"""load studetn file again and show me student who have less 
than 50 marks and plot them in other scores"""
import pandas
import seaborn
import matplotlib.pyplot as plt
v=pandas.read_csv("../../DATA/StudentsPerformance.csv")
l50ind = v['math score']<50
l50 = v[l50ind]
seaborn.scatterplot(x="math score",data =l50)
plt.show()