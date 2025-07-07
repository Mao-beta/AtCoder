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
    Q = NI()
    # [childs, val, x?]
    trie = [[] for _ in range(26)] + [0, 0]
    # print(trie)

    for _ in range(Q):
        T, S = SMI()
        T = int(T)
        S = [ord(s)-ord("a") for s in S]
        # print(T, S)

        if T == 1:
            is_x = False
            now = trie
            for s in S:
                # print(s, trie)
                if len(now[s]) == 0:
                    now[s] = [[] for _ in range(26)] + [0, 0]
                    now = now[s]
                else:
                    if now[s][-1] == 1:
                        is_x = True
                        break
                    else:
                        now = now[s]

            if not is_x:
                now[-1] = 1
                v = now[-2]
                now = trie
                now[-2] -= v
                for s in S:
                    now = now[s]
                    now[-2] -= v

        else:
            is_x = False
            now = trie
            for s in S:
                if len(now[s]) == 0:
                    now[s] = [[] for _ in range(26)] + [0, 0]
                    now = now[s]
                else:
                    if now[s][-1] == 1:
                        is_x = True
                        break
                    else:
                        now = now[s]
            # print(is_x)
            if not is_x:
                now = trie
                now[-2] += 1
                for s in S:
                    now = now[s]
                    now[-2] += 1

        print(trie[-2])


if __name__ == "__main__":
    main()
