import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N, M = NMI()
    UV = EI(M)
    Q = NI()
    QAB = EI(Q)
    UV = [[x-1, y-1] for x, y in UV]
    QAB = [[x, y-1, w-1] for x, y, w in QAB]
    # 公開非公開が変わりうるaiのみ管理
    # aについて、Fopen, Fcloseを管理
    # open + len(Fclose_ai)を答える
    As = set(a for _, a, _ in QAB)
    Fopen = defaultdict(set)
    Fclose = defaultdict(set)
    is_closed = defaultdict(bool)
    open_num = N
    for u, v in UV:
        if u in As and v in As:
            Fopen[u].add(v)
    for q, a, b in QAB:
        if q == 1:
            if b not in As:
                pass
            elif is_closed[b]:
                if b in Fclose[a]:
                    Fclose[a].discard(b)
                else:
                    Fclose[a].add(b)
            else:
                if b in Fopen[a]:
                    Fopen[a].discard(b)
                else:
                    Fopen[a].add(b)

        else:
            if is_closed[a]:
                for u in As:
                    if a in Fclose[u]:
                        Fclose[u].discard(a)
                        Fopen[u].add(a)
                open_num += 1
            else:
                for u in As:
                    if a in Fopen[u]:
                        Fopen[u].discard(a)
                        Fclose[u].add(a)
                open_num -= 1

            is_closed[a] = not is_closed[a]

        # print(open_num, len(Fclose[a]), Fopen, Fclose)
        # print(q, a, b)
        print(open_num + len(Fclose[a]) - int(not is_closed[a]))


if __name__ == "__main__":
    main()
