import pandas as pd

df = pd.read_csv('weather_data.csv')

print(list(df['temp']))

# series object has methods
print(df['temp'].max())

# conditional selection
print(df[df['day'] == 'Monday'])