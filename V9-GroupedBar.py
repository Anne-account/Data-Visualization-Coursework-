import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def groupedbarChart():
        
    # Read data from the CSV file
    data = pd.read_csv("newData.csv")


    # Remove rows where Marital Status is "missing"
    data = data[data['Education Level'] != 'Missing']

    # Define the order of education levels for plotting
    education_order = ['Less Than 9th Grade', '9-11th Grade','High School', 'Some College or AA Degree','College Graduate or Above']

    # Filter data for depressed individuals
    depressed_data = data[data['Depression'] == 'Depressed']

    # Group the data by education level and gender to get the count of depressed individuals
    education_gender_counts = depressed_data.groupby(['Education Level', 'Gender']).size().reset_index(name='Depressed Count')


    # Plotting the bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=education_gender_counts,
        x='Education Level',  # Education level on x-axis
        y='Depressed Count',  # Depressed count on y-axis
        hue='Gender',  # Split by gender
        order=education_order,
        palette={'Male': '#ff5733', 'Female': '#33aaff'} 
    )
    plt.title('Depressed Count by Education Level and Gender')
    plt.xlabel('Education Level')
    plt.ylabel('Depressed Count')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Gender')
    plt.tight_layout()
    plt.show()

groupedbarChart()
