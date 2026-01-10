# accessing dictionary values using keys
student = {
    "name": "Charlie",
    "age": 28,
    "city": "Chicago"
}
print(student["name"])  # Output: Charlie

# acessing key which is not present in dictionary will raise KeyError
print(student["country"])  # Uncommenting this line will raise KeyError