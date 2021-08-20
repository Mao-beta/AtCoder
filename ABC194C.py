import sys
import math
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = NLI()
    C = Counter(A)
    ans = 0
    for a, m in C.items():
        for b, n in C.items():
            ans += (a-b)**2 * m * n
    print(ans // 2)


if __name__ == "__main__":
    main()
