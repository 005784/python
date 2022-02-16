# Example 1: Read CSV
import csv
# with open('Book1.csv') as csvfile:
#  data = csv.reader(csvfile, delimiter=' ')
#  for row in data:
#    print(' '.join(row))
# import csv
#
with open('C:\python\student details.csv','w') as file:
    writer1 = csv.writer(file)
    writer1.writerow(["SN", "student name", "student id"])
    writer1.writerow([1, "pranee", "123"])
    writer1.writerow([2, "neeru", "345"])
#     # Example 2: Read CSV
import csv
with open('C:\python\student details.csv','r') as file:
           reader = csv.reader(file)
           for row in reader:

               print(row)



