# python file following class example
import json

data1 = {

    "name": "John Appleseed", #string value
    "age": 30, #integer value
    "city": "New York", #string value
    "interests":["reading", "traveling", "swimming"], #list of strings
    "is_student": False #boolean value

}

with open('data1.json', 'w') as json_file:

    json.dump(data1, json_file, indent=4)
# This code creates a JSON file named 'data.json' with the specified data structure.

print("JSON file created successfully")