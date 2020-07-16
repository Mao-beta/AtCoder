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
    edges = [[i]+NLI() for i in range(N-1)]
    C = NLI()
    tree = [[] for _ in range(N+1)]
    for edge in edges:
        tree[edge[1]].append(edge[2])
        tree[edge[2]].append(edge[1])
    option_nums = []
    for i, node in enumerate(tree):
        option = len(node)
        option_nums.append([option, i])
    option_nums = sorted(option_nums)
    C = sorted(C)
    ans = {}
    for op, c in zip(option_nums[1:], C):
        ans[op[1]] = c
    A = 0
    for edge in edges:
        x, y = edge[1], edge[2]
        A += min(ans[x], ans[y])
    print(A)
    for i in range(1, N+1):
        if i == N:
            print(str(ans[i]))
            continue
        print(str(ans[i]), end=" ")

if __name__ == "__main__":
    main()