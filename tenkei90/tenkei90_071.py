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
    N, M, K = NMI()
    AB = [NLI() for _ in range(M)]
    G = [[] for _ in range(N)]
    dims = [0] * N
    for a, b in AB:
        a, b = a-1, b-1
        dims[b] += 1
        G[a].append(b)

    # いま進める点
    state = [i for i, d in enumerate(dims) if d == 0]
    # 順序
    perm = []
    ans = []

    def rec():
        # print(perm)
        # print("s", state)
        if len(perm) == N:
            ans.append(perm[:])
            if len(ans) == K:
                for a in ans:
                    print(*a)
                exit()

            return

        if len(state) == 0:
            print(-1)
            exit()

        for i in range(min(len(state), K)):
            now = state[i]

            del state[i]

            for goto in G[now]:
                dims[goto] -= 1
                if dims[goto] == 0:
                    state.append(goto)

            perm.append(now+1)
            rec()
            perm.pop()

            for goto in reversed(G[now]):
                if dims[goto] == 0:
                    state.pop()
                dims[goto] += 1

            state.insert(i, now)

        return

    rec()
    # print(*ans, sep="\n")
    print(-1)


if __name__ == "__main__":
    main()
