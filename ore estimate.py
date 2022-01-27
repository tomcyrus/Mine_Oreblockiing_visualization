import pandas as pd


df = pd.read_csv (r'C:\Users\ECHELON\Desktop\final_data.csv')
x = df['Easting']
y = df['Northing']
z = df['Grade']
OR = df['Ore depth']
OB = df['Overburden']

length = float(input('enter length of a unit block: '))
width = float(input('enter width of a unit block: '))
bulk_density = float(input('enter the bulk density of the rock: '))

for ind, row in df.iterrows():
    df.loc[ind, 'Volume'] = length * width * row['Ore depth']
print(df['Volume'].sum())

for ind, row in df.iterrows():
    df.loc[ind, 'Tonnage'] = row['Volume'] * bulk_density

Total_tonnage = (df['Tonnage'].sum())
print('Total tonnage')
print(Total_tonnage)

for ind, row in df.iterrows():
    df.loc[ind, 'Metal Content'] = row['Grade'] * row['Ore depth']

Total_Metal_Content = (df['Metal Content'].sum())
print('Total Metal Content')
print(Total_Metal_Content)

Total_thickness = (df['Ore depth'].sum())
print('Total Thickness')
print(Total_thickness)

Average_Grade =Total_Metal_Content / Total_thickness
print('Average_Grade')
print(Average_Grade)
