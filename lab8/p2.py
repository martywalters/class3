import matplotlib
#matplotlib.use('Agg')  # Use the Agg backend for environments without a display

import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('car_data.csv', header='infer', index_col=0)

# Basic scatter plot
df.plot(kind='scatter', x='Displ', y='City MPG', color='r')
plt.xlabel('Displacement')
plt.ylabel('City MPG')
plt.title('Displacement vs. City MPG')
#plt.savefig('basic_scatter_plot.png')  # Save the plot to a file
plt.show()  # This will not display the plot in a headless environment, but will save the file

# Create color and size lists
c = ['r' if fuel == 'Gasoline' else 'g' for fuel in df['Fuel']]
s = df['Greenhouse Gas Score'] * 8

# Enhanced scatter plot
plt.scatter(df['Displ'], df['City MPG'], c=c, s=s, alpha=0.5)
plt.xlabel('Displacement')
plt.ylabel('City MPG')
plt.title('Displacement vs. City MPG with Fuel Type and Greenhouse Gas Score')
plt.legend(['Gasoline', 'Diesel'], loc='upper right')
#plt.savefig('enhanced_scatter_plot.png')  # Save the plot to a file
plt.show()  # This will not display the plot in a headless environment, but will save the file

# Extra Credit: Plotting city, highway, and combined MPG values using separate colors
df.plot(x='Displ', y=['Cmb MPG'], kind='line')
plt.xlabel('Displacement')
plt.ylabel('MPG')
plt.title('City, Highway, and Combined MPG vs. Displacement')
plt.legend(['City MPG', 'Highway MPG', 'Combined MPG'])
#plt.savefig('mpg_vs_displacement.png')  # Save the plot to a file
plt.show()  # This will not display the plot in a headless environment, but will save the file

