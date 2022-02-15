import json
# #
# Opening JSON file
f = open('data.json','r')

# returns JSON object as
# a dictionary
data = json.load(f)
# #
#
# # # # Iterating through the json
# # # # list
# for i in data['employee']:
#  print(i)
#
# # Closing file
# f.close()
# # Python program to write into json file
# import json
#
# Data to be written
dictionary ={
         "id": "05",
         "name": "Nancy",
         "department": "Sales"
      }

with open("data.json", "a") as outfile:
   json.dump(dictionary, outfile)
