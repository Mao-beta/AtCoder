import sys
import math
from collections import deque
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    C = Counter(SI())
    C = list(C.items())
    C.sort(key=lambda x: x[1], reverse=True)
    print(C[0][0])


if __name__ == "__main__":
    main()