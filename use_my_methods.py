## Normal variable
username = 'Bhaskar'
## Lists - names and ages
names = [ 'Rakesh', 'Harsha', 'Sai', 'Bhaskar', 'Lehit' ]
ages  = [ 38, 22, 32, 42, 6]
## Dictionary
user_data = { 'Rakesh' : 38,
              'Harsha' : 22,
              'Sai'    : 32,
              'Bhaskar': 42,
              'Lehit'  : 6
              }
from my_methods import return_two_values, return_list_range
#from my_methods import *

first, last = return_two_values( names)
print( first)
print(last)
print ( return_list_range(names, 1,3))
print( return_list_range(names, -1, len(names)))
