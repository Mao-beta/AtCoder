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
    S = SI()
    L = [-1]*26
    for i, s in enumerate(S, start=1):
        si = ord(s) - 97
        pi = L[si]
        if i - pi <= 2 and pi != -1:
            print(pi, i)
            exit()
        else:
            L[si] = i
    print(-1, -1)


if __name__ == "__main__":
    main()
