import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('newData.csv')

# Assuming 'Depression' column contains categorical data
# Count the frequency of each category
depression_counts = df['Depression'].value_counts()

# Custom autopct function to adjust the position of percentage labels
def custom_autopct(pct):
    return '{:.1f}%\n'.format(pct)

# Plotting the donut chart with custom autopct function
plt.figure(figsize=(8, 8))
plt.pie(depression_counts, labels=depression_counts.index, autopct=custom_autopct, startangle=90, wedgeprops=dict(width=0.4))
plt.title('Distribution of Depression Status')

plt.show()
