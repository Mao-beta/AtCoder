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
    B = NLI()
    C = NLI()
    BC = [B[c-1] for c in C]

    A = Counter(A)
    BC = Counter(BC)

    ans = 0
    for a, k in A.items():
        ans += k * BC[a]
    print(ans)


if __name__ == "__main__":
    main()
