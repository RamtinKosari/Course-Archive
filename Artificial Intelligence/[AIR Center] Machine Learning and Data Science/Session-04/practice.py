import numpy as np
import pandas as pd

# dictionary of lists
test1 = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [5, np.nan, np.nan],
    'C': [1, 2, 3]
})
print(test1)
print(test1.isnull())
print(test1.isna())
print(test1.isnull().sum())
print(test1.isnull().sum().sum())
print(test1.isnull().sum().count())
# remove rows which has nan values
print(test1.dropna())
print(test1.dropna(axis=1))
print(test1.dropna(thresh=2))
print(test1.dropna(axis=1, thresh=2))
# fill nan values
print(test1.fillna(value="Fill Value"))
print(test1['A'].fillna(value=test1['A'].mean()))
print(test1['B'].fillna(value=test1['B'].mean()))
print(test1['C'].fillna(value=test1['C'].mean()))
# manage it with implace
test2 = test1.copy()
test2['A'] = test1['A'].fillna(value=test1['A'].mean())
test2['B'] = test1['B'].fillna(value=test1['B'].mean())
test2['C'] = test1['C'].fillna(value=test1['C'].mean())
print(test1)
print(test2)
# in order to check if any missing data is available we can do .sum() or .any()
print(test1.isnull().any())
print(test1.isnull().sum())


# GroupBy
data = {
    'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    'Sales': [200, 120, 340, 124, 243, 350]
}
test3 = pd.DataFrame(data=data)
print(test3)
print(test3.groupby('Company'))
print(test3.groupby('Company').max())         # not only affects sam column, but also affects other columns because there are alphabets and can be sorted
print(test3.groupby('Company').min())
# print(test3.groupby('Company').mean())      # why does not work ?
# print(test3.groupby('Company').std())       # why does not work ?
print(test3.groupby('Company').sum())
print(test3.groupby('Company', sort=False).sum())
print('-------------------')
print(test3.groupby('Company').sum().loc['FB'])
print(test3.groupby('Company').count())
print(test3)
print('-------------------')
print(test3.groupby('Company').agg({
    'sum', 'count', 'max'
}))