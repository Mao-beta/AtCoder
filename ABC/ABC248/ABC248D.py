import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main():
    N = NI()
    A = NLI()
    Q = NI()
    LRX = [NLI() for _ in range(Q)]
    root = int(N**0.5+1)
    B = N // root + 1
    C = [[0]*B for _ in range(N+1)]

    for i, a in enumerate(A):
        bucket = i // root
        C[a][bucket] += 1

    # print(root)
    # print(*C, sep="\n")

    for l, r, x in LRX:
        l -= 1
        if r - l <= root:
            ans = 0
            for i in range(l, r):
                if A[i] == x:
                    ans += 1
            print(ans)

        else:
            ans = 0
            bl = l // root
            br = r // root

            if l % root:
                for i in range(l, (l//root + 1) * root):
                    # print(i)
                    if A[i] == x:
                        ans += 1
                bl += 1
            if r % root:
                for i in range(r//root * root, r):
                    # print(i)
                    if A[i] == x:
                        ans += 1

            ans += sum(C[x][bl: br])
            print(ans)
            # print("###")


if __name__ == "__main__":
    main()
