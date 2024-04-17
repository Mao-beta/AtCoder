import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


from typing import List
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main():
    N = NI()
    LR = EI(N)
    for i in range(N-1):
        li, ri = LR[i]
        lj, rj = LR[i+1]
        if ri < lj or rj < li:
            continue
        LR[i+1] = [max(li, lj), min(ri, rj)]

    print(*LR, sep="\n")
    print()

    for i in range(N-1, 0, -1):
        li, ri = LR[i]
        lj, rj = LR[i-1]
        if ri < lj or rj < li:
            continue
        LR[i-1] = [max(li, lj), min(ri, rj)]

    print(*LR, sep="\n")

    ans = [0] * N
    R = runLengthEncode(LR)
    print(*R, sep="\n")

    if len(R) == 1:
        ans = [R[0][0][0]] * N
        print(*ans)
        return

    now = 0
    for i in range(len(R)):
        if i < len(R)-1:
            (l1, r1), k1 = R[i]
            (l2, r2), k2 = R[i + 1]
            if l1 < l2:
                for j in range(k1):
                    ans[now+j] = r1
            else:
                for j in range(k1):
                    ans[now+j] = l1
        else:
            (l1, r1), k1 = R[i]
            (l2, r2), k2 = R[i-1]
            if l1 < l2:
                for j in range(k1):
                    ans[now+j] = r1
            else:
                for j in range(k1):
                    ans[now+j] = l1
        now += k1

    print(*ans)


if __name__ == "__main__":
    main()
