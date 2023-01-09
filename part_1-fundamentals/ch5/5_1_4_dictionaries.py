

"""
5.1.4 Key-value mappings (Dictionaries)
"""

my_dict = {"name": "Jemima"}
my_dict["middle_name"] = "Eloise"
user_card = {"city": "Los Angeles"}
print(my_dict)
user_card.update(my_dict)
print(user_card)
for k, v in user_card.items():
    print(k, v)


def update_user_data(card: dict) -> dict:
    try:
        card.pop("country")
    except KeyError as error:
        print(f"[ERROR] Entry: {error} not found!")
    return card


print(update_user_data(user_card))

city_sizes = {
    "Cologne": 1_000_000,
    "Kiel": 250_000,
    "Bremen": 550_000,
    "Zurich": 400_000,
    "Oldenburg": 170_000
}


# Filtering elements of a dictionary in a general way.
def filter_dict(input_dict, key_value_condition):
    filtered_dict = dict()
    for key, value in input_dict.items():
        if key_value_condition((key, value)):
            filtered_dict[key] = value
    return filtered_dict


def filter_by_value(input_dict, value_condition):
    filtered_results = filter_dict(input_dict, lambda item: value_condition(item[1]))
    return filtered_results


print(filter_dict(city_sizes, lambda city: 200_000 <= city[1] <= 700_000))
filtered_cities = filter_by_value(city_sizes, lambda size: 200_000 <= size <= 700_000)
print(filtered_cities)
print(set(filtered_cities.keys()))
print(set(filtered_cities.values()))
