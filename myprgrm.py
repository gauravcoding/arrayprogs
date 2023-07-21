age=input("enter your age")
age =int(age)
if age>=18:
    print("you can vote")
elif age>=12 and age<=18:
    print("you're a teen")
else:
    print("you are a kid")
