# - Numpy
import numpy as np

# convert list to array
my_list = list(range(5))
print(np.array(my_list))

# convert nested list to array / matrix
my_matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
print(np.array(my_matrix))

# range method in numpy
print(np.arange(11))
print(np.arange(5, 16))
print(np.arange(1, 11, 2))
print(np.arange(11, 1, -1))

# zeroes, ones, eye
print(np.zeros(3))
print(np.ones(
    (3, 3)
))
print(np.eye(4))

# linspace
print(np.linspace(0, 10, 2))
print(np.linspace(0, 10, 3))
print(np.linspace(0, 10, 4))
print(np.linspace(0, 10, 5))

# random
# - random number between 0, 1
print(np.random.rand())
# - random numbers between 0, 1 in shape of array or matrix
print(np.random.rand(2))
# normalized random : might be higher than 1 or lower than -1 --> normal distribution with average 0 and variance 1 ?
print(np.random.randn(5, 2))
# randint : random int between 0 to 10
print(np.random.randint(10))
# randint : random int between 2 to 12
print(np.random.randint(2, 12))
# randint : 5 random int between 1 to 20
print(np.random.randint(1, 20, 5))

# reshape
arr = np.arange(36)
print(arr)
print(arr.reshape(6, 6))
print(arr.reshape(4, 9))
print(np.random.randint(0, 50, 15).reshape(5, 3))

# min, max, argmin, argmax
arr = np.random.randint(0, 50, 20)
print(arr)
print(arr.max())
print(arr.min())
# if we want to know what index it is :
print(arr.argmin())
print(arr.argmax())

# dtype
print(arr.dtype)
print(np.array([1, 2, 3, 4, 5, 6, 7, 8]).dtype)
print(np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype = float).dtype)

# bracket indexing and selection
print(arr[3])
print(arr[3:7])

# broadcasting
print(arr)
arr[3:5] = 100
print(arr)

# numpy pointers
arr1 = list(range(10))
print(arr1)
# - if you copy part of a list and change it, main array wont be changed
arr1_copy = arr1[0:4]
print(arr1_copy)
arr1_copy = [37 for i in arr1_copy]
print(arr1_copy)
print("stays like before :", arr1)
arr2 = np.arange(10)
arr2_copy = arr2[0:4]
print(arr2_copy)
arr2_copy[:] = 37
print(arr2_copy)
print("changed, because numpy use pointers :", arr2)
# we can use copy method instead
arr2 = np.arange(10)
arr2_copy = arr2.copy()[0:4]
print(arr2_copy)
arr2_copy[:] = 37
print(arr2_copy)
print("remains same because we used copy() :", arr2)

# transpose
array_2D = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(array_2D)
print(array_2D.transpose())

# slicing in 2D arrays
array_2D = np.arange(1, 101).reshape(10, 10)
print(array_2D, "\n")
# first slice is row
print(array_2D[3:7], "\n")
# but second slice is not column, it is still row
print(array_2D[3:7][0], "\n")
# for accessing to column we have to :
print(array_2D[3:7 , 5:], "\n")
# and for accessing individuals, these two are same
print(array_2D[3:, 5:][0][1])
print(array_2D[3:, 5:][0, 1])
# also these 2 are same
print(array_2D[3:, 5:])
print(array_2D[3:][:, 5:])
print("\n")

# fancy indexing
print(array_2D[2:5])
# but what if we dont want row #3 :
print(array_2D[[2, 4]])

# selection
arr = np.arange(1, 11)
print(arr)
print(arr > 4)
print(arr == 3)
bool_arr = arr > 4
print(bool_arr)
# slicing can be that bool array
print(arr[bool_arr])
print("\n")

# numpy operations
# array with array (arithmetic)
arr = np.arange(0, 11)
print(arr)
print(arr + arr)
print(arr - arr)
print(arr * arr)
# array with scaler
print(arr + 100)
print(arr * 2)
print(arr - 5)
# universal array functions
print(np.sqrt(arr))
print(np.exp(arr))
print(np.sin(arr))
print(np.cos(arr))
print(np.log(arr))
print(np.log10(arr))
print("\n\n")

# flatten
arr = np.random.randn(5, 5)
print(arr)
print(arr.shape)
print(arr.flatten())
print(arr.flatten().shape)

# vstack, hstack, concatenate
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.vstack(
    (arr1, arr2)
))
print(np.hstack(
    (arr1, arr2)
))
print(np.concatenate(
    (arr1, arr2)
))
