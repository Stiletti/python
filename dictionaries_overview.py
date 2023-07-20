# dictionary syntax
dic_name = {
    "key": "value",
}

print(dic_name)

# wipe dictionary
dic_name = {}

# add item to dictionary
dic_name["new_key"] = "new_value"

print(dic_name)

# loop through dictionaries is the same as with lists
for key in dic_name:
    # print keys
    print(key)
    # print values
    print(dic_name[key])
    # print together with f-string format
    print(f"key: {key}, value: {dic_name[key]}")

# nesting dictionaries and using lists inside dictionaries for better datastructure
travel_log = {
    "France": {
        "cities_visited": ["Lion", "Paris", "Dijon"],
        "visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Kiel", "Stuttgart"],
        "visits": 7
    }
}

# nesting dictionaries inside a list
travel_list = [
    {
        "country": "England",
        "cities": ["London", "Bristol", "New Castle"],
        "total_visits": 13
    },
    {
        "country": "USA",
        "cities": ["Denver", "New York", "Ohio"],
        "total_visits": 17
    }
]
