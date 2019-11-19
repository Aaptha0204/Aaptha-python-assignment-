print('done by Aaptha.B.V from K section')
print('my SRN is PES2201900234')
import pandas as pd

df=pd.read_excel('empl.xlsx')

print('solution for 1st problem is assignment.')
print(df.iloc[0:5])
print(df.iloc[44:50])

print('solution for 2nd problem is assignment.')
print(df[df.Year_of_Joining >= 2000])

print('solution for 3rd problem is assignment.')
print(df[df.Salary >= 100000]) 

print('solution for 4th problem is assignment.')
print(df[df.Region == 'Mideast']) 

print('solution for 5th problem is assignment.')
print(df[['First Name','E mail','Date of Joining','Salary']])

print('solution for 6th problem is assignment.')
print(df.sort_values(by = 'Salary'))

print('solution for 7th problem is assignment.')
print(df.sort_values(by = 'Age in Yrs'))

print('solution for 8th problem is assignment.')
print(df[df.Gender == 'M'])
print(df[df.Gender == 'F'])
