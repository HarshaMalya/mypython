num = 2
for count in range(1,10):
    for x in range(1,count+1):
        print(f"{num:>2}",end=' ')
        num = num+2
        if num > 20:
            print('\n')
            exit(1)
    print()