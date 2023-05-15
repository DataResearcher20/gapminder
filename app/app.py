import pandas as pd
import streamlit as st
import numpy as np


st.title('Gapminder')
st.write("Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication")




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

values = df_tidy
'''st.line_chart(values)-->bubble chart The bubble chart should show the following KPIs:

On the x-axis: the logarithmic Gross Natition Income (GNI) per captia (inflation-adjusted and converted to $ based on purchasing power parity (PPP)). The maximal x value should be constant independent what you select, so that you can more easily compare the charts.
On the y-axis: Life expectancy
Size of the bubble: population
Color: Country
# st.slider () to control the year
# multiselect widget for selecting one or more countries
'''

