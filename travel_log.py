travel_log = [
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

# add an entry to the travel_log
country = input("Which country you have visited ?: ")
nr_cities = int(input("How much cities you have visited ?: "))
visits = int(input("How many visits in total ?: "))
cities = []

counter = 0
while counter < nr_cities:
    city = input("Which city you have visited ?: ")
    cities.append(city)
    counter += 1


def add_to_travel_log(visited_country, visited_cities, total_visits):
    travel_info = {}
    travel_info["country"] = country
    travel_info["visited_cities"] = cities
    travel_info["total_visits"] = visits

    return travel_info


travel_log.append(add_to_travel_log(country, cities, visits))
print(travel_log)
