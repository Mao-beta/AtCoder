import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    A, B = NMI()
    ans = [[0]*100 for _ in range(50)] + [[1]*100 for _ in range(50)]

    for i in range(0, 2*B-2, 2):
        h = i // 100 * 2
        w = i % 100
        ans[h][w] = 1

    for i in range(0, 2*A-2, 2):
        h = i // 100 * 2 + 51
        w = i % 100
        ans[h][w] = 0

    print(100, 100)
    for row in ans:
        row = ["#" if x else "." for x in row]
        print("".join(row))


if __name__ == "__main__":
    main()
