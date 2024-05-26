import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for environments without a display

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('car_data.csv', header='infer', index_col=0)

# Basic scatter plot
df.plot(kind='scatter', x='Displ', y='City MPG', color='r')
plt.xlabel('Displacement')
plt.ylabel('City MPG')
plt.title('Displacement vs. City MPG')
plt.savefig('part2_f1.png')  # Save the plot to a file
plt.close()  # Close the plot to free up resources

# Create color and size lists
c = ['r' if fuel == 'Gasoline' else 'g' for fuel in df['Fuel']]
s = df['Greenhouse Gas Score'] * 8

# Enhanced scatter plot
plt.scatter(df['Displ'], df['City MPG'], c=c, s=s, alpha=0.5)
plt.xlabel('Displacement')
plt.ylabel('City MPG')
plt.title('Displacement vs. City MPG with Fuel Type and Greenhouse Gas Score')
# Custom legend
handles = [plt.Line2D([0], [0], marker='o', color='w', label='Gasoline', markersize=10, markerfacecolor='r'),
           plt.Line2D([0], [0], marker='o', color='w', label='Diesel', markersize=10, markerfacecolor='g')]
plt.legend(handles=handles, loc='upper right')
plt.savefig('part2_f2.png')  # Save the plot to a file
plt.close()  # Close the plot to free up resources

# Extra Credit: Plotting city, highway, and combined MPG values using separate colors
df.plot(x='Displ', y=['City MPG', 'Hwy MPG', 'Cmb MPG'], kind='line')
plt.xlabel('Displacement')
plt.ylabel('MPG')
plt.title('City, Highway, and Combined MPG vs. Displacement')
plt.legend(['City MPG', 'Highway MPG', 'Combined MPG'])
plt.savefig('part2_f3.png')  # Save the plot to a file
plt.close()  # Close the plot to free up resources
