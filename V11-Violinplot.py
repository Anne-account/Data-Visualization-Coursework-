import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def violinplotChart():
        
    # Read data from the CSV file
    data = pd.read_csv("newData.csv")

    # Remove rows where Marital Status is "missing"
    data = data[data['Marital Status'] != 'Missing']

    # Filter data for depressed individuals
    depressed_data = data[data['Depression'] == 'Depressed']

    # Plotting the violin plot
    plt.figure(figsize=(12, 8))
    sns.violinplot(
        data=depressed_data,
        x='Marital Status',  # Marital status on x-axis
        y='Age',  # Age on y-axis
        hue='Gender',  # Split by gender 
        split=True,  # Split violins by gender
        inner='quartile',  # Show quartiles inside the violins
        palette={'Male': '#ffb400', 'Female': '#9080ff'},  # Color palette for genders
    )
    plt.title('Age Distribution Among Depressed Individuals by Marital Status and Gender')
    plt.xlabel('Marital Status')
    plt.ylabel('Age')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Gender')
    plt.tight_layout()
    plt.show()

violinplotChart()
