# verification-helper: PROBLEM https://judge.yosupo.jp/problem/queue_operate_all_composite
import sys
from cp_snippet_palette.library.structures.aggregate_queue import AggregateQueue


def main():
    read = sys.stdin.buffer.readline
    mod = 998244353

    def op(f, g):
        # 先頭fを適用してから、後ろのgを適用する。
        return g[0] * f[0] % mod, (g[0] * f[1] + g[1]) % mod

    queue = AggregateQueue(op, (1, 0))
    output = []
    for _ in range(int(read())):
        query = list(map(int, read().split()))
        if query[0] == 0:
            queue.append((query[1], query[2]))
        elif query[0] == 1:
            queue.popleft()
        else:
            a, b = queue.prod()
            output.append(str((a * query[1] + b) % mod))
    sys.stdout.write("\n".join(output) + ("\n" if output else ""))


if __name__ == "__main__":
    main()
