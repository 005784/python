class Student:
     # class variables
     name='pranee'
     def __init__(self,id,course):
         # instance variables
         self.id=id
         self.course=course
         print(self.id)
         print(self.course)
s=Student(1234,"ece")
# class variables can access through class name
print(Student.name)
s.name="neeraja"
print(s.name)
s.course="mech"
print(s.course)