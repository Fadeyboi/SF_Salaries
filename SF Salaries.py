# Import pandas as pd.
import pandas as pd
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
