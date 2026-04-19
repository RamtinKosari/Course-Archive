# - List
test1 = "Interstellar"
print(test1[:])
print(test1[0])
print(test1[-1])
print(test1[2:5])
print(test1[::2])
print(test1[::-1]) # - reverse
print(test1[::-2])

# - Dictionary
test2 = {1:2}
print(test2)
print(test2[1])
test2 = {
    "item1": "value1",
    "item2": "value2"
}
print(test2)

# - Set
test3 = {1,2}
print(test3)
test3 = {1,2,1,2,1,2,1,2,1,2,1,2,1,2}
print(test3)

# - Range
test4 = range(5)
print(test4)
print(list(test4))
test4 = range(2, 5)
print(list(test4))
test4 = range(5, 2)
print(list(test4))
test4 = range(1, 15, 2)
print(list(test4))
test4 = range(15, 1, -1)
print(list(test4))

# - List Comprehensions
test5 = [i - 1 for i in test4]
print(test5)

# - Lambda Expressions
def test6(var: int):
    return var**2
print(test6(6))
# lambda is mostly being used in map and filter
test6 = lambda var: var**2
print(test6(6))

# - Map
test7 = [1, 2, 3, 4, 5, 6, 7]
print(7**2)
# print(test7**2) # Error
print(test7)
# - Map function into list of iterables
print(list(map(test6, test7)))
# - lambda used here :
print(list(map(lambda var: var**2, test7)))
# - so we do not need to write function in another place

# - Filter
def check_even(var: int):
    return var % 2 == 0
print(check_even(8))
print(check_even(9))
test8 = list(range(9))
print(test8)
test8_1 = list(filter(check_even, test8))
print(test8_1)
# - we can even use lambda
test8_2 = list(filter(lambda var: var % 2 == 0, test8))
print(test8_2)

# - Methods
test9 = "Interstellar Movie is Amazing"
print(test9.capitalize())
print(test9.lower())
print(test9.upper())
print(test9.count("l"))
print(test9.endswith(("Interstellar", "Movie")))
print(test9.endswith("Amazing"))
print(test9.find("Movie"))
print(test9.isascii())
print(test9.isalpha())
print(test9.strip())
print(test9.split())
print(test9.split("a"))
print(test9.replace("Amazing", "Fascinating"))
# dictionary methods
print(test2.keys())
print(test2.values())
# lists
print(test7)
test7.pop()
print(test7)
test7.remove(3)
print(test7)
