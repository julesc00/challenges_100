
color_set = {"RED", "GREEN", "BLUE"}
color_set.update(["YELLOW", "ORANGE"])
color_set.add("GOLD")
print(color_set)

number_set1 = {1, 2, 3, 4, 5, 6, 7, 8}
number_set2 = {2, 3, 5, 7, 9, 11, 13}
print(f"""
    union: {number_set1 | number_set2}
    intersection: {number_set1 & number_set2}
    diff: {number_set1 - number_set2}
    sym diff: {number_set1 ^ number_set2}
""")


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


def update_user_data() -> dict:
    try:
        user_card.pop("country")
    except KeyError as error:
        print(f"[ERROR] Entry: {error} not found!")
    return user_card


print(update_user_data())


# Filtering elements of a dictionary in a general way.
def filter_dict(input_dickt, key_value_condition)
