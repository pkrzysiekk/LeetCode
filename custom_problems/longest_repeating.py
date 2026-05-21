from suffix_tree import Tree, mccreight
import random
import string
import time


def find_lrs(s):
    tree = Tree({"A": s})
    text_len = len(s)
    max_len = 0
    start = 0
    end = 0
    for C, path in tree.maximal_repeats():

        path_len = path.end - path.start

        if text_len == path_len:
            continue

        if path_len > max_len:
            start = path.start
            end = path.end
            max_len = path_len

    return (start, end)


s = "".join(random.choices(string.ascii_lowercase, k=5 * (10 ** 5)))
begin = time.perf_counter()
start, end = (find_lrs(s))
stop = time.perf_counter()
print([start, end - 1])
print(f"Took: {stop - begin}s")
