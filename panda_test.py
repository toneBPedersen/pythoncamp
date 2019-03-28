import pandas as pd

df = pd.read_csv('final_PINK.csv')

print(df.head())
print(df.tail())
print(df.columns)

sum_snacks_country = df.groupby(['country_id','traffic_source_level_1'])['SEK_IN_SNACKS'].sum()

print(sum_snacks_country.head())

#set the first element to string to make an error in the data
df['SEK_IN_FOOD'] = df['SEK_IN_FOOD'].astype(str)
[df['SEK_IN_FOOD'][i].replace('.',',') for i in range(len(df['SEK_IN_FOOD']))]

#Reset to float type again
[df['SEK_IN_FOOD'][i].replace(',','.') for i in range(len(df['SEK_IN_FOOD']))]
df['SEK_IN_FOOD'] = df['SEK_IN_FOOD'].astype(float)

print(df.loc['DE'])


