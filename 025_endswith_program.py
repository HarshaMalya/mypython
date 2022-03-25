txt = 'hi this is harsha.'

x = txt.endswith("harsha.")

print(x)

names = [ 'Rakesh', 'Harsha', 'Sai', 'Bhaskar', 'Lehit' ]
ages  = [ 38, 22, 32, 42, 6]

for index, name in enumerate(names):
    if name == 'Bhaskar':
        print("Found Bhaskar at index {}.".format(index))
        print("His age is {}".format( ages[index]))
for count, name in enumerate( names, start=1):
    print("Name {} is {}".format(count, name))

