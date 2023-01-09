
def remove_all(values: list, item) -> list:
    idx = 0
    for value in values:
        if value != item:
            values[idx] = value
            idx += 1
    return values[:idx]


def remove_all_v2(values, item):
    # I like this one better
    return [value for value in values if value != item]


def remove_all_v3(values, item):
    return list(filter(lambda x: x != item, values))


"""
Collect all elements
"""


# Iteration
def collect_all(values: list, condition) -> list:
    result = []
    for el in values:
        if condition(el):
            result.append(el)
    return result


# List comprehension
def collect_all_v2(values: list, condition) -> list:
    return [el for el in values if condition(el)]


# Filter
def collect_all_v3(values: list, condition) -> list:
    return list(filter(condition, values))


if __name__ == "__main__":
    print(remove_all(["a", "a", "b"], "a"))
    print(remove_all_v2(["a", "a", "b"], "a"))
    names = ["Cari", "Jemi", "Luli", "Luli", "Luli"]
    print(collect_all_v2(names, lambda val: val == "Luli"))
    print(collect_all_v3(names, lambda value: value == "Luli"))
