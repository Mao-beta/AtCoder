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
    S = SI()
    R = runLengthEncode(S)

    X = []
    if R[0][0] == "1":
        X.append(["0", R[0][1]])

    if R[-1][0] != "1":
        R.append(("1", 0))

    for i in range(len(R)-1):
        if R[i][0] != "1" and R[i+1][0] != "1":
            print(-1)
            exit()

        if R[i][0] != "1":
            X.append([R[i][0], R[i+1][1]])

    # print(X)

    ans = 0
    now = 0
    prev_s = 1

    for i, (s, x) in enumerate(X[::-1]):
        z = prev_s - 1
        peak = x + now * z
        ans += peak + 1
        now += peak + 1
        ans %= MOD99
        now %= MOD99
        prev_s = int(s)

    if X[0][0] == "0":
        ans -= 1
    print((ans-1) % MOD99)


if __name__ == "__main__":
    main()
