
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

