# Read a number and print multiplication table for that number up to 10
# Ex:
#   Enter a number : 5
#  Result:
#   The multiplication table for given number 5 is as below:
#   5 x  1 =  5
#   5 x  2 = 10
#...
#   5 x 10 = 50
#
a=int(input('enter an integer:'))
p=len(str(a))+1
for count in range (1,11):
    product=int(a)*int(count)
    print(f'{a:>2} * {count:>2} = {product:>{p}}')


