# Print below sequence of numbers up to 10
# 1
# 2 3
# 4 5 6
# 7 8 9 10
#####################################
num = 1
for count in range(1, 10):
    for x in range(1,count+1):
        print(num,end=" ")
        num = num+1
        if num > 10:
            print("\n")
            exit(1)
    print()









