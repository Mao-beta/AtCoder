import sys
import math
from collections import Counter

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    S = []
    for _ in range(N):
        S.append(SI())
    C = Counter(S)
    print(C.most_common()[0][0])


if __name__ == "__main__":
    main()
