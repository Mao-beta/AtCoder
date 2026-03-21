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


from typing import List
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "deque[list[str, int]]":
    grouped = groupby(S)
    res = deque()
    for k, v in grouped:
        res.append([k, int(len(list(v)))])
    return res


def main():
    S = SI()
    T = SI()
    RS = runLengthEncode(S)
    RT = runLengthEncode(T)
    ans = 0
    while RS and RT:
        if RS[0][0] == "A" and RT[0][0] == "A":
            ans += abs(RS[0][1] - RT[0][1])
            RS.popleft()
            RT.popleft()
        elif RS[0][0] == "A":
            ans += RS[0][1]
            RS.popleft()
        elif RT[0][0] == "A":
            ans += RT[0][1]
            RT.popleft()
        else:
            if RS[0][0] != RT[0][0]:
                print(-1)
                return
            else:
                if RS[0][1] == RT[0][1]:
                    RS.popleft()
                    RT.popleft()
                elif RS[0][1] > RT[0][1]:
                    RS[0][1] -= RT[0][1]
                    RT.popleft()
                else:
                    RT[0][1] -= RS[0][1]
                    RS.popleft()
    if len(RS) > 1 or len(RT) > 1:
        print(-1)
        return
    if RS:
        if RS[0][0] == "A":
            ans += RS[0][1]
        else:
            print(-1)
            return
    if RT:
        if RT[0][0] == "A":
            ans += RT[0][1]
        else:
            print(-1)
            return
    print(ans)


if __name__ == "__main__":
    main()
