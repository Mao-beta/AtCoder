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
    N, M = NMI()
    ABC = EI(M)
    E = [[] for _ in range(N+1)]
    for a, b, c in ABC:
        E[c].append([a, b])

    kouho = [0] * (N+1)
    fixed = [0] * (N+1)
    pairs = [0] * (N+1)
    maxes = [N] * (N+1)

    for c in range(N, 0, -1):
        # print(c, E[c])
        Cnt = Counter()

        # もう決まってるのが出たらダメ
        for a, b in E[c]:
            maxes[a] = c
            maxes[b] = c
            if fixed[a] > 0 or fixed[b] > 0:
                print(0)
                return

        for a, b in E[c]:
            Cnt[a] += 1
            Cnt[b] += 1

        multi = set()
        for x, k in Cnt.items():
            if k > 1:
                multi.add(x)

        c_fixed = False

        # 複数票得ている頂点が複数あったらダメ
        if len(multi) > 1:
            print(0)
            return
        # 1つだけならそれ確定
        if multi:
            m = multi.pop()

            x = m
            if kouho[x] > c:
                kouho[x] = 0
                p = pairs[x]
                fixed[p] = kouho[p]
                kouho[p] = 0

            fixed[m] = c
            kouho[m] = 0
            for a, b in E[c]:
                # 確定した点を含まない辺があればダメ
                if a != m and b != m:
                    print(0)
                    return
                x = a if a != m else b
                if kouho[x] > c:
                    kouho[x] = 0
                    p = pairs[x]
                    fixed[p] = kouho[p]
                    kouho[p] = 0

        else:
            # 重複点がないのに辺が複数あったらダメ
            if len(E[c]) > 1:
                print(0)
                return
            for a, b in E[c]:
                if kouho[a] > c:
                    kouho[a] = 0
                    p = pairs[a]
                    fixed[p] = kouho[p]
                    kouho[p] = 0
                else:
                    kouho[a] = c
                    pairs[a] = b

                if kouho[b] > c:
                    kouho[b] = 0
                    p = pairs[b]
                    fixed[p] = kouho[p]
                    kouho[p] = 0
                else:
                    kouho[b] = c
                    pairs[b] = a


        # print("kouho", *kouho, sep="\t")
        # print("fixed", *fixed, sep="\t")
        # print("pairs", *pairs, sep="\t")
        # print("maxes", *maxes, sep="\t")

    ans = 1
    for i in range(1, N+1):
        if kouho[i] > 0:
            ans *= 2
            fixed[i] = kouho[i]
            kouho[i] = 0
            kouho[pairs[i]] = 0

    # print("kouho", *kouho, sep="\t")
    # print("fixed", *fixed, sep="\t")
    # print("pairs", *pairs, sep="\t")
    # print("maxes", *maxes, sep="\t")

    Ks = [0] * (N+1)
    used = set()
    for i in range(1, N+1):
        used.add(fixed[i])
        if fixed[i] == 0:
            Ks[maxes[i]] += 1

    # print(Ks)
    # print(used)
    now = 0
    for i in range(N, 0, -1):
        now += Ks[i]
        if i in used:
            continue
        if now <= 0:
            print(0)
            return

        ans = ans * now % MOD99
        # print(i, now, ans)
        now -= 1
        used.add(i)

    if now > 0:
        print(0)
        return

    print(ans)


if __name__ == "__main__":
    main()
