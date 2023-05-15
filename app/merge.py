import pandas as pd

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

# Display the merged DataFrame
print(merged_df.head())
