# multi level inheritance
class Employee:
    def __init__(self,name):
        self.name=name

    def getName(self):
        self.name

class Department(Employee):
    def __init__(self,name,id):
        self.id=id
    def getId(self,id):
        self.id
class Admin(Department):
    def __init__(self,name,id,location):
        self.name=name
        self.location=location
        self.id=id
    def getLoc(self,location):
        self.location
a=Admin("pranee",1234,"telangana")
print(a.name)
print(a.id)
print(a.location)


