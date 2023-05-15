import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Gapminder')
st.write("Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication")

# Load the merged data
file_path = 'merged_data.csv'
df_merged = pd.read_csv(file_path)

@st.cache
def preprocess_data(df):
    # Apply data preprocessing steps here
    # For example, forward fill missing values
    df_filled = df.fillna(method='ffill')
    return df_filled

# Data preprocessing
df_tidy = preprocess_data(df_merged)

# Filter the data based on the selected year
year = st.slider('Select a year', min_value=1990, max_value=2020, value=2020, step=1)
df_filtered = df_tidy[['country', str(year), 'life_expectancy', 'population', 'gni_per_capita']]

# Select one or more countries
selected_countries = st.multiselect('Select countries', df_filtered['country'].unique())

# Filter the data based on the selected countries
df_filtered = df_filtered[df_filtered['country'].isin(selected_countries)]

# Bubble chart
chart_data = df_filtered.rename(columns={str(year): 'GNI per capita'})
chart_data['log_GNI_per_capita'] = chart_data['GNI per capita'].apply(lambda x: np.log10(x))

st.write('Bubble chart')
st.write(chart_data)

# Plot the bubble chart
fig = px.scatter(chart_data, x='log_GNI_per_capita', y='life_expectancy', size='population', color='country')
fig.update_layout(
    xaxis_title='Logarithmic GNI per capita',
    yaxis_title='Life Expectancy',
    showlegend=False
)
st.plotly_chart(fig)







