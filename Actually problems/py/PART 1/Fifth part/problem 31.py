import pandas as pd
import seaborn as seaside
import random
import matplotlib.pyplot as plt
# Generate random data
survey_data = {
    'Age': [random.randint(5, 15) for _ in range(20)],
    'Toys': [random.randint(0, 30) for _ in range(20)]
}

# Create the dataframe
df = pd.DataFrame(survey_data)

# Display the dataframe
print(df)
for each in survey_data['Age']:
    if each > 10:
        print(each)

print(df[df['Age']>10])
seaside.scatterplot(x='Age',y='Toys',data=df)
plt.show()