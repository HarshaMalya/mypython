username = 'hima'
names = ['harsha', 'hima', 'gowri',]
ages  = [21, 26, 42,]
## Dictionary
user_data = { 'harsha' : 21,
              'hima'   : 26,
              'gowri'  : 42,
              }

for key in user_data.keys():
    if key == username:
        print( user_data[key])

def common_display(name, mylist, mydict):
    print(name)
    print(mylist)
    print(mydict)

common_display(username, names, user_data)

def return_two_values( names):
    return names[1], names[2]

def return_list_range( names, start, end):
    return names[start:end]

first, last = return_two_values( names)
print( first)
print(last)
