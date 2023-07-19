from array import *
arr = array('i',[])
n=int(input("enter the number of values"))
for i in range(n):
    x= int(input("enter the next value"))
    arr.append(x)

print(arr)

j=int(input("enter the value you want search"))
k=0
for e in arr:
    if e == j:
        print(k)
        break
    k+=1
else:
    print("value not found")

