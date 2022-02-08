class B:
    def b(self,name):
        self.name=name
        print(self.name)
        print("i am B class")
class A:
    def a(self,age):
        self.age=age
        print(self.age)
        print("i am A class")
class C(B,A):
    def c(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
        print("i am D class")
d=C()
d.b("pranee")
d.a(20)
d.c("pranee",20)


