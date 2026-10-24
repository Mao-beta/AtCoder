# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat
import sys
from cp_snippet_palette.library.graphs.scc import two_sat


def main():
    read = sys.stdin.buffer.readline
    _, _, n, m = read().split()
    n, m = int(n), int(m)
    clause = []
    for _ in range(m):
        a, b, _ = map(int, read().split())
        clause.append((abs(a) - 1, a > 0, abs(b) - 1, b > 0))
    answer = two_sat(n, clause)
    if answer is None:
        print("s UNSATISFIABLE")
    else:
        print("s SATISFIABLE")
        print("v", *[i + 1 if x else -i - 1 for i, x in enumerate(answer)], 0)


if __name__ == "__main__":
    main()
