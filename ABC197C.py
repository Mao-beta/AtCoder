import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    A = NLI()
    ans = 2**40
    for case in range(1<<N):
        L = []
        now_bit = -1
        now_or = 0
        for i, a in enumerate(A):
            if (case>>i)&1 != now_bit:
                if i != 0:
                    L.append(now_or)
                now_or = a
                now_bit = (case>>i)&1
            else:
                now_or = now_or | a
        L.append(now_or)
        res = L[0]
        for l in L:
            res = res ^ l
        res = res ^ L[0]
        ans = min(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
