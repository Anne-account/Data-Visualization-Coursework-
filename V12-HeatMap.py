# Heat Map
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def heatmapChart():
        
    # Read data from the CSV file
    df = pd.read_csv("newData.csv")

    # Information box
    info_text = "Other chronic conditions include - 'Asthma', 'Overweight', 'Arthritis', 'Liver Condition', 'Thyroid Problem', 'Cancer', etc."

    # Read data from the CSV file
    df = pd.read_csv("newData.csv")

    # Filter out rows where 'Depression' is 'Depressed'
    filtered_data = df[df['Depression'] == 'Depressed']
    # Group by Depression status and age group, count occurrences of each condition
    counts_age_group = filtered_data.groupby(['Depression', 'Age group']).agg({'Cardiovascular Disease': 'value_counts',
                                                                            'Other Chronic Conditions': 'value_counts'})
    # Unstack the multi-level index for plotting
    counts_age_group_unstacked = counts_age_group.unstack(level=-1).fillna(0)

    # Plot heatmap
    plt.figure(figsize=(10, 6))
    plt.title('Count of Individuals with Cardiovascular Disease and Other Chronic Conditions by Age Group and Depression Status')
    sns.heatmap(counts_age_group_unstacked, annot=True, fmt='g', cmap='Blues')
    plt.xticks(rotation=45)  # Rotate x-axis labels by 45 degrees
    plt.xlabel('Health Issues group')  # Set x-axis title

    # Add information box below X-axis label
    plt.text(0.5, -0.45, info_text, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

    plt.show()

heatmapChart()