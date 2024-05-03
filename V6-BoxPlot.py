import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('newData.csv')

# Create a box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Depression', y='Household Income', data=df, palette='pastel')
plt.title('Box Plot of Household Income by Depression Status')
plt.xlabel('Depression Status')
plt.ylabel('Household Income ($)')
plt.show()
