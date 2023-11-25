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
    N, K = NMI()
    A = NLI()
    Arev = [N] * (N+1)
    for i, a in enumerate(A):
        Arev[a] = i
    S = set(range(1, N+1))

    now = 0
    for i in range(N):
        ok = False
        ai = A[i]
        L = sorted(list(S))

        # aiより小さいものは1通り
        for x in L:
            if x >= ai:
                break
            now += 1
            if now == K:
                # 解決処理
                r = Arev[x] + 1
                A[i:r] = A[i:r][::-1]
                ok = True

        if ok:
            break

        # aiが採用されるか？
        tmp = (N-1-i) * (N-2-i) // 2 + N
        # print(now, tmp, K)
        if now + tmp > K:
            # 採用
            S.discard(ai)
        else:
            # 非採用
            now += tmp
            # aiより大きいものは1通り
            for x in L:
                if x <= ai:
                    continue
                now += 1
                if now == K:
                    # 解決処理
                    r = Arev[x] + 1
                    A[i:r] = A[i:r][::-1]
                    ok = True

        if ok:
            break

    print(*A)



if __name__ == "__main__":
    main()
