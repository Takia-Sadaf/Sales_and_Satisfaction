import pandas as pd

df = pd.read_csv('C:\303project')  # replace with the actual file path
df.head()
df.info()
df.describe(include='all')
df['Satisfaction'].value_counts(normalize=True) * 100  # frequency and percentage
