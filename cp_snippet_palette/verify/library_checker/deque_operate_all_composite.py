# verification-helper: PROBLEM https://judge.yosupo.jp/problem/deque_operate_all_composite
import sys
from cp_snippet_palette.library.structures.aggregate_deque import AggregateDeque


def main():
    read = sys.stdin.buffer.readline
    mod = 998244353

    def op(f, g):
        return g[0] * f[0] % mod, (g[0] * f[1] + g[1]) % mod

    d = AggregateDeque(op, (1, 0))
    answer = []
    for _ in range(int(read())):
        query = list(map(int, read().split()))
        t = query[0]
        if t == 0:
            d.appendleft(tuple(query[1:]))
        elif t == 1:
            d.append(tuple(query[1:]))
        elif t == 2:
            d.popleft()
        elif t == 3:
            d.pop()
        else:
            a, b = d.prod()
            answer.append(str((a * query[1] + b) % mod))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
