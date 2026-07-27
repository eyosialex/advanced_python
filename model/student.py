class Student :
    def __init__(self,name,age,department,gpa):
        self.name=name;
        self.age=age
        self.department=department;
        self.gpa=gpa
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("deparment",self.department)
        print ("gpa",self.gpa)
    def ginuen(self):
        return self.gpa>3.5
    