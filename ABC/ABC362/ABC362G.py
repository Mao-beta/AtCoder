import sys
from collections import deque, defaultdict

sys.set_int_max_str_digits(10 ** 6)
sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.read().strip()
MOD = 10 ** 9 + 7
MOD99 = 998244353

ALPHABET_SIZE = 26
OFFSET = ord('a')


class TrieNode:
    def __init__(self):
        self.children = [None] * ALPHABET_SIZE
        self.output = []
        self.fail = None


def build_automaton(keywords):
    root = TrieNode()

    # Step 1: Build the Trie
    for keyword in keywords:
        node = root
        for char in keyword:
            index = ord(char) - OFFSET
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.output.append(keyword)

    # Step 2: Build the failure links using BFS
    queue = deque()
    for node in root.children:
        if node:
            node.fail = root
            queue.append(node)

    while queue:
        current_node = queue.popleft()
        for i in range(ALPHABET_SIZE):
            next_node = current_node.children[i]
            if next_node:
                queue.append(next_node)
                fail_node = current_node.fail
                while fail_node and not fail_node.children[i]:
                    fail_node = fail_node.fail
                next_node.fail = fail_node.children[i] if fail_node else root
                next_node.output.extend(next_node.fail.output if next_node.fail else [])
    return root


def search_text(text, root):
    result = defaultdict(int)
    current_node = root

    for char in text:
        index = ord(char) - OFFSET
        while current_node and not current_node.children[index]:
            current_node = current_node.fail
        if not current_node:
            current_node = root
            continue
        current_node = current_node.children[index]
        for keyword in current_node.output:
            result[keyword] += 1

    return result


def main():
    input_data = sys.stdin.read().split()
    S = input_data[0]
    Q = int(input_data[1])
    Ts = input_data[2:2 + Q]

    unique_Ts = list(set(Ts))
    root = build_automaton(unique_Ts)
    matches = search_text(S, root)

    output = []
    for T in Ts:
        output.append(str(matches[T]))

    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
