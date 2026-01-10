# creating a dictionary using zip() method
keys = ['name', 'age', 'city']
values = ['Bob', 25, 'Los Angeles']

print(type(keys))
print(type(values))

new_dictionary=dict(zip(keys, values))
print(new_dictionary)

period=[1,2,3,4]
topics=['Math','Science','English','History']
print(dict(zip(period,topics)))

print(period[0])
# accessing elements from list using index

