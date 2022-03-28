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
    S = SI()

    if "UTPC" in S:
        print(0)
        exit()

    ans = 100000
    for i in range(N-3):
        tmp = 0

        now = list(S[i:i+4])
        for j, s in enumerate("UTPC"):
            if now[j] == s:
                continue

            for k in range(j+1, 4):
                if now[k] == s and now[j] == "UTPC"[k]:
                    now[j], now[k] = now[k], now[j]
                    tmp += 1
                    break

            if now[j] == s:
                continue

            for k in range(j+1, 4):
                if now[k] == s:
                    now[j], now[k] = now[k], now[j]
                    tmp += 1
                    break

            if now[j] == s:
                continue

            now[j] = s
            tmp += 1

            # print(now, tmp)

        ans = min(ans, tmp)


    S = S[::-1]
    for i in range(N-3):
        tmp = 0

        now = list(S[i:i+4])
        for j, s in enumerate("CPTU"):
            if now[j] == s:
                continue

            for k in range(j+1, 4):
                if now[k] == s and now[j] == "CPTU"[k]:
                    now[j], now[k] = now[k], now[j]
                    tmp += 1
                    break

            if now[j] == s:
                continue

            for k in range(j+1, 4):
                if now[k] == s:
                    now[j], now[k] = now[k], now[j]
                    tmp += 1
                    break

            if now[j] == s:
                continue

            now[j] = s
            tmp += 1

            # print(now, tmp)

        ans = min(ans, tmp)

    assert ans <= 4
    print(ans)


if __name__ == "__main__":
    main()
