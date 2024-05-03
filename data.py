import pandas as pd

def dataPreprocess():
    # Read the raw data into a DataFrame
    raw_data = pd.read_csv('StreamlitData.csv', low_memory=False)

    # Select the required columns
    required_columns = ['Depression', 'Gender', 'Age', 'Race', 'Education Level', 'Marital Status', 'Pregnant', 'Birth Place', 
                        'Household Income', 'Work Type', 'Sleep Hours', 'Asthma', 'Arthritis', 'Liver Condition', 
                        'Thyroid Problem', 'Cancer', 'Heart Failure', 'Heart Disease', 'Angina', 'Heart Attack', 'Stroke', 
                        'Marijuana Use', 'Cocaine Use', 'Heroine Use']

    # Create a new DataFrame with only the selected columns
    df = raw_data[required_columns].copy()  # Explicitly create a copy of the DataFrame

    # Preprocess Household Income column
    def preprocess_income(income_str):
        if income_str == "$75K+":
            return 75000
        elif income_str == "Over $20K":
            return 20000
        elif income_str.startswith("Below"):
            return int(income_str.split("$")[1].split("K")[0]) * 1000
        else:
            return 0

    def categorize_age(age):
        if age >= 50:
            return 'Senior Users'
        elif age >= 36:
            return 'Middle Age'
        elif age >= 25:
            return 'Young Adults'
        else:
            return 'Teenagers'

    df['Age group'] = df['Age'].apply(categorize_age)

    # Remove rows with 'Missing' in Education Level
    df = df[df['Education Level'] != 'Missing']

    # Remove rows with 'Missing' in Marital Status
    df = df[df['Marital Status'] != 'Missing']

    # Apply preprocessing to Household Income column
    df['Household Income'] = df['Household Income'].apply(preprocess_income)

    # Create column 'Other Chronic Conditions' based on multiple conditions
    chronic_cols = ['Asthma', 'Arthritis', 'Liver Condition', 'Thyroid Problem', 'Cancer']
    df['Other Chronic Conditions'] = df[chronic_cols].apply(lambda x: 'Yes' if 'Yes' in x.values else 'No', axis=1)

    # Combine columns for Set 2: Heart Issues
    cardiovascular_cols = ['Heart Failure', 'Heart Disease', 'Angina', 'Heart Attack', 'Stroke']
    df['Cardiovascular Disease'] = df[cardiovascular_cols].apply(lambda x: 'Yes' if 'Yes' in x.values else 'No', axis=1)
    
    # Combine columns for Drug Usage using OR logic
    drug_cols = ['Marijuana Use', 'Cocaine Use', 'Heroine Use']
    df['Drug Usage'] = df[drug_cols].apply(lambda x: 'Yes' if 'Yes' in x.values else 'No', axis=1)

    # Drop the original columns used for combining
    df.drop(columns=cardiovascular_cols + chronic_cols + drug_cols, inplace=True)

    # Save the preprocessed data to a new CSV file
    df.to_csv("newData.csv", index=False)
    print("Preprocessed data saved to newData.csv")


dataPreprocess()