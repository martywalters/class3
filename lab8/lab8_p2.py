import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#%matplotlib inline # For Jupyter Notebook only

df = pd.read_csv('car_data.csv', header='infer', index_col=0)
print(df.head())

df.plot(kind='scatter', x='Displ', y='City MPG', color='r')

plt.show()
plt.close()
c = df['Fuel'].apply(lambda x: 'r' if x == 'Gasoline' else 'g')

print(c.head())

s = df['Greenhouse Gas Score'] * 8

print(s.head())
plt.scatter(df['Displ'], df['City MPG'], c=c, s=s, alpha=0.5)

plt.xlabel('Engine Displacement (L)')
plt.ylabel('City MPG')
plt.title('City MPG vs. Engine Displacement')

plt.show()
plt.close()
df.plot(kind='line', x='Displ', y='Cmb MPG', figsize=(12, 6))

plt.xlabel('Engine Displacement (L)')
plt.ylabel('Cmp MPG')
plt.title('MPG Comparison Across Engine Displacement')

plt.xticks(rotation=90)

plt.show()




