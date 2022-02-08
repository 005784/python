# hybrid inheritance
class Student:
    def fun1(self,name):
        self.name=name
        print(self.name)
        print("i am employee class method")
#         multilevel inheritance
class Course(Student):
    def fun2(self,corname):
        self.corname=corname
        print("course name is " ,self.corname)
        print("i am course class method")
class Course1(Course):
    def fun3(self,cor1name):
        self.cor1name=cor1name
        print("course1 name is " ,self.cor1name)
        print("i am course1 class method")
#         multiple level inheritance
class Department(Course1,Course,Student):
    def fun4(self,deptid):
        self.deptid=deptid
        print("department id is",self.deptid)
        print("i am department class method")
d=Department()
d.fun4(1234)
d.fun3("phthon")
d.fun2("c ")