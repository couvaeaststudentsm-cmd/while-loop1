class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
    
    def display(self):
        print("Employee Name:",self.name)
        print("Employee salary:",self.salary)

e1 = Employee("Riya",500000)
e1.display()