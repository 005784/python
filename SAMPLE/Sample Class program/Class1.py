# class Person:
#     def  __init__(self,name,age):
#          self.name=name
#          self.age=age
#
#
# p=Person("pranee",20)
# print(p.name)
# print(p.age)
# class Student:
#     def  __init__(self,name,id):
#         self.name=name
#         self.id=id
#
# s=Student("pranee",124)
# print(s.name)
# print(s.id)
# class Student:
#     def __init__(self,name,subject,id):
#         self.name=name
#         self.subject=subject
#         self.id=id
#     def myfunc(self):
#         print("my name is " + self.name,"my subject is " + self.subject,"my id is", + self.id)
# s1=Student("pranee","python",1234)
# s1.myfunc()
# class Student:
#     def __init__(efg,name,age):
#         efg.name=name
#         efg.age=age
#     def myfunct(efg):
#         print("name is " +efg.name,"age is",+efg.age)
# s2=Student("pranee",20)
# print(s2.name)
# print(s2.age)
# s2.myfunct()
class Employee:
    def __init__(self,dept,role):
        self.dept=dept
        self.role=role
    def fun(self):
        print("dept number is" ,+self.dept,"role is" + self.role)
e=Employee(1234,"consultant")
print(e.dept)
print(e.role)
e.fun()








