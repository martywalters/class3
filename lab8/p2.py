import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('car_data.csv', header='infer', index_col=0)

# Display the first few rows to ensure it loaded correctly
print(df.head())

# Create the scatter plot
df.plot(kind='scatter', x='Displ', y='CityKML', color='r')

# Show the plot
plt.show()

# Create the 'c' list for colors based on the fuel type
c = df['Fuel'].apply(lambda x: 'r' if x == 'Gasoline' else 'g')

# Display the first few elements to verify
print(c.head())

# Create the 's' list for sizes based on the Greenhouse Gas Score
s = df['Greenhouse Gas Score'] * 8

# Display the first few elements to verify
print(s.head())

# Create the enhanced scatter plot
plt.scatter(df['Displ'], df['CityKML'], c=c, s=s, alpha=0.5)

# Add labels and title
plt.xlabel('Engine Displacement (L)')
plt.ylabel('City KML')
plt.title('City KML vs. Engine Displacement')

# Show the plot
plt.show()
