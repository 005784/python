# protected
class Person:
    def __init__(self,name,age):
        self.name=name
        self._age=age
    def display(self):
        print(self.name)
        print(self._age)
p=Person("pranee",20)
 # acceesing through class method
p.display()
#  accesing directly from outside
print(p.name)
print(p._age)
#private
class Person:
    def __init__(self,name)
