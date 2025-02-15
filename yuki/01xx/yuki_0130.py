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



class BinaryTrie:
    def __init__(self, bit=32):
        self.D = [[-1, -1]]
        self.bit = bit

    def add(self, x):
        now = 0
        for i in range(self.bit-1, -1, -1):
            b = (x>>i) & 1
            if self.D[now][b] == -1:
                self.D[now][b] = len(self.D)
            now = self.D[now][b]
            self.D.append([-1, -1])

    def dfs(self):
        ans = 1 << self.bit
        stack = deque()
        stack.append([0, 0])
        while stack:
            now, res = stack.pop()
            l, r = self.D[now]
            if l == r == -1:
                ans = min(ans, res)
            elif l == -1 or r == -1:
                res <<= 1
                if l == -1:
                    stack.append([r, res])
                else:
                    stack.append([l, res])
            else:
                res = (res << 1) | 1
                stack.append([l, res])
                stack.append([r, res])
        return ans


def xor_minimax(N, A):
    """
    非負整数列 A=(a1, ..., aN)の全体に非負整数xを選んでxorをとる
    操作後の最大値の最小値を返す O(N)
    """
    trie = BinaryTrie()
    for a in A:
        trie.add(a)
    return trie.dfs()


def main():
    N = NI()
    A = NLI()
    ans = xor_minimax(N, A)
    print(ans)


if __name__ == "__main__":
    main()
