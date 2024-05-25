import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#%matplotlib inline # For Jupyter Notebook only

df = pd.read_csv('all_alpha_19.csv', header='infer')

# Display the first few rows to ensure it loaded correctly
print(df.head())

df_filtered = df[(df['Stnd'] == 'T3B125') & (df['Fuel'].isin(['Gasoline', 'Diesel']))]

# Display the first few rows to ensure filtering worked
print(df_filtered.head())

# List of columns to keep
cols = ['Model', 'Displ', 'Fuel', 'City MPG', 'Hwy MPG', 'Cmb MPG', 'Greenhouse Gas Score']

df_filtered = df_filtered[cols].reset_index(drop=True)

df_new = df_filtered[cols]

print(df_new.head())

# Convert the MPG columns to float
df_new[['City MPG', 'Hwy MPG', 'Cmb MPG']] = df_new[['City MPG', 'Hwy MPG', 'Cmb MPG']].astype(float)

# Display the first few rows to ensure the conversion is correct
print(df_new.head())




# Conversion function
def mpg_to_kml(mpg):
    return mpg * 0.42514


# Add the KML columns
df_new = df_new.assign(
    CityKML=lambda x: mpg_to_kml(x['City MPG']),
    HwyKML=lambda x: mpg_to_kml(x['Hwy MPG']),
    CmbKML=lambda x: mpg_to_kml(x['Cmb MPG'])
)

# Display the first few rows to ensure the new columns are added correctly
print(df_new.head())

# Save the DataFrame to a CSV file
df_new.to_csv('car_data.csv', index=False)
