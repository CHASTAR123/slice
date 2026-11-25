import pandas as pd
data = pd.read_csv('titanic.csv')
print(data.info())
above_60 = data[data['Age'] > 60]
print(len(above_60))

children = data[(data['Age'] <  12) & (data['Survived'] == 1)]
print(len(children))


females = data[(data['Sex'] == 'female') & (data['Pclass'] == 1)]
print(len(females))

males = data[(data['Sex'] == 'male') & (data['Pclass'] == 3) & (data['Survived'] ==1)]
print(len(males))

females = data[(data['Sex'] == "female") & (data["Pclass"] == 1) & (data['Age'] > 50)]
print(females)