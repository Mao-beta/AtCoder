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
    A, B, X, Y = NMI()
    if A == B:
        print(X)
        exit()

    if A < B:
        ans = X + (B-A) * min(2*X, Y)
    else:
        ans = X + (A-B-1) * min(2*X, Y)
    print(ans)


if __name__ == "__main__":
    main()
