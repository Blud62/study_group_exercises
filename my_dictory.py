my_dict = {
      'Piston': 3,
      'Lakers': 2,
      'Timberwolves': 1,
      'Heat':3,
}
'''''
# by default a for loop on a dictionary returns back 
# the keys in the dictionary
for key in my_dict:
    print(key)
my_dict['Celtics'] = 17 

# we can use the dict.items method to extract the keys and values
for key, value in my_dict.items():
     print(key,value)

# can use the dict.values method to return a list of the values 
# in a dictionary
for value in my_dict.values():
     print(value)

# can use the dict.key method to return a list of the keys 
# in a dictionary
for key in my_dict.keys():
     print(key)

# use brackets to return back a specific value in a dictionary
print(my_dict['Lakers'])
'''''
# use the value to return back a specific key in a dictionary
print(my_dict.keys())
print(my_dict.values())
