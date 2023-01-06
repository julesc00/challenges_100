
def pop_an_item():
    lst1 = ["a", "b", "c"]
    for idx, item in enumerate(lst1):
        if item == "a":
            popped = lst1.pop(idx)
            return popped, lst1


numbers = [x for x in range(5+1)]
print(numbers)

names = ["Cari", "Luli", "Julito", "Cesar"]

names.insert(0, "Jemima")

print(names)

if __name__ == "__main__":
    print(pop_an_item())
