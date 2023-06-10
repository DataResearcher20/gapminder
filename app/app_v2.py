import streamlit as st
import pandas as pd

# Load the data
@st.cache
def load_data():
    df_life_expectancy = pd.read_csv('life_expectancy.csv')
    df_population = pd.read_csv('population.csv')
    df_gni_per_capita = pd.read_csv('gni_per_capita.csv')
    return df_life_expectancy, df_population, df_gni_per_capita

df_life_expectancy, df_population, df_gni_per_capita = load_data()

# Merge the dataframes
df_merged = pd.merge(df_life_expectancy, df_population, on=['country', 'year'], how='inner')
df_merged = pd.merge(df_merged, df_gni_per_capita, on=['country', 'year'], how='inner')

# Tidy data format
df_tidy = pd.melt(df_merged, id_vars=['country', 'year'], value_vars=['life_expectancy', 'population', 'gni_per_capita'])
df_tidy = df_tidy.rename(columns={'variable': 'KPI', 'value': 'value'})

# Convert year to datetime
df_tidy['year'] = pd.to_datetime(df_tidy['year'], format='%Y')

# Filter data based on selected year and countries
year = st.slider('Select a year', min_value=1800, max_value=2100, value=2021, step=1)
countries = st.multiselect('Select countries', df_tidy['country'].unique())

df_filtered = df_tidy[df_tidy['year'].dt.year == year]
if countries:
    df_filtered = df_filtered[df_filtered['country'].isin(countries)]

# Plot bubble chart
st.title('KPI Bubble Chart')
st.markdown('Life Expectancy vs GNI per Capita (PPP)')

st.plotly_chart(
    df_filtered.iplot(asFigure=True, kind='scatter', mode='markers',
                      x='gni_per_capita', y='life_expectancy', size='population',
                      text='country', categories='country', colors='country',
                      xlog=True, title='KPI Bubble Chart')
)
