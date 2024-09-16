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
    N, K = NMI()
    A = NLI()
    C = [0] + list(accumulate(A+A))
    SA = sum(A)
    W = 0
    ans = 0
    best = set()
    for i in range(N):
        if i in best:
            continue
        def judge(X):
            used = set()
            idx = i
            used.add(i)
            k = 0
            while k < K:
                nidx = bisect.bisect_left(C, C[idx]+X)
                k += 1
                used.add(nidx % N)
                idx = nidx
                if idx > i+N:
                    return False, None

            return True, used

        ok = 0
        ng = SA // K + 1
        while abs(ok - ng) > 1:
            X = (ok + ng) // 2
            j, used = judge(X)
            if j:
                ok = X
            else:
                ng = X

        j, used_ok = judge(ok)
        if ok > W:
            W = ok
            best = used_ok
        elif ok == W:
            best |= used_ok
        else:
            continue

    print(W, N - len(best))


if __name__ == "__main__":
    main()
