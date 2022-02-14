import csv
class Parent:
    def parent(self):
        with open('C:\python\image details.csv','w') as file:
             writer1 = csv.writer(file)
             writer1.writerow(["Filename", "file size", "image res","image name","no.of .objects","obj res"])
             writer1.writerow(["image", "100mb", "123pix","abcd","234","12"])


#: Read CSV
class Child(Parent):
    def child(self):
        with open('C:\python\image details.csv','r') as file:
                 reader = csv.reader(file)
                 for row in reader:
                     print(row)

c=Child()
c.parent()
c.child()