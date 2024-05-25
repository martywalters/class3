import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
# %matplotlib inline  # Uncomment this line if you are using Jupyter Notebook

# Load the dataset
df = pd.read_csv('all_alpha_19.csv', header='infer')

# Display the first few rows to ensure it loaded correctly
print(df.head())

# Filter the DataFrame for the required standard and fuel types
df_filtered = df[(df['Stnd'] == 'T3B125') & (df['Fuel'].isin(['Gasoline', 'Diesel']))]

# Display the first few rows to ensure filtering worked
print(df_filtered.head())

# List of columns to keep
cols = ['Model', 'Displ', 'Fuel', 'City MPG', 'Hwy MPG', 'Cmb MPG', 'Greenhouse Gas Score']

# Create new DataFrame with only the specified columns and reset index
df_filtered = df_filtered[cols].reset_index(drop=True)

# Display the first few rows to ensure the new DataFrame is correct
print(df_filtered.head())

# Convert the MPG columns to float
df_filtered[['City MPG', 'Hwy MPG', 'Cmb MPG']] = df_filtered[['City MPG', 'Hwy MPG', 'Cmb MPG']].astype(float)

# Display the first few rows to ensure the conversion is correct
print(df_filtered.head())

# Conversion function
def mpg_to_kml(mpg):
    return mpg * 0.42514

# Add the KML columns
df_filtered = df_filtered.assign(
    CityKML=lambda x: mpg_to_kml(x['City MPG']),
    HwyKML=lambda x: mpg_to_kml(x['Hwy MPG']),
    CmbKML=lambda x: mpg_to_kml(x['Cmb MPG'])
)

# Display the first few rows to ensure the new columns are added correctly
print(df_filtered.head())

# Save the DataFrame to a CSV file
df_filtered.to_csv('car_data.csv', index=False)


