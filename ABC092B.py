import sys
import math
from collections import defaultdict
from collections import deque

# sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    D, X = NMI()
    A = [NI() for _ in range(N)]
    for a in A:
        X += (D-1) // a + 1
    print(X)


if __name__ == "__main__":
    main()
