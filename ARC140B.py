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


from typing import List
from itertools import groupby

def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main():
    N = NI()
    S = SI()
    S = runLengthEncode(S)
    A = []
    now = 0
    ok = False
    for i in range(len(S)-2):
        if S[i][0] == "A" and S[i+1][0] == "R" and S[i+2][0] == "C":
            if S[i+1][1] == 1:
                A.append(min(S[i][1], S[i+2][1]))

    ans = 0

    ones = 0
    heapify(A)
    while A:
        a = heappop(A)
        # print(a, ones)
        if a == 1:
            ones += 1
            continue

        # print("ans", ans, A, ones)

        if ans % 2 == 0:
            ans += 1
            if a > 2:
                heappush(A, a-1)
            else:
                ones += 1

        else:
            if ones > 0:
                ans += 1
                ones -= 1
                heappush(A, a)
            else:
                ans += 1

    # print(ones)
    print(ans + ones)

# 20
# AAAARCCCCAARCCARC


if __name__ == "__main__":
    main()
