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


class KindDeque():
    """
    D = KindDeque()
    D.kindで種類数を、len(D)で長さを、
    D.Cで中身のkeyごとの個数（要はCounterのような辞書）を
    O(1)で取ってこれるdeque
    """
    def __init__(self):
        self.D = deque()
        self._k = 0
        self.C = defaultdict(int)

    @property
    def kind(self):
        return self._k

    def __len__(self):
        return len(self.D)

    def append(self, x):
        self.D.append(x)
        if self.C[x] == 0:
            self._k += 1
        self.C[x] += 1

    def appendleft(self, x):
        self.D.appendleft(x)
        if self.C[x] == 0:
            self._k += 1
        self.C[x] += 1

    def pop(self):
        x = self.D.pop()
        self.C[x] -= 1
        if self.C[x] == 0:
            self._k -= 1

    def popleft(self):
        x = self.D.popleft()
        self.C[x] -= 1
        if self.C[x] == 0:
            self._k -= 1


def main():
    N, M = NMI()
    AB = EI(N)
    M2X = [[] for _ in range(M+1)]
    for i, (a, b) in enumerate(AB):
        M2X[a].append(i)
        M2X[b].append(i)

    imos = [0] * (M+2)
    D = KindDeque()
    r = 1
    for l in range(1, M+1):
        for x in M2X[l-1]:
            D.popleft()

        while r < M+1 and D.kind < N:
            for x in M2X[r]:
                D.append(x)
            r += 1
        if D.kind >= N:
            # print(l, r)
            if r-l < M+2-l:
                imos[r-l] += 1
                imos[M+2-l] -= 1

        # print(l, r, D.C, D.D)
        # print(M2X[l])

    ans = list(accumulate(imos))[1:-1]
    print(*ans)


if __name__ == "__main__":
    main()
