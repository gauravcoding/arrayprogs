class employee:
    def __int__(self,name,salary):
        self.name=name
        self.salary=salary

    def   getSalary(self):
        return self.salary

rohan = employee("rohan","3455")
print(rohan.name)
print(rohan.salary)
