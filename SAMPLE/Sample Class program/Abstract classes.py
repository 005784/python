from abc import ABC,abstractmethod
class Car(ABC):
    def __init__(self,name):
        self.name=name
    def description(self):
        print("the description function of the car")
    @abstractmethod
    def price(self,x):
        pass
class New(Car):
    def price(self,x):
         print(f"the {self.name}'s price is {x}.lakhs")
obj=New("xcent")
obj.description()
obj.price(500000)
