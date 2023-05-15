import streamlit as st
import pandas as pd

import numpy as np


st.title('Gapminder')
st.write("Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication")

x = st.slider('Slope', min_value=0.01, max_value=0.10, step=0.01)
y = st.slider('Noise', min_value=0.01, max_value=0.10, step=0.01)

st.write(f"x={x} y={y}")
values = np.cumprod(1 + np.random.normal(x, y, (100, 10)), axis=0)
st.line_chart(values)


#data

# Load the CSV files into DataFrames
df_population = pd.read_csv('population.csv')
df_life_expectancy = pd.read_csv('life_expectancy.csv')
df_gni_per_capita = pd.read_csv('gni_per_capita.csv')

# Forward fill missing values in each DataFrame
df_population_filled = df_population.fillna(method='ffill')
df_life_expectancy_filled = df_life_expectancy.fillna(method='ffill')
df_gni_per_capita_filled = df_gni_per_capita.fillna(method='ffill')


# Select relevant columns and rename them for each DataFrame
df_population_tidy = df_population_filled[['country', 'year', 'population']]
df_population_tidy = df_population_tidy.rename(columns={'population': 'population'})

df_life_expectancy_tidy = df_life_expectancy_filled[['country', 'year', 'life_expectancy']]
df_life_expectancy_tidy = df_life_expectancy_tidy.rename(columns={'life_expectancy': 'life_expectancy'})

df_gni_per_capita_tidy = df_gni_per_capita_filled[['country', 'year', 'gni_per_capita']]
df_gni_per_capita_tidy = df_gni_per_capita_tidy.rename(columns={'gni_per_capita': 'gni_per_capita'})

# Merge the three DataFrames based on 'country' and 'year'
merged_df = pd.merge(df_population_tidy, df_life_expectancy_tidy, on=['country', 'year'])
merged_df = pd.merge(merged_df, df_gni_per_capita_tidy, on=['country', 'year'])

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



#creating a line chart

#st.line_chart()'''
