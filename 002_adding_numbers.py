#a=input('enter the first number:')
#b=input('enter the second number:')
a=int(input('enter the first number:'))
b=int(input('enter the second number:'))

sum = a + b
if type(a) is str:
    print('sum of strings is :',sum)
else:
    print('sum of numbers is :', sum)

