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


from typing import List
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str):
    grouped = groupby(S)
    res = deque()
    for k, v in grouped:
        res.append([k, int(len(list(v)))])
    return res


def main():
    S = SI()
    R = runLengthEncode(S)
    ans = []
    cnt = 0
    while len(R) >= 2:
        if R[0][0] == "0":
            ans.append(R.popleft())
            continue
        if R[0][1] % 2:
            R[0][1] -= 1
            ans.append(["1", 1])
            continue
        s, k = R.popleft()
        cnt += k // 2 * R[0][1]
        ans.append(R.popleft())
        if R:
            R[0][1] += k
        else:
            ans.append([s, k])
    if R:
        ans.append(R.popleft())
    print(cnt)


if __name__ == "__main__":
    main()
