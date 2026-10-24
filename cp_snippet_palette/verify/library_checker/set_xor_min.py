# verification-helper: PROBLEM https://judge.yosupo.jp/problem/set_xor_min
import sys
from cp_snippet_palette.library.structures.binary_trie import BinaryTrie


def main():
    read = sys.stdin.buffer.readline
    trie = BinaryTrie(30)
    answer = []
    for _ in range(int(read())):
        t, x = map(int, read().split())
        if t == 0:
            if not trie.count(x):
                trie.add(x)
        elif t == 1:
            trie.discard(x)
        else:
            answer.append(str(trie.min_xor(x)))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
