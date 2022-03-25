names = ['harsha','gowri','hiamja']
ages = [ '21','45','26']
for index, name in enumerate(names)
    if name == 'harsha'
        print('found harsha at index{}.'format(index))
        print('his age{}.'format(ages[index]))
for count, name in enumerate(names, start=1):
    print("Name {} is {}".format(count, name))
    