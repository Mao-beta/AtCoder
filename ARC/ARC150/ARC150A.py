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

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main(N, K, S):
    R = runLengthEncode(S)

    if "1" not in S:
        cnt = 0
        for s, k in R:
            if s == "?" and k == K:
                cnt += 1
            if s == "?" and k > K:
                print("No")
                return
        if cnt == 1:
            print("Yes")
        else:
            print("No")

    else:
        l = S.index("1")
        r = S.rindex("1")
        # print(l, r)

        if r - l + 1 > K:
            print("No")
            return

        for i in range(l, r+1):
            if S[i] == "0":
                print("No")
                return

        if r - l + 1 == K:
            print("Yes")
            return

        i = l-1
        ll = l
        while i >= 0:
            if S[i] == "0":
                break
            ll = i
            i -= 1

        i = r+1
        rr = r
        while i < N:
            if S[i] == "0":
                break
            rr = i
            i += 1

        # print(ll, rr)
        if ll == l or rr == r:
            if rr - ll + 1 >= K:
                print("Yes")
            else:
                print("No")
            return

        else:
            if rr - ll + 1 == K:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    T = NI()
    for _ in range(T):
        # K = random.randint(0, N)
        # S = ["01?"[random.randint(0, 2)] for _ in range(N)]
        # S = "".join(S)
        # print(N, K, S)
        N, K = NMI()
        S = SI()
        main(N, K, S)
