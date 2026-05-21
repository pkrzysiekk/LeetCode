from suffix_tree import Tree
import time
import random
import string


def longest_palindrome_suffix_tree(s: str):
    if not s:
        return 0, 0

    n = len(s)
    rs = s[::-1]

    texts = {
        "S": s + "#",
        "R": rs + "$"
    }

    st = Tree(texts)

    def get_children(node):
        ch = getattr(node, "children", None)
        if not ch:
            return []
        return list(ch.values())

    def edge_length(node):
        end = getattr(node, "end", None)
        if isinstance(end, int):
            return end - node.start
        return len(texts[node.str_id]) - node.start

    leaves = []

    def collect_leaves(node, depth, path_nodes):
        ch = get_children(node)
        if not ch:
            if getattr(node, "str_id", None) in ("S", "R"):
                leaves.append((node.str_id, depth, node))
            return
        for child in ch:
            collect_leaves(child, depth + edge_length(child),
                           path_nodes + [child])

   # collect_leaves(st.root, 0, [])

    best_start = 0
    best_len = 1

    for i in range(n):

        l = i
        r = i
        while l >= 0 and r < n and s[l] == s[r]:
            cur_len = r - l + 1
            if cur_len > best_len:
                best_len = cur_len
                best_start = l
            l -= 1
            r += 1

    for i in range(n - 1):
        l = i
        r = i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            cur_len = r - l + 1
            if cur_len > best_len:
                best_len = cur_len
                best_start = l
            l -= 1
            r += 1

    return best_start, best_len


if __name__ == "__main__":
    s = "".join(random.choices(string.ascii_lowercase, k=5 * (10 ** 5)))

    begin = time.perf_counter()
    start, length = longest_palindrome_suffix_tree(s)
    stop = time.perf_counter()

    print(f"Zajelo: {stop - begin:.6f} s")
    print(f"Indeks: {start}, Długość: {length}")
    print(f"Palindrom: {s[start:start + length]}")
