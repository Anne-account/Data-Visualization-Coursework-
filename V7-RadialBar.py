import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def radialbarChart():

    # Read data from the CSV file
    df = pd.read_csv("newData.csv")

    # Grouping individuals by age ranges (e.g., 20-30, 31-40, etc.)
    age_bins = [20, 30, 40, 50, 60, 70, 80, 90]  # Define age bins
    age_labels = ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89']  # Labels for age bins
    df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

    # Calculating the prevalence of depression within each age group
    depression_counts = df.groupby('Age_Group')['Depression'].apply(lambda x: (x == 'Depressed').mean())

    # Plotting the radial bar chart
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 6))

    # Define colors for each age group
    colors = plt.cm.viridis(np.linspace(0, 1, len(depression_counts)))

    # Plot each age group as a radial bar
    theta = np.linspace(0, 2*np.pi, len(depression_counts), endpoint=False)
    width = 2*np.pi / len(depression_counts)
    bars = ax.bar(theta, depression_counts, width=width, color=colors, alpha=0.7)

    # Adding labels for each age group
    ax.set_xticks(theta)
    ax.set_xticklabels(depression_counts.index)

    # Adding title
    plt.title('Radial Bar Chart: Prevalence of Depression by Age Group')

    # Displaying the plot
    plt.show()

radialbarChart()