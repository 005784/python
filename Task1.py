import json
imagedetails={
    "file1":{
        "filename":"image",
        "filesize" :   "12mb",
        "imageres":"20pix",
        "imagename":"abcd",
        "objects":"100",
        "objres":"20"
    }
}
class Parent:
    def innerMethod(self):
         with open("image.json","w")as c:
             json.dump(imagedetails,c)
class Child(Parent):
    def outerMethod(self):
         with open("image.json",'r') as external:
               a=json.load(external)
               print(a)
               print(type(a))





c=Child()
c.outerMethod()
c.innerMethod()


