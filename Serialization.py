import json
#To encode a data structure to JSON, use the "dumps" method.
#This method takes an object and returns a String:
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print json_string
#To load JSON back to a data structure, use the "loads" method.
#This method takes a string and turns it back into the json object datastructure:
print json.loads(json_string)

import cPickle
pickled_string = cPickle.dumps([1, 2, 3, "a", "b", "c"])
print cPickle.loads(pickled_string)


import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print decoded_salaries["Alfred"]
print decoded_salaries["Jane"]
print decoded_salaries["Me"]
