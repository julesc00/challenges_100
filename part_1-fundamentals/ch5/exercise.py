
ids = [
    "aaa111",
    "bbb111",
    "ccc111",
    "fff111",
    "ppp111"
]

captured_ids = [
    "ddd111",
    "aaa111",
    "eee111",
    "ppp111"
]


def filter_ids(local_ids: list, cap_list: list):
    local_id_set, cap_id_set = set(local_ids), set(cap_list)
    # & is the set 'intersection' method
    already_registered_ids = list(local_id_set & cap_id_set)
    not_registered_ids = []
    for cap_id in local_ids:
        if cap_id in already_registered_ids:
            print(f"[WARNING] '{cap_id}' ID is already registered, you cannot add it.")
    for cap_id in already_registered_ids:
        if cap_id == cap_list:
            not_registered_ids.append(cap_id)
    print(not_registered_ids)


filter_ids(ids, captured_ids)
