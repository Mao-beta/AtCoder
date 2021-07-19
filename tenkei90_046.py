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
    A = Counter([x % 46 for x in NLI()])
    B = Counter([x % 46 for x in NLI()])
    C = Counter([x % 46 for x in NLI()])

    ans = 0
    for a, x in A.items():
        for b, y in B.items():
            c = (46 - a - b) % 46
            z = C[c]
            ans += x * y * z

    print(ans)


if __name__ == "__main__":
    main()
