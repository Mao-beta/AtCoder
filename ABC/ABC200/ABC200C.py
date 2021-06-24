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
    A = [a%200 for a in A]
    C = Counter(A)
    ans = 0
    for x, n in C.items():
        ans += (n-1) * n // 2
    print(ans)


if __name__ == "__main__":
    main()
