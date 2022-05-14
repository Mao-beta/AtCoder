import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a - 1, b - 1
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    N, M = NMI()
    UV = [NLI() for _ in range(M)]
    graph = adjlist_nond_1to0(N, UV)
    S = SI()

    seen = [0] * N
    pars = [-1] * N
    pars[0] = N
    ans = []

    def rec(now):
        seen[now] ^= 1
        # print(now+1)
        ans.append(now+1)
        for goto in graph[now]:
            if pars[goto] == -1:
                pars[goto] = now
                rec(goto)

        if now == 0:
            return seen[now] == int(S[now])

        if seen[now] != int(S[now]):
            # print(now, pars[now])
            ans.append(pars[now]+1)
            ans.append(now+1)
            ans.append(pars[now]+1)
        else:
            ans.append(pars[now]+1)
            seen[pars[now]] ^= 1
        # print(now+1)

    flag = rec(0)
    if flag:
        print(len(ans))
        print(*ans)
    else:
        print(len(ans)-1)
        print(*ans[:-1])


if __name__ == "__main__":
    main()
