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
    N, K = NMI()
    A = NLI()
    graph = [(i+A[i])%N for i in range(N)]
    vs = {0}
    vl = [0]
    nums = [0]

    for i in range(N):
        now = vl[-1]
        goto = graph[now]
        vl.append(goto)
        nums.append(nums[-1] + A[now])
        if goto in vs:
            start = vl.index(goto)
            end = i+1
            break

        vs.add(goto)

    # print(vs)
    # print(vl)
    # print(nums)
    # print(start, end)

    if K <= end:
        print(nums[K])
        exit()

    loop_n = end - start
    loop = nums[end] - nums[start]
    ans = nums[start]
    K -= start
    ans += (K // loop_n) * loop
    K = K % loop_n
    ans += nums[start + K] - nums[start]
    print(ans)


if __name__ == "__main__":
    main()
