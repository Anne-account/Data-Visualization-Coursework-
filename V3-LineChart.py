import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def linechart():
    # Read data from the CSV file
    df = pd.read_csv("newData.csv")

    # A function to remove outliers using the IQR method
    def remove_outliers(data):
        Q1 = np.percentile(data, 25)
        Q3 = np.percentile(data, 75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return data[(data >= lower_bound) & (data <= upper_bound)]

    # Filtering out rows where 'Depression' column is equal to 'Depressed'
    depressed_data = df[df['Depression'] == 'Depressed'].copy()  # Make a copy to avoid modifying the original DataFrame
    
    # Remove outliers from the 'Sleep Hours' column
    depressed_data.loc[:, 'Sleep Hours'] = remove_outliers(depressed_data['Sleep Hours'])  # Use .loc to modify DataFrame in place
    
    # Calculate the mean sleep hours for each age group
    average_sleep_hours = depressed_data.groupby('Age')['Sleep Hours'].mean()
    
    # Calculate the mean sleep hours for each age group in the whole dataset
    average_sleep_hours_normal = df.groupby('Age')['Sleep Hours'].mean()
    
    # Plotting the line chart
    plt.figure(figsize=(12, 10))  # Adjust figure size
    
    # Plot average sleep hours trend over age for depressed individuals
    plt.subplot(2, 1, 1)  # 2 rows, 1 column, subplot 1
    average_sleep_hours.plot(kind='line', marker='o', color='g', linestyle='-')
    plt.title('Average Sleep Hours Over Age for Depressed Individuals')
    plt.xlabel('Age')
    plt.ylabel('Average Sleep Hours')
    plt.grid(True)
    
    # Plot distribution of sleep hours for all individuals
    plt.subplot(2, 1, 2)  # 2 rows, 1 column, subplot 2
    average_sleep_hours_normal.plot(kind='line', marker='o', color='g', linestyle='-')
    plt.title('Distribution of average Sleep Hours for all people')
    plt.xlabel('Age')
    plt.ylabel('Avg Sleep Hours')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

linechart()