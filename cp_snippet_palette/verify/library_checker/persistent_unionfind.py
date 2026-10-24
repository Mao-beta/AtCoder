# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_unionfind
import sys
from cp_snippet_palette.library.structures.rollback_dsu import RollbackDSU


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    children = [[] for _ in range(q + 1)]
    queries = [None] + [tuple(map(int, read().split())) for _ in range(q)]
    for i in range(1, q + 1):
        children[queries[i][1] + 1].append(i)
    dsu = RollbackDSU(n)
    answer = [None] * (q + 1)
    stack = [(0, False)]
    while stack:
        i, leaving = stack.pop()
        if leaving:
            dsu.undo()
            continue
        if i:
            t, k, u, v = queries[i]
            if t == 0:
                dsu.merge(u, v)
                stack.append((i, True))
            else:
                answer[i] = str(int(dsu.same(u, v)))
        for child in reversed(children[i]):
            stack.append((child, False))
    print("\n".join(x for x in answer if x is not None))


if __name__ == "__main__":
    main()
