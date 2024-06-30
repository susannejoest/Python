# https://www.kaggle.com/code/robikscube/introduction-to-exploratory-data-analysis
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('max_columns', 200)
df = pd.read_csv('../sample.csv')

# Number of columns and rows,  e.g. (10, 5)
df.shape 

# Get first 10 rows as a sample
df.head(10)

# Get columns
df.columns

# Get types (object, float64 etc.)
df.dtypes

# Describe (count, mean std etc.)
df.describe()

# drop rename columns, make copy of dataset
df = df[['column 1',
    # 'column2',
       'column3']].copy()

# df.drop(['column4'], axis=1)

# convert date
df['date1'] = pd.to_datetime(df['date1_clean'])

# Rename columns
df = df.rename(columns={'col1':'Column 1',
                   'col2':'Column_2'})

# Analyze Null Values (number of null values per column)
df.isna().sum()

# Look for duplicates
df.loc[df.duplicated()]

# Check for duplicate column
df.loc[df.duplicated(subset=['Col1'])].head(5)

# Checking an example duplicate
df.query('Coaster_Name == "Crystal Beach Cyclone"')

# get current columns
df.columns

df = df.loc[~df.duplicated(subset=['Coaster_Name','Location','Opening_Date'])] \
    .reset_index(drop=True).copy()

# Plotting Feature Distributions, Histogram, KDE, Boxplot

df['Year_Introduced'].value_counts()
  1999    46
  2000    45
  
  1956     1
  
  Name: Year_Introduced, Length: 101, dtype: int64

# Bar Chart Year
    ax = df['Year_Introduced'].value_counts() \
        .head(10) \
        .plot(kind='bar', title='Top 10 Years Coasters Introduced')
    ax.set_xlabel('Year Introduced')
    ax.set_ylabel('Count')

# Bar Chart Speed
  ax = df['Speed_mph'].plot(kind='hist',
                            bins=20,
                            title='Coaster Speed (mph)')
  ax.set_xlabel('Speed (mph)')

# Scatter Plot height vs speed
  df.plot(kind='scatter',
          x='Speed_mph',
          y='Height_ft',
          title='Coaster Speed vs. Height')
  plt.show()

# Pairplot

  sns.pairplot(df,
               vars=['Year_Introduced','Speed_mph',
                     'Height_ft','Inversions','Gforce'],
              hue='Type_Main')
  plt.show()


