from itertools import permutations


def possible_permutations(some_list):
    perm = permutations(some_list)
    for p in perm:
        yield list(p)