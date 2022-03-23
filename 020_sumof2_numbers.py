#a=int(input('enter the value for a:'))

#b=int(input('enter the value for b:'))

## A Method to add 2 numbers and return sum
def add_2_numbers(num1, num2):
    sum = num1 + num2
    return sum

import sys
print( "Total arguments from CLI are: {}".format( len(sys.argv)))
print("The program name is : {}".format( sys.argv[0]))
print("The cli arguments to program are: {}".format( sys.argv[1:]))
a = int(sys.argv[1])
b = int(sys.argv[2])

numsum1 = add_2_numbers( a, b)
print( "Sum of {0} + {1} = {2}".format(a, b, numsum1))

numsum1 = add_2_numbers( 99, 1)
print( "Sum of {0} + {1} = {2}".format(99, 1, numsum1))

numsum1 = add_2_numbers( 100, -1)
print( "Sum of {0} + {1} = {2}".format(100, -1, numsum1))
