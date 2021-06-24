import sys
import math
from collections import Counter
from itertools import accumulate

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
    for i, a in enumerate(A):
        if i % 2 == 1:
            A[i] = -a

    C = Counter(accumulate(A))
    C[0] += 1
    ans = 0
    for _, n in C.items():
        ans += n * (n-1) // 2
    print(ans)


if __name__ == "__main__":
    main()
