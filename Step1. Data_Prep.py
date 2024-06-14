#Data Preparation

#Import Pandas library
import pandas as pd

#Load the dataset
df = pd.read_csv('/Users/paritagala/Desktop/Website/1. Customer Churn Analysis and Visualization/Customer_Churn.csv')

# Check for missing values
print(df.isnull().sum())

# Handle missing values (e.g., fill with mean or drop)
df.fillna(df.mean(), inplace=True)