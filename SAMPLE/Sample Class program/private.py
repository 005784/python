#private
class Parent:
    def _protected(self,age):
        self._age=age
        print(self._age)
        print("it is protected method")
        pass
    def __private(self,name):
        self.name=name
        print(self.name)
        print("it is private method")
class Child(Parent):
    def func1(self):
        self._protected()
    def func2(self):
        self.__private()
c=Child()
c._protected(20)
c._Parent__private("pranee")

