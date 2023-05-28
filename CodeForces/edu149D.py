import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        S = SI()
        ans1 = [0] * N
        ans2 = [0] * N

        def f(ans, rev=False):
            if rev:
                x = ")"
                y = "("
                c = 2
            else:
                x = "("
                y = ")"
                c = 1

            D = deque()
            for i in range(N):
                if ans[i] != 0:
                    continue

                if S[i] == x:
                    D.append(i)
                elif len(D) > 0:
                    l = D.pop()
                    ans[l] = c
                    ans[i] = c
                else:
                    continue

        f(ans1, False)
        f(ans1, True)

        f(ans2, True)
        f(ans2, False)

        if min(ans1) == 0 and min(ans2) == 0:
            print(-1)
            continue
        elif min(ans1) == 0:
            ans = ans2
        elif min(ans2) == 0:
            ans = ans1
        else:
            if len(set(ans1)) > len(set(ans2)):
                ans = ans2
            else:
                ans = ans1

        if len(set(ans)) == 1:
            ans = [1] * N
        print(len(set(ans)))
        print(*ans)


if __name__ == "__main__":
    main()
