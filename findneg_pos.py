list1 = [2, -7, 5, -64, -14]
pos_count , neg_count = 0, 0
for num in list1:
    if num>=0:
        pos_count +=1
    else:
        neg_count +=1

print('postive numbers:-',pos_count)
print('negative numbers:-',neg_count)
