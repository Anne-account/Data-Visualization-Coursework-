import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def horizontalbarChart():

    # Read data from the CSV file
    data = pd.read_csv("newData.csv")

    # Filter data for depressed individuals and remove missing education levels
    depressed_data = data[(data['Depression'] == 'Depressed') & (data['Education Level'] != 'Missing')]

    # Count the number of depressed individuals by education level
    depressed_count_by_education = depressed_data['Education Level'].value_counts().reset_index()

    # Rename the columns for clarity
    depressed_count_by_education.columns = ['Education Level', 'Count']

    # Define the order of education levels for plotting
    education_order = ['College Graduate or Above','Less Than 9th Grade', '9-11th Grade','High School', 'Some College or AA Degree']

    # Plotting the horizontal bar chart using Seaborn
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Count', y='Education Level', data=depressed_count_by_education, order=education_order, palette='Set2')
    plt.title('Count of Depressed Individuals by Education Level')
    plt.xlabel('Depressed Count')
    plt.ylabel('Education Level')

    # Set the limits of the x-axis to be up to 1000
    plt.xlim(0, 1000)
    plt.grid(True)
    plt.tight_layout()

    plt.show()

horizontalbarChart()
