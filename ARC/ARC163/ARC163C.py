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
    ans = [set()]

    for i in range(1, 501):
        if i == 1:
            ans.append({1,})
        elif i == 2:
            ans.append(set())
        elif i == 3:
            ans.append({2, 3, 6})
        else:
            S = sorted(list(ans[-1]))
            for s in S:
                x, y = s+1, s*(s+1)
                if x not in S and y not in S:
                    SS = ans[-1] | {x, y}
                    SS.discard(s)
                    break
            ans.append(SS)

    for _ in range(T):
        N = NI()
        A = ans[N]
        if len(A) == 0:
            print("No")
        else:
            print("Yes")
            print(*A)


if __name__ == "__main__":
    main()
