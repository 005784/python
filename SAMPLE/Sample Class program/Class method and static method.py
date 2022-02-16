from datetime import date
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def fromBirthYear(cls,name,year):
         return cls(name,date.today().year-year)
    @staticmethod
    def isAdult(age):
        return age>18
p=Person("pranee",21)
p2=Person.fromBirthYear("pranee",1999)
print(p.age)
print(p2.age)
print(Person.isAdult(21))
