
names1 = ["Jemima", "Jamal", "Michele", "Brigitte"]
names2 = ["Cari", "Julieta", "Cesar", "Julito"]

names = names1 + names2

print(names)
print(names[::-1])
print(names[::2])
print("len: %d, min: %s, max: %s" % (len(names), min(names), max(names)))
print(f"len: {len(names)}, min: {min(names)}, max: {max(names)}")


def rindex(values, item):
    reversed_values = values[::-1]
    return len(values) - reversed_values.index(item) - 1


print(rindex(names, "Cari"))

names[4] = "Tai"
print(names)

print(names.count("Tai"))


def remove_item(values: list, name: str) -> str:
    try:
        values.remove(name)
        return f"{name} was removed from the list."
    except ValueError as error:
        return f"{name} is not in the list, error: {error}"


print(remove_item(names, "John"))


"""
List Comprehension
It's an elegant possibility for creating new data structures. A list comprehension is an expression that 
generates a new result list based on a sequence of values and a calculation rule to generate a new list of 
results.
"""

even_numbers = [num for num in range(1, 100+1) if num % 2 == 0]
print(even_numbers)

my_tuple_list = [(x, y) for x in range(3) for y in range(5+1)]
print(my_tuple_list)

my_tuple_list_xyz = [(x, y, z) for x in range(3) for y in range(5+1) for z in range(3)]
print(my_tuple_list_xyz)


"""
Variant as a set and dictionary comprehension
"""
my_odd_set = {i for i in range(10+1) if i % 2 != 0}
print(my_odd_set)

my_even_dict = {n: n ** 2 for n in range(10+1) if n % 2 == 0}
print(my_even_dict)


"""
`Inplace variants` for removing all elements from a collection that match a certain value.
"""


# Not optimal variant
def remove_all_inplace(lst: list, value):
    try:
        while True:
            lst.remove(value)
    except ValueError as error:
        print(error)


# Not optimal variant either :/
def remove_all_inplace_improved(values: list, item):
    """
    This is a O(n2), due to the implementation of .remove(); not optimized
    """
    while item in values:
        values.remove(item)


# Better performance
def remove_all_fast(values: list, item):
    write_idx = 0
    for value in values:
        if value != item:
            values[write_idx] = value
            write_idx += 1
    return values[:write_idx]


# Improved, though it used slightly more memory since it creates another list (list comprehension).
def remove_all_v2(values: list, item):
    return [value for value in values if value != item]


def remove_all_v3(values: list, item):
    return list(filter(lambda x: x != item, values))


"""
Custom implementation of collect_all()
"""


def collect_all(values, condition):
    result = []
    for elem in values:
        if condition(elem):
            result.append(elem)
    return result


# List comprehension
def collect_all_v2(values, condition):
    return [elem for elem in values if condition(elem)]


# With Filter
def collect_all_v3(values, condition):
    return list(filter(condition, values))


remove_all_inplace(names, "Jemima")
print(names)

remove_all_fast(names, "Michele")
print(names)

remove_all_v2(names, "Julito")
print(f" with v2: {names}")
