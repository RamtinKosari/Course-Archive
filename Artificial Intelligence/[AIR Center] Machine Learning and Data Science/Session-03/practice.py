import numpy as np
import pandas as pd

# - Series
my_list = [10, 20, 30, 44]
my_lables = ["sirius", "vega", "proxima centauri", "arcturus"]
my_dict = {
    "aa": 11,
    "bb": 22,
    "cc": 33,
    "dd": 44
}

test1 = pd.Series(my_list)
print(test1)
print(test1[3])

test2 = pd.Series(my_list, my_lables)
print(test2)
print(test2[1])
print(test2["vega"])

test3 = pd.Series(my_dict, my_lables)
# NaN because pandas find for labels in dictionary and it might not be available
print(test3)
# so we do not need to assign labels, pandas can use dictionary lables :
test3 = pd.Series(my_dict)
print(test3)

# we can even use objects
test4 = pd.Series([sum, print])
print(test4)

# seed is amazing, same seed, same random number output
# from numpy.random import randn
# np.random.seed(101)
# print(np.random.randn())
# print(np.random.randn())
# print(np.random.randn())
# print(np.random.randn())


# numpy 1D : Vector
# numpy 2D : Matrix
# pandas 1D : Series
# pandas 2D : Data Frame

# Data Frames
from numpy.random import randn
np.random.seed(101)
test5 = pd.DataFrame(
    randn(5, 4),
    index = ["A", "B", "C", "D", "E"],
    columns = ["W", "X", "Y", "Z"]
)
print(test5)
# selection and indexing
print(test5["W"])
print(test5[["W", "X"]])
# print(test5["A"]) # error, not available in columns
# columns are Series :
print(type(test5))
print(type(test5["W"]))
# operations
test5["New"] = test5["W"] + test5["X"]
print(test5)
# removing columns
# test6 = test5.drop("New")
# print(test6)
# above we get error, because axis in pandas is in opposite direction than numpy so we must specify axis to 1
test6 = test5.drop("New", axis = 1)
print(test6)
# but the problem is that we still have that new column in old test5
print(test5)
# if we use inplace, we can drop columns everywhere
test6 = test5.drop("New", axis = 1, inplace = True)
print(test6) # None because inplace is called and its return is none
print(test5)

# selecting row
print(test5)
print(test5.loc['A'])
print(test5.loc[['A', 'B']])    # by label
print(test5.iloc[[0, 1]])       # by index
print(test5.loc['A', 'X'])      # by specific element row:A col:W
print(test5.iloc[0, 1])         # by specific element row:0 col:1
print(test5['W']['A'])
# print(test5[0][1])            # error
# slicing
print(test5.loc[
    ["A", "B"],
    ["X", "Y"]
])
# we can even do that on matrices
mat = np.arange(1, 26).reshape(5, 5)
test7 = pd.DataFrame(mat)
print(test7)
print(test7.loc[
    [0, 2, 4],
    [0, 2, 4]
])
print(test7.iloc[
    [0, 2, 4],
    [0, 2, 4]
])
# slicing using pandas is much more easier than numpy itself

# conditional selection query
test8 = test5 > 0
print(test8)
print(test5[test5["W"] > 0])