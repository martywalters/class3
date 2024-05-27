import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#%matplotlib inline # For Jupyter Notebook only

df = pd.read_csv('all_alpha_19.csv', header='infer')

print(df.head())

df_filter = df[(df['Stnd'] == 'T3B125') & (df['Fuel'].isin(['Gasoline', 'Diesel']))]

print(df_filter.head())

cols = ['Model', 'Displ', 'Fuel', 'City MPG', 'Hwy MPG', 'Cmb MPG', 'Greenhouse Gas Score']

df_filter = df_filter[cols].reset_index(drop=True)

df_new = df_filter[cols]

print(df_new.head())

df_new[['City MPG', 'Hwy MPG', 'Cmb MPG']] = df_new[['City MPG', 'Hwy MPG', 'Cmb MPG']].astype(float)

print(df_new.head())

def mpg_to_kml(mpg):
    return mpg * 0.42514

df_new = df_new.assign(
    CityKML=lambda x: mpg_to_kml(x['City MPG']),
    HwyKML=lambda x: mpg_to_kml(x['Hwy MPG']),
    CmbKML=lambda x: mpg_to_kml(x['Cmb MPG'])
)

print(df_new.head())

df_new.to_csv('car_data.csv', index=False)
