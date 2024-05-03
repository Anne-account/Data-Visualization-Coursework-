import pandas as pd
import matplotlib.pyplot as plt

def histogramChart():

    # Load the dataset
    data = pd.read_csv('newData.csv')

    # Grouping individuals by age ranges 
    age_bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  
    age_labels = [str(age) for age in age_bins[:-1]]  # Convert age bins to string labels
    data['Age_Group'] = pd.cut(data['Age'], bins=age_bins, labels=age_labels, right=False)

    # Filter data for depressed individuals
    depressed_data = data[data['Depression'] == 'Depressed']

    # Create the histogram
    plt.figure(figsize=(10, 6))

    # Plotting the histogram
    plt.hist(depressed_data['Age'], bins=age_bins, edgecolor='black')

    plt.xlabel("Age")
    plt.ylabel("Depressed Count")
    plt.title("Histogram of Age Distribution Among Depressed Individuals")

    # Set x-axis ticks to individual integers and show age ranges in between
    plt.xticks(ticks=age_bins[:-1], labels=age_labels, rotation='vertical')

    plt.tight_layout()
    plt.show()

histogramChart()
