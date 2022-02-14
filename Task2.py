from bs4 import BeautifulSoup
import xmltodict
import pprint
#XML -eXTENSIBLE MARKUP LANGUAGE
# Reading data from the xml file
class Parent:
   def parentDetails(self):
       with open('Image.xml', 'r') as f:
           data = f.read()
           print(data)
class Child(Parent):


   # Open the file and read the contents UNICODE TRANSFORMATION FORM
       def childDetails(self):
            with open('Image.xml', 'r') as file:
                 my_xml = file.read()

   # Use xmltodict to parse and convert
   # the XML document
            my_dict = xmltodict.parse(my_xml)  # xmltodict.parse to convert XML to PYTHONDICT

   # Print the dictionary
            pprint.pprint(my_dict, indent=4)  # Reading complex data in a easier way(pretty print)
c=Child()
c.parentDetails()
c.childDetails()
