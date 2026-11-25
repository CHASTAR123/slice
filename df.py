import pandas as pd
df =  pd.DataFrame({
    'Name':['Bob', 'Jhon', 'Jim', 'Cad'],
    'Age':[14, 10, 62, 53],
    'City':['London', 'Paris' ,'Rome', 'Delhi']
})
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df[['Name','Age']])

#Titanic
data = pd.read_csv('titanic.csv')
print(data.head())
print(data.shape)
print(data.info())
print(data.describe())
print(data.dtypes)
print(data[['Name','Age','Sex']])
print('filtering data')
above_30 = data[data['Age'] > 30]
print(above_30)
print(above_30.shape)
# combining multiple conditions together
p23 = data[data['Pclass'].isin([2, 3])]
print(p23[['Name', 'Pclass']].head())
print(p23[['Name', 'Pclass']].shape)

p23b = data[data['Pclass'] != 1]
print(p23b[['Name', 'Pclass']].shape)

p23c = data[(data['Pclass'] == 2) | (data['Pclass'] == 3)]
print(p23c[['Name', 'Pclass']].shape)
male_fc = data[(data['Sex'] == 'male') & (data['Pclass'] == 3)]
print(male_fc['Fare'].mean())

female_fc = data[(data['Sex'] == 'female') & (data['Pclass'] == 1)]
print(female_fc['Fare'].mean())
print(female_fc.shape)

adult_name = data.loc[data['Age'] > 18, 'Name']
print(adult_name)
# sliceing with 2d data
print(data.iloc[9:25, 3:7])
print(data.iloc[9:25:2 , 3:7:2])