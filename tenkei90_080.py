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
    N, D = NMI()
    A = NLI()

    ans = 0

    for j in range(1<<N):
        nj = 0
        cond = 0
        for i in range(N):
            if (j>>i) & 1: continue
            a = A[i]
            nj |= a
            cond += 1

        free = D - bin(nj).count("1")
        if cond % 2:
            ans -= 1 << free
        else:
            ans += 1 << free

    print(ans)


if __name__ == "__main__":
    main()
