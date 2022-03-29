my_list=[9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9]
my_list.sort()
print(my_list)
res=[]
for i in my_list:
    if i not in res:
        res.append(i)
print('the list after removing duplicates:{}'.format(res))
loc1=2
loc2=4
print(res[loc1])
print(res[loc2])
temp=res[loc1]
res[loc1]=res[loc2]
res[loc2]=temp
print(res[loc1])
print(res[loc2])
print(res)







