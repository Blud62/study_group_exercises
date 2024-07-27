# my_var = 1

# def my_func():
#     global my_var
#     my_var = 2

# my_func()
# print(my_var)

# for num in range(5):
#   print(num)

x = 10

def my_function():
  global x 
  #x = 10
  x = x + 5 # variable shadowing
  print(x)

my_function()