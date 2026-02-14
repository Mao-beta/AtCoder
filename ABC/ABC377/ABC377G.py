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


INF = 10**10

class Node:
    def __init__(self, par, step, val):
        self.par = par
        self.val = val
        self.step = step
        self.C = [-1] * 26

    def __str__(self):
        return f"par={self.par} val={self.val} C={self.C}"

    def __repr__(self):
        return f"par={self.par} val={self.val} C={self.C}"


class Trie:
    def __init__(self):
        self.tree = [Node(par=-1, step=0, val=0)]
        self.new_idx = 1

    def add(self, key):
        now = 0
        sl = len(key)
        for i, s in enumerate(key, start=1):
            si = int(s)

            par_node = self.tree[now]

            if par_node.C[si] != -1:
                now = par_node.C[si]
                self.tree[now].val = min(self.tree[now].val, sl-i)
                continue

            par_node.C[si] = self.new_idx

            node = Node(par=now, step=i, val=sl-i)
            now = self.new_idx
            self.tree.append(node)
            self.new_idx += 1

        # leaf = self.tree[now]
        # leaf.val += val


    def scan(self, S: list):
        """
        Sについてtrieを辿る
        各nodeのvalを足したものを返す
        :param key:
        :return:
        """
        # print(S)
        res = INF
        now = 0
        sl = len(S)
        for i, s in enumerate(S):
            assert 0 <= s < 26
            now_node = self.tree[now]
            res = min(res, now_node.val + sl - now_node.step)
            goto = now_node.C[s]

            if goto == -1:
                now = 0
                now_node = self.tree[now]
                goto = now_node.C[s]
                if goto == -1:
                    goto = 0
                break

            now = goto
        now_node = self.tree[now]
        res = min(res, now_node.val + sl - now_node.step)

        return res


def str2int(S):
    return [ord(s) - ord("a") for s in S]


def main():
    N = NI()
    T = Trie()
    for _ in range(N):
        S = SI()
        S = str2int(S)
        ans = T.scan(S)
        print(ans)
        T.add(S)


if __name__ == "__main__":
    main()
