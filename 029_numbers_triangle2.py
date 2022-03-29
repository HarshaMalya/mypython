# Print below sequence
#   1
#   3   5
#   7   9   11
#  13  15   17   19
num = 1
for count in range(1,5):
    for x in range(1,count+1):
        print(f"{num:>2}",end=' ')
        num = num+2
        if num > 19:
            print('\n')
            exit(1)
    print()


