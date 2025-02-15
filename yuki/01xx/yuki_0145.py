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


def main():
    N = NI()
    S = SI()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    D = {}
    V = [0] * 26
    v = 0
    for i, a in enumerate(alphabets):
        D[a] = i
        if a == "i": # 1
            v += 1
        elif a == "j": # 2
            v += 1
        elif a == "k": # 3
            v += 1
        elif a == "l": # 4
            v += 1
        elif a == "u": # 5
            v += 1
        elif a == "v": # 6
            v += 1
        elif a == "y": # 7
            v += 1
        elif a == "z": # 8
            v += 1
        V[i] = v

    S = [V[D[s]] for s in S]
    C = Counter(S)
    print(sorted(C.items()))
    ans = C[8]
    tmp = C[7]
    if C[6] >= tmp:
        ans += tmp
        tmp = 0
    else:
        ans += C[6]
        tmp -= C[6]

    print(ans, tmp)

    if C[5] >= tmp:
        g = C[5] - tmp
        C[4] += g
    else:
        g = tmp - C[5]
        ans += g // 2
        tmp -= g
        if tmp >= g % 2:
            ans += g % 2
            tmp -= g % 2

    print(ans, tmp)

    if C[4] >= tmp:
        ans += tmp
        tmp = 0
    else:
        ans += C[4]
        tmp -= C[4]

    print(ans, tmp)

    if C[3] >= tmp:
        g = C[3] - tmp
        C[2] += g
    else:
        g = tmp - C[3]
        ans += g // 2
        tmp -= g
        if tmp >= g % 2:
            ans += g % 2
            tmp -= g % 2

    print(ans, tmp)

    if C[2] >= tmp:
        ans += tmp
        tmp = 0
    else:
        ans += C[2]
        tmp -= C[2]

    print(ans, tmp)

    if C[1] >= tmp:
        g = C[1] - tmp
        C[0] += g
    else:
        g = tmp - C[1]
        ans += g // 2
        tmp -= g
        if tmp >= g % 2:
            ans += g % 2
            tmp -= g % 2

    print(ans, tmp)

    if C[0] >= tmp:
        ans += tmp
        tmp = 0
    else:
        ans += C[0]
        tmp -= C[0]

    print(ans, tmp)

    if tmp > 1:
        ans += tmp // 2

    print(ans)


if __name__ == "__main__":
    main()
