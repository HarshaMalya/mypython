my_list=['himja', 'harsha', 'gowri', 'harsha', 'himaja', 'harsha']
print('the original list is:' + str(my_list))
res=[]
for text1 in my_list:
    if text1 not in res:
        res.append(text1)
print('the list after removing duplicates:{}'.format(res))
