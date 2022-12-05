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
EI = lambda m: [NLI() for _ in range(m)]


class Node:
    def __init__(self, val, _prev, _next):
        self.val = val
        self.prev = _prev
        self.next = _next

    def __str__(self):
        return str([self.val, self.prev, self.next])


class LinkedList:
    def __init__(self):
        self.D = [Node("TOP", 0, 1), Node("BOTTOM", 0, 1)]
        self.top = 0
        self.bottom = 1
        self.mid = 0
        self.len = 0

    def append(self, val):
        b_idx = self.bottom
        B = self.D[self.bottom]
        p_idx = B.prev
        P = self.D[p_idx]
        new_idx = len(self.D)
        self.D.append(Node(val, p_idx, b_idx))
        B.prev = new_idx
        P.next = new_idx
        if self.len % 2 == 0:
            self.mid = self.D[self.mid].next
        self.len += 1

    def insert_mid(self, val):
        p_idx = self.mid
        P = self.D[p_idx]
        b_idx = P.next
        B = self.D[b_idx]

        new_idx = len(self.D)
        if self.len % 2 == 0:
            self.mid = new_idx
        self.D.append(Node(val, p_idx, b_idx))
        B.prev = new_idx
        P.next = new_idx

        self.len += 1

    def popleft(self):
        t_idx = self.top
        T = self.D[t_idx]
        X = self.D[T.next]
        b_idx = X.next
        B = self.D[b_idx]
        T.next = b_idx
        B.prev = t_idx

        if self.len == 1:
            self.mid = 0
        elif self.len % 2 == 0:
            self.mid = self.D[self.mid].next

        self.len -= 1

    def front(self):
        t_idx = self.top
        T = self.D[t_idx]
        X = self.D[T.next]
        assert X.val != "BOTTOM"
        return X.val


    def __str__(self):
        res = [self.D[0]]
        now = 0
        while now != 1:
            now = res[-1].next
            res.append(self.D[now])
        res = [str(node) for node in res]

        return str(self.mid) + str(res)


def main():
    Q = NI()
    querys = [SLI() for _ in range(Q)]
    L = LinkedList()
    for q, *X in querys:
        # print(q, X)
        if q == "A":
            L.append(X[0])
        elif q == "B":
            L.insert_mid(X[0])
        elif q == "C":
            L.popleft()
        else:
            print(L.front())
        # print(L)



if __name__ == "__main__":
    main()

