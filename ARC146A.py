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


def main():
    N = NI()
    A = NLI()
    D = defaultdict(list)
    Ks = []
    for a in A:
        D[len(str(a))].append(a)
        Ks.append(len(str(a)))

    for k in D.keys():
        D[k].sort(reverse=True)

    Ks.sort()
    ka, kb, kc = Ks[-1], Ks[-2], Ks[-3]
    ans = 0

    for kp in permutations([ka, kb, kc], 3):
        tmp = ""
        idx = [0] * 7
        for k in kp:
            tmp += str(D[k][idx[k]])
            idx[k] += 1
        ans = max(ans, int(tmp))

    print(ans)



if __name__ == "__main__":
    main()
