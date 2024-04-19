# Import pandas as pd.
import pandas as pd
import re
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)

# Read Salaries.csv as a dataframe called sal.
df = pd.read_csv('Salaries.csv')
print("Check the head of the DataFrame\n", df.head())
# Use the .info() method to find out how many entries there are.
print("\n\nUse the .info() method to find out how many entries there are.")
print(df.info())
# What is the average BasePay ?
print("What is the average BasePay?")
print(df['BasePay'].mean())
# What is the highest amount of OvertimePay in the dataset ?
print("What is the highest amount of OvertimePay in the dataset?")
print(df['OvertimePay'].max())
# What is the job title of JOSEPH DRISCOLL ? Note: Use all caps,
# otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll).
print("What is the job title of JOSEPH DRISCOLL?")
print(df.loc[df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
# How much does JOSEPH DRISCOLL make (including benefits)?
print("How much does JOSEPH DRISCOLL make (including benefits)?")
print(df.loc[df['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
# What is the name of highest paid person (including benefits)?
print("What is the name of highest paid person (including benefits)?")
print(df.loc[df['TotalPayBenefits'].max() == df['TotalPayBenefits']])
# What is the name of lowest paid person (including benefits)?
print("What is the name of lowest paid person (including benefits)?")
print(df.loc[df['TotalPayBenefits'].min() == df['TotalPayBenefits']])
# What was the average (mean) BasePay of all employees per year? (2011-2014) ?
print("What was the average (mean) BasePay of all employees per year? (2011-2014)?")
for i in range(2011, 2015):
    print(df.loc[df['Year'] == i]['BasePay'].mean())
# How many unique job titles are there?
print("How many unique job titles are there?")
print(df['JobTitle'].nunique())
# What are the top 5 most common jobs?
print("What are the top 5 most common jobs?")
print(df['JobTitle'].value_counts().head())
# How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurrence in 2013?)
print("How many Job Titles were represented by only one "
      "person in 2013? (e.g. Job Titles with only one occurrence in 2013?)")
print(sum(df[df['Year'] == 2013]['JobTitle'].value_counts() == 1))
# How many people have the word Chief in their job title?
print("How many people have the word Chief in their job title?")
jobs = df["JobTitle"].tolist()
print(len(list(filter(lambda x: 'CHIEF' in x.upper(), jobs))))
# Is there a correlation between length of the Job Title string and Salary?
print("Is there a correlation between length of the Job Title string and Salary?")

