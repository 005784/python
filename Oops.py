class Employee:
    def fun1(self):

        print("i am employee function")
class Department(Employee):
    def func2(self):

        print("i am department function")
class Admin(Department,Employee):
    def func3(self):
        print("i am admin function")
object=Admin()
object.fun1()
object.func2()
object.func3()


