'''
#by default a for loop on a dictionary returns back the keys in the dictionary
for key in numbers:

# we can use the dict.items method to extract the keys and values
for key,value in numbers.items():
    print(key, value)

# we can use the dict.values method to return a list of the values in a dictionary
for key in numbers.keys():
    print(key)

# use brackets to return back a specific value in a dictionary
x = numbers['medium']
print(x)

# use the value to return back a specific key in a dictionary
# i = numbers.index(50)

#list#append()
https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/

PEDAC
    Problem
        Input:  given a dictionary
        Output: list of values containing the values that are even as integers
                and values that are odd as floats
    Example:

    Data Structure list

    Algorithm
        Use for loop to iterate over the values of dictionary
        create an empty list 'half_numbers"
        divide number by 2 and append to half_numbers
'''
numbers = {
  'high': 100, #50.0
  'medium': 50, #25.0
  'low': 25,    #12
}

half_numbers = []

for value in numbers.values():
    result = value // 2
    if value % 2 != 0:
        half_numbers.append(value)
    else:
        half_numbers.append((value))

print(half_numbers)


# creating a new dictionary
# my_dict = {
#     "Java":100, 
#     "Python":112, 
#     "C":11,
# }
 
# # one-liner
# print("One line Code Key value: ", list(my_dict.keys())
#       [list(my_dict.values()).index(100)])