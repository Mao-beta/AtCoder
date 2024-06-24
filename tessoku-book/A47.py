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


def donyoku():
    N = 20
    T = NI()
    PQR = [NLI() for _ in range(T)]
    PQR = [[p-1, q-1, r-1] for p, q, r in PQR]

    X = [0] * N


    def add_k(p, q, r, k):
        X[p] += k
        X[q] += k
        X[r] += k

    def count_zero():
        return X.count(0)


    def abs_error():
        return sum([abs(x) for x in X])


    score = 0
    ans = []
    for pqr in PQR:
        add_k(*pqr, 1)
        error_a = abs_error()
        new_a = count_zero()
        add_k(*pqr, -2)
        error_b = abs_error()
        new_b = count_zero()

        if error_a < error_b:
            add_k(*pqr, 2)
            score += new_a
            ans.append("A")
        else:
            score += new_b
            ans.append("B")

        # print(score)
        # print(X)

    print("\n".join(ans))


class Query:
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r

    def __repr__(self):
        return f"Query(p={self.p}, q={self.q}, r={self.r})"


class State:
    def __init__(self, t=0, score=0, X=None, last_hand=".", last_idx=-1):
        self.t = t
        self.N = 20
        self.score = score
        self.X = X if X else [0]*self.N
        self.last_hand = last_hand
        self.last_idx = last_idx

    def action(self, last_idx: int, s: str, query: Query) -> "State":
        if s == "A":
            X = self.X[:]
            X[query.p] += 1
            X[query.q] += 1
            X[query.r] += 1
            ns = self.score + get_score(X)
            return State(self.t+1, ns, X, "A", last_idx)

        else:
            X = self.X[:]
            X[query.p] -= 1
            X[query.q] -= 1
            X[query.r] -= 1
            ns = self.score + get_score(X)
            return State(self.t+1, ns, X, "B", last_idx)

    def __repr__(self):
        return f"State(t={self.t}, score={self.score}, from {self.last_idx} by {self.last_hand})"


def get_score(X):
    return X.count(0)


def main():
    T = NI()
    N = 20
    PQR = [NLI() for _ in range(T)]
    PQR = [Query(p-1, q-1, r-1) for p, q, r in PQR]

    Beam = [[] for _ in range(T+1)]
    Beam[0].append(State())

    WIDTH = 10000

    for t in range(T):
        query = PQR[t]

        for si, state in enumerate(Beam[t]):
            Beam[t+1].append(state.action(si, "A", query))
            Beam[t+1].append(state.action(si, "B", query))

        Beam[t+1].sort(key=lambda s: -s.score)
        Beam[t+1] = Beam[t+1][:WIDTH]

    idx = 0
    ans = []
    for t in range(T, 0, -1):
        state = Beam[t][idx]
        ans.append(state.last_hand)
        idx = state.last_idx

    ans = ans[::-1]
    print("\n".join(ans))


if __name__ == "__main__":
    main()
