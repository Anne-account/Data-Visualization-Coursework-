import pandas as pd
import matplotlib.pyplot as plt

# Read data from the CSV file
data = pd.read_csv("newData.csv")

# Filter data for depressed individuals
depressed_data = data[data['Depression'] == 'Depressed']

# Count the occurrences of each race among depressed individuals
race_counts = depressed_data['Race'].value_counts()

# Create pie chart
plt.figure(figsize=(8, 8))

# Plotting the pie chart
plt.pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Race Among Depressed Individuals', y=1.05)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

