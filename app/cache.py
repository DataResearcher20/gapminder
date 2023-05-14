import streamlit as st
import pandas as pd

@st.cache
def load_data(file_path):
    # Load the merged CSV data into a DataFrame
    df = pd.read_csv(file_path)
    return df

@st.cache
def preprocess_data(df):
    # Apply data preprocessing steps here
    # For example, forward fill missing values
    
    # Forward fill missing values
    df_filled = df.fillna(method='ffill')
    
    # Transform the DataFrame into tidy format
    df_tidy = df_filled[['country', 'year', 'life_expectancy', 'population', 'gni_per_capita']]
    
    return df_tidy

# Data loading and preprocessing
file_path = 'merged_data.csv'
df_merged = load_data(file_path)
df_tidy = preprocess_data(df_merged)

# Display the processed DataFrame
st.write(df_tidy)
