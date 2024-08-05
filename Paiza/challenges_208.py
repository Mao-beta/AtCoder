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
    N, M, K = NMI()
    S = [list(SI()) for _ in range(N)]

    C = [0] * 10
    for h in range(N):
        for w in range(N):
            if S[h][w] != ".":
                C[int(S[h][w])] += 1

    ans = []
    rem = set(range(1, K+1))
    for i in range(K):
        def check(sh, sw):
            res = set()
            RC = [0] * 10
            for h in range(sh, sh+M):
                for w in range(sw, sw+M):
                    res.add(S[h][w])
                    if S[h][w] != ".":
                        RC[int(S[h][w])] += 1
            if len(res) > 2:
                return -1
            elif len(res) == 1:
                x = res.pop()
                if x == ".":
                    return -1
                elif x == "0":
                    return 0
                else:
                    return int(x)
            else:
                if "." in res:
                    return -1
                elif "0" in res:
                    res.discard("0")
                    x = int(res.pop())
                    if RC[x] != C[x]:
                        return -1
                    return int(x)
                else:
                    return -1

        def search():
            free = []
            for sh in range(N-M+1):
                for sw in range(N-M+1):
                    x = check(sh, sw)
                    if x == -1:
                        continue
                    if x > 0:
                        return x, sh, sw
                    if x == 0 and len(free) == 0:
                        free = [sh, sw]
            return 0, *free

        x, sh, sw = search()
        # print(x, sh, sw)
        if x > 0:
            rem.discard(x)
        else:
            x = rem.pop()

        ans.append([x, sw+1, sh+1])
        for h in range(sh, sh + M):
            for w in range(sw, sw + M):
                S[h][w] = "0"

        # for row in S:
        #     print(*row, sep="")
        # print()

    for c, x, y in ans[::-1]:
        print(c, x, y)


if __name__ == "__main__":
    main()
