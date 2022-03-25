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

for key in user_data.keys():
    if key == username:
        print( user_data[key])
print("=" * 60)
def common_display(name, mylist, mydict = None):
    print(name)
    print(mylist)
    print(mydict)

common_display(username, names, user_data)

def return_two_values( names):
    return names[0], names[-1]

def return_list_range( names, start, end):
    #if start < 0:
    #    print( "ERROR: Start can not be less than zero")
    #    raise ValueError("ERROR: Start can not be less than zero")
    return names[start:end]

first, last = return_two_values( names)
print( first)
print(last)

print ( return_list_range(names, 1,3))
print( return_list_range(names, -1, len(names)))
'''
print( type(username))
print( username)
print( type(names))
print( names)
print( ages)
print( type(user_data))
print( user_data)
'''
