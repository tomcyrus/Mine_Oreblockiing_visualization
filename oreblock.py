import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#getting ore block data from file
df = pd.read_csv ('oreblock01.csv')
x = df['Easting']
y = df['Northing']
z = df['Grade']
#sns.set_style('whitegrid')
sns.axes_style('darkgrid')
#input value of cut off grade
plt.figure(figsize=(50,50))

n=float(input('enter cut off grade: '))
plt.style.use('seaborn')
#data visualisation
#plt.colorbar()
sns.scatterplot(x,y,df['Grade']>=n, marker = "s", edgecolor= 'black', s=1000, palette = 'cool' )

plt.legend(labels=["Grade","Cut off Grade"], title='oreblock',loc='lower right')
# plt.legend(loc='lower right')
plt.show()