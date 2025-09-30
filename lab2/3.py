def recursive_reverse(some_list):
    if len(some_list) <= 1:
        return some_list
    else:
        return recursive_reverse(some_list[1:]) + [some_list[0]]

print(recursive_reverse([1, 2, 3]))