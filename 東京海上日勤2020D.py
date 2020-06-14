import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    tree = [[0,0]] + [NLI() for _ in range(N)]
    Q = NI()
    querys = [NLI() for _ in range(Q)]

    def indexes(node):
        res = []
        for _ in range(20):
            res.append(node)
            node = node // 2
            if node == 0:
                break
        return res

    for node, limit in querys:
        idxes = indexes(node)
        items = [tree[idx] for idx in idxes]
        dp = make_grid(len(items)+1, limit+1, 0)
        for i, item in enumerate(items):
            i += 1
            for w in range(limit+1):
                if w >= item[1]:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-item[1]] + item[0])
                else:
                    dp[i][w] = dp[i-1][w]
        print(dp[len(items)][limit])


if __name__ == "__main__":
    main()