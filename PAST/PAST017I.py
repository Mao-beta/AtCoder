import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N = NI()
    S = [SI() for _ in range(N)]
    C = Counter(S)
    ans = 0
    for s in S:
        T = set()
        for case in range(1, 1<<len(s)):
            t = []
            for i in range(len(s)):
                if (case >> i) & 1:
                    t.append(s[i])
            t = "".join(t)
            if t in T:
                continue
            ans += C[t]
            T.add(t)
    print(ans)


if __name__ == "__main__":
    main()
