# pop method removes the specified key and returns the corresponding value

# synatx of pop method: dict.pop(key, default=None)

fruit_prices = {
    "apple": 2.5,
    "banana": 1.2,
    "orange": 1.8,
    "grape": 3.0
}
# trying to pop a key which is not present in dictionary
apple=fruit_prices.pop("Suchandra"," is a good girl")
print("Price of apple:", apple)


print("Before pop:", fruit_prices)

removed_price = fruit_prices.pop("banana")  # removing 'banana' key

print("Removed price of banana:", removed_price)

print("After pop:", fruit_prices)

#popitem method removes and returns an arbitrary (key, value) pair from the dictionary

config_settings = {
    "resolution": "1920x1080",
    "volume": 75,
    "brightness": 50,
    "language": "English",
    "theme": "Dark"
}
print("Before popitem:", config_settings)
#remove first time
removed_item1 = config_settings.popitem()

# remove second time
removed_item2 = config_settings.popitem()

# remove third time
removed_item3 = config_settings.popitem()

# remove fourth time
removed_item4 = config_settings.popitem()

print("Removed item:", removed_item1)
print("Removed item:", removed_item2)
print("Removed item:", removed_item3)
print("Removed item:", removed_item4)

print("After popitem:", config_settings)
