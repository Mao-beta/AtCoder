import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


from operator import itemgetter

class Mo:

    def __init__(self, ls):
        from math import sqrt, ceil
        self.ls = ls.copy()
        self.n = len(ls)
        self.b = ceil(sqrt(self.n))  # bukectのサイズ及び個数

        self.p = 0 # 自分で定義、ペアの数

    def _init_states(self):
        ########################################
        self.states = [0] * (self.n + 1)  # その時点における状態(自分で定義しろ) #いくつでもいい
        ########################################

        # [l,r)の半開区間で考える
        self.l = 0
        self.r = 0

        # queryを格納する用
        self.bucket = [list() for _ in range((self.b + 1))]

    def _add(self, i):
        # !!!書いたら_one_processにベタうちする
        # i番目の要素を含めて考えるときへstatesを更新
        ########################################
        a = self.ls[i]
        if self.states[a] % 2:
            self.p += 1
        self.states[a] += 1
        # print("add", a, self.states, self.p)
        ########################################

    def _delete(self, i):
        # !!!書いたら_one_processにベタうちする
        # i番目の要素を除いて考えるときへstatesを更新
        ########################################
        a = self.ls[i]
        if self.states[a] % 2 == 0:
            self.p -= 1
        self.states[a] -= 1
        # print("del", a, self.states, self.p)
        ########################################

    def _one_process(self, l, r):
        # クエリ[l,r)に対してstatesを更新する
        # !!!_add, _deleteの呼び出しが遅いのでベタ打ちする
        for i in range(self.r, r):  # rまで伸長
            # self._add(i)
            a = self.ls[i]
            if self.states[a] % 2:
                self.p += 1
            self.states[a] += 1
        for i in range(self.r - 1, r - 1, -1):  # rまで短縮
            # self._delete(i)
            a = self.ls[i]
            if self.states[a] % 2 == 0:
                self.p -= 1
            self.states[a] -= 1
        for i in range(self.l, l):  # lまで短縮
            # self._delete(i)
            a = self.ls[i]
            if self.states[a] % 2 == 0:
                self.p -= 1
            self.states[a] -= 1
        for i in range(self.l - 1, l - 1, -1):  # lまで伸長
            # self._add(i)
            a = self.ls[i]
            if self.states[a] % 2:
                self.p += 1
            self.states[a] += 1

        self.l = l
        self.r = r


    # def add_query(self, l, r, i):
    #     self.bucket[l // self.b].append((l, r, i))
    #     self.Q += 1


    def process(self, queries):
        self._init_states()

        for i, (l, r) in enumerate(queries):  # queryをbucketに格納
            self.bucket[l // self.b].append((l, r, i))

        for i, buc in enumerate(self.bucket):
            buc.sort(key=lambda x: x[1]*(1-i%2*2)) # 昇順→降順→昇順→...のジグザグ走行

        ret = [-1] * len(queries)
        for b in self.bucket:
            for l, r, i in b:  # クエリに答えていく
                self._one_process(l, r)
                ########################################
                # クエリに答える作業をここで書く
                # ans=
                ret[i] = self.p
                # print("####")
                ########################################
        return ret


def main():
    N = NI()
    A = NLI()
    Q = NI()
    querys = [NLI() for _ in range(Q)]
    querys = [(l-1, r) for l, r in querys]

    MO = Mo(A)
    # MO._init_states()
    # for i in range(Q):
    #     l, r = NMI()
    #     MO.add_query(l-1, r, i)

    ans = MO.process(querys)
    print(*ans, sep="\n")


def _main():
    N = NI()
    A = NLI()
    Q = NI()

    B = int(math.sqrt(N))
    # B = 500
    Bucket = [[] for _ in range(N//B + 2)]

    for i in range(Q):
        l, r = NMI()
        Bucket[l//B].append([l, r, i])

    for i, buc in enumerate(Bucket):
        buc.sort(key=lambda x: x[1] * (i%2*2-1))

    nl = 0
    nr = 0
    C = [0] * (N+1)
    ans = 0
    ANS = [0] * Q
    for buc in Bucket:
        for l, r, i in buc:
            # print(l, r, i)
            l -= 1

            for t in range(nr, r):
                # print(t)
                a = A[t]
                if C[a] % 2:
                    ans += 1
                C[a] += 1

            for t in range(nl, l, -1):
                # print(t)
                a = A[t-1]
                if C[a] % 2:
                    ans += 1
                C[a] += 1

            for t in range(nr, r, -1):
                # print(t)
                a = A[t-1]
                if C[a] % 2 == 0:
                    ans -= 1
                C[a] -= 1

            for t in range(nl, l):
                # print(t)
                a = A[t]
                if C[a] % 2 == 0:
                    ans -= 1
                C[a] -= 1

            nl = l
            nr = r
            ANS[i] = ans

    print(*ANS, sep="\n")


if __name__ == "__main__":
    main()
