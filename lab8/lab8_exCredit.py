import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#%matplotlib inline # For Jupyter Notebook only

#df = pd.read_csv('car_data.csv', header='infer', index_col=0)
df = pd.read_csv('car_data.csv', header='infer')
# Create a plot for City, Highway, and Combined KML values
#df.plot(kind='line', x='Model', y=['City MPG', 'Hwy MPG', 'Cmb MPG'], figsize=(12, 6))
df.plot(kind='line', x='Model', y='Cmb MPG', figsize=(12, 6))

# Add labels and title
plt.xlabel('Car Model')
plt.ylabel('Cmp MPG')
plt.title('MPG Comparison Across Models')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.show()
