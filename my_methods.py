def common_display(name, mylist, mydict = None):
    print(name)
    print(mylist)
    print(mydict)

def return_two_values( names):
    return names[0], names[-1]

def return_list_range( names, start, end):
    #if start < 0:
    #    print( "ERROR: Start can not be less than zero")
    #    raise ValueError("ERROR: Start can not be less than zero")
    return names[start:end]
