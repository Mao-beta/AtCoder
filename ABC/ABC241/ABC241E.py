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

if "PyPy" in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def _main():
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


class Doubling:
    def __init__(self, D, M=60):
        """Dが1回の遷移、2^M回までのダブリング表"""
        self.M = M
        self.D = [D]
        for m in range(self.M):
            tmp = []
            for i in range(len(D)):
                j = self.D[-1][i]
                tmp.append(self.D[-1][j])
            self.D.append(tmp)

    def pow(self, K):
        """ダブリング遷移DをもとにK回後の遷移先を求める"""
        now = 0
        for m in range(self.M):
            if (K >> m) & 1:
                now = self.D[m][now]

        return now


def main():
    N, K = NMI()
    A = NLI()

    M = 40
    # D[m][i]: XmodN = i のときの2^m回後の行き先
    D = [[0]*N for _ in range(M+1)]
    X = [[0]*N for _ in range(M+1)]

    for i, a in enumerate(A):
        D[0][i] = (i + A[i]) % N
        X[0][i] = A[i]

    for m in range(M):
        for i in range(N):
            # 2^m回後の行先
            g = D[m][i]
            # 2^m回後の行先
            D[m+1][i] = D[m][g]
            X[m+1][i] = X[m][i] + X[m][g]

    # print(*X, sep="\n")
    ans = 0
    now = 0
    for m in range(M):
        if (K >> m) & 1:
            ans += X[m][now]
            now = D[m][now]
    print(ans)


if __name__ == "__main__":
    main()
