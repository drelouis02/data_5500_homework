#create a data frame named temperatures containing temperature readings for three people
import pandas as pd


# Activity 1 
# Create a DataFrame with three people's temperature readings
temperatures = pd.DataFrame({
    'Andre': [97.8, 98.4, 98.1],
    'James': [98.2, 98.6, 98.3],
    'Sarah': [97.9, 98.5, 98.0]
}, index=['Morning', 'Afternoon', 'Evening'])

# Print the completed DataFrame
print(temperatures)


#Activity 2
# Select and print Morning temperatures for all three people
print(temperatures.loc['Morning'])

# Select and print Morning and Afternoon temperatures for Andre and James
print(temperatures.loc[['Morning', 'Afternoon'], ['Andre', 'James']])


#Activity 3
# Display descriptive statistics for the temperatures DataFrame
print(temperatures.describe())

# Sort the columns in alphabetical order
sorted_temperatures = temperatures.sort_index(axis=1)

# Print the sorted DataFrame
print(sorted_temperatures)
