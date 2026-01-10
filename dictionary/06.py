# deleting an item from dictionary using del keyword
employee = {
    "name": "David",
    "age": 35,
    "city": "San Francisco",
    "position": "Manager"
}
print("Before deletion:", employee)

del employee["position"] # deleting 'position' key
del employee["age"]      # deleting 'age' key

# is this possible to delete non existing key?
# del employee["salary"]  # Uncommenting this line will raise KeyError
print("After deletion:", employee)

# deleting entire dictionary
temp_dict = {
    "temp_key1": "temp_value1",
    "temp_key2": "temp_value2"
}
print("Temporary dictionary before deletion:", temp_dict)
#del temp_dict
print(temp_dict)  # Uncommenting this line will raise NameError since temp_dict is

# clear() method to empty the dictionary
config = {
    "setting1": True,
    "setting2": False,
    "setting3": "default"
}
print("Config before clear:", config)
config.clear()
print("Config after clear:", config)