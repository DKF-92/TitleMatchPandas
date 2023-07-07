#Checks for keyword in Title(string) and returns csv with true or false

#Imports libraries/dependencies
import pandas as pd

# uses pandas to read csv into dataframe
df = pd.read_csv('TitleMatchPandas\SummaryTitles.csv', header=0, dtype=str)
df['Site Name'] = df['Site Name'].str.lower()

#User inputs keyword
keyword = ['letham']

#loops through df to find keyword
for test in keyword:
    df[test] = df.astype(str).sum(axis=1).str.contains(test)


#Prints df (uncomment), and creates csv with true or false column
print(df)
print(df.dtypes)
df.to_csv('TitleMatchPandas\Test.csv')