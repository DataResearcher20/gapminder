import pandas as pd

# Define chunk size
chunksize = 10000

# Initialize an empty DataFrame with 'country' and 'year' columns
merged_df = pd.DataFrame(columns=['country', 'year'])

# Iterate over chunks of df_population_tidy and merge with other DataFrames
for chunk in pd.read_csv('population.csv', chunksize=chunksize):
    df_population_filled = chunk.fillna(method='ffill')
    df_population_tidy = pd.melt(df_population_filled, id_vars='country', var_name='year', value_name='population')
    merged_df = pd.merge(merged_df, df_population_tidy, on=['country', 'year'], how='outer')

# Merge df_life_expectancy_tidy
for chunk in pd.read_csv('life_expectancy.csv', chunksize=chunksize):
    df_life_expectancy_filled = chunk.fillna(method='ffill')
    df_life_expectancy_tidy = pd.melt(df_life_expectancy_filled, id_vars='country', var_name='year', value_name='life_expectancy_tidy')
    merged_df = pd.merge(merged_df, df_life_expectancy_tidy, on=['country', 'year'], how='outer')

# Merge df_gni_per_capita_tidy
for chunk in pd.read_csv('gni_per_capita.csv', chunksize=chunksize):
    df_gni_per_capita_filled = chunk.fillna(method='ffill')
    df_gni_per_capita_tidy = pd.melt(df_gni_per_capita_filled, id_vars='country', var_name='year', value_name='gni_per_capita_tidy')
    merged_df = pd.merge(merged_df, df_gni_per_capita_tidy, on=['country', 'year'], how='outer')

# Save merged_df as CSV
merged_df.to_csv('merged_data.csv', index=False)
