import pandas as pd
import matplotlib.pyplot as plt

# Read data from the CSV file
data = pd.read_csv("newData.csv")

# Remove rows where Marital Status is "missing"
data = data[data['Marital Status'] != 'Missing']

# Filter data for depressed individuals
depressed_data = data[data['Depression'] == 'Depressed']

# Count the occurrences of each marital status among depressed individuals
marital_counts = depressed_data['Marital Status'].value_counts()

# Create the bar chart
plt.figure(figsize=(8, 6))

# Plotting the bar chart
marital_counts.plot(kind="bar", color="skyblue")

plt.xlabel("Marital Status")
plt.ylabel("Count")
plt.title("Marital Status Distribution Among Depressed Individuals")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
