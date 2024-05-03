import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('newData.csv')

# Filter the dataset for depressed individuals and remove rows with 'Missing' values
df_depressed = df[(df['Depression'] == 'Depressed') & (df['Marital Status'] != 'Missing') & (df['Gender'] != 'Missing')]

# Group by marital status and gender, and count the frequency of each combination
grouped_data = df_depressed.groupby(['Marital Status', 'Gender']).size().unstack()

# Plot the stacked bar chart
plt.figure(figsize=(10, 6))
grouped_data.plot(kind='bar', stacked=True)
plt.title('Marital Status vs. Gender for Depressed Individuals')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.legend(title='Gender')
plt.show()
