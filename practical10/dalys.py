# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Verify working directory and files
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())
# Import the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
# Examine the dataframe
print("\nFirst 5 rows of the dataset:")
print(dalys_data.head(5))
# Get information about the dataframe
print("\nDataframe info:")
print(dalys_data.info())
# Get descriptive statistics
print("\nDescriptive statistics:")
print(dalys_data.describe())
# Access specific data points using iloc
print("\nValue in first row, fourth column:")
print(dalys_data.iloc[0, 3])
# Show third column (Year) for first 10 rows
print("\nYear for first 10 rows:")
print(dalys_data.iloc[0:10, 2])
print("10th year with DALYs data recorded in Afghanistan:", dalys_data.iloc[9, 2])
# Using Boolean to filter columns
my_columns = [True, True, False, True]
print("\nFirst 3 rows with selected columns:")
print(dalys_data.iloc[0:3, my_columns])
# Get DALYs for all countries in 1990
year_1990 = dalys_data['Year'] == 1990
dalys_1990 = dalys_data.loc[year_1990, 'DALYs']
print("\nDALYs for all countries in 1990:")
print(dalys_1990)
# Compare mean DALYs between UK and France
uk_data = dalys_data.loc[dalys_data['Entity'] == 'United Kingdom', 'DALYs']
france_data = dalys_data.loc[dalys_data['Entity'] == 'France', 'DALYs']
uk_mean = np.mean(uk_data)
france_mean = np.mean(france_data)
print("\nMean DALYs comparison:")
print(f"UK mean DALYs: {uk_mean}")
print(f"France mean DALYs: {france_mean}")
print("The mean DALYs in the UK was", "greater" if uk_mean > france_mean else "smaller", "than in France.")
# Plot DALYs over time for the UK
uk = dalys_data.loc[dalys_data['Entity'] == 'United Kingdom', ['DALYs', 'Year']]
plt.figure(figsize=(10, 6))
plt.plot(uk['Year'], uk['DALYs'], 'b+')
plt.xticks(uk['Year'], rotation=-90)
plt.title('DALYs Over Time in the United Kingdom')
plt.xlabel('Year')
plt.ylabel('DALYs Rate')
plt.grid(True)
plt.tight_layout()
plt.show()
# Example question: How has the DALYs changed in China over time?
china = dalys_data.loc[dalys_data['Entity'] == 'China', ['DALYs', 'Year']]
plt.figure(figsize=(10, 6))
plt.plot(china['Year'], china['DALYs'], 'r-')
plt.xticks(china['Year'], rotation=-90)
plt.title('DALYs Over Time in China')
plt.xlabel('Year')
plt.ylabel('DALYs Rate')
plt.grid(True)
plt.tight_layout()
plt.show()
# Create a boxplot of DALYs across countries in 1990
dalys_1990_all = dalys_data.loc[dalys_data['Year'] == 1990, ['Entity', 'DALYs']]
plt.figure(figsize=(12, 6))
plt.boxplot(dalys_1990_all['DALYs'])
plt.title('Distribution of DALYs Across Countries in 1990')
plt.ylabel('DALYs Rate')
plt.xticks([1], ['All Countries'])
plt.grid(True)
plt.tight_layout()
plt.show()