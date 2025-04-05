import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
from random import randint

sys.set_int_max_str_digits(10 ** 6)
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
    N, L = NMI()
    T = NLI()
    import time
    START = time.time()

    TI = [[t, i] for i, t in enumerate(T)]
    TI.sort(reverse=True)
    I2V = [0] * N
    V2I = [0] * N
    for v, (t, i) in enumerate(TI):
        I2V[i] = v
        V2I[v] = i

    from random import randint

    def simulate(AB):
        C = [0] * N
        now = 0
        for _ in range(L):
            a, b = AB[now]
            C[now] += 1
            if C[now] % 2:
                goto = a
            else:
                goto = b
            now = goto
        res = sum(abs(c-t) for c, t in zip(C, T))
        return 10**6 - res

    ans = [[V2I[(I2V[i]+1)%N], randint(0, N-1)] for i in range(N)]
    best_score = simulate(ans)

    while time.time() - START < 1.8:
        # 1本変更、1本反転、2本入れ替えなど？
        # 1本変更
        t = randint(0, N-1)
        nb = randint(0, N-1)
        ob = ans[t][1]
        ans[t][1] = nb
        score = simulate(ans)
        if score > best_score:
            best_score = score
        else:
            ans[t][1] = ob
        # print(best_score, score)

    for a, b in ans:
        print(a, b)


if __name__ == "__main__":
    main()
