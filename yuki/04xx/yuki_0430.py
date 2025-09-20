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


class Node:
    def __init__(self, par, val):
        self.par = par
        self.val = val
        self.C = [-1] * 26

    def __str__(self):
        return f"par={self.par} val={self.val} C={self.C}"

    def __repr__(self):
        return f"par={self.par} val={self.val} C={self.C}"


class Trie:
    def __init__(self):
        self.tree = [Node(-1, 0)]
        self.new_idx = 1

    def add(self, key, val):
        now = 0
        for s in key:
            si = int(s)

            par_node = self.tree[now]

            if par_node.C[si] != -1:
                now = par_node.C[si]
                continue

            par_node.C[si] = self.new_idx

            node = Node(par=now, val=0)
            now = self.new_idx
            self.tree.append(node)
            self.new_idx += 1

        leaf = self.tree[now]
        leaf.val += val


    def scan(self, S: list):
        """
        Sについてtrieを辿る
        各nodeのvalを足したものを返す
        :param key:
        :return:
        """
        res = 0
        now = 0
        for s in S:
            assert 0 <= s < 26
            now_node = self.tree[now]
            goto = now_node.C[s]

            if goto == -1:
                now = 0
                now_node = self.tree[now]
                goto = now_node.C[s]
                if goto == -1:
                    goto = 0

            now = goto
            res += self.tree[now].val
            print(now, self.tree[now].val)

        return res


def str2int(S):
    return [ord(s) - ord("A") for s in S]


from collections import deque

class AhoCorasick:
    """
    検索でひっかけたい複数の文字列patternsを登録し、
    任意の文字列から拾えるだけ拾う

    https://ikatakos.com/pot/programming_algorithm/string_search#aho-corasick_%E6%B3%95

    ahc = AhoCorasick(['bc', 'd', 'ababcde', 'bababcde', 'ab'])
    print(ahc.search('xbababcdex'))
    # => [(2, 3, 'ab'), (4, 5, 'ab'), (5, 6, 'bc'), (7, 7, 'd'), (1, 8, 'bababcde'), (2, 8, 'ababcde')]
    """
    def __init__(self, patterns):
        self.patterns = patterns
        self.children = [{}]
        self.match = [[]]

        for pi, pattern in enumerate(patterns):
            self._register(pi, pattern)

        self.failure = [0] * len(self.children)
        self._create_failure()

    def _register(self, pi, pattern):
        k = 0
        for c in pattern:
            if c in self.children[k]:
                k = self.children[k][c]
            else:
                j = len(self.children)
                self.children[k][c] = j
                self.children.append({})
                self.match.append([])
                k = j
        self.match[k].append(pi)

    def _create_failure(self):
        children = self.children
        match = self.match
        failure = self.failure

        q = deque(children[0].values())
        while q:
            k = q.popleft()
            b = failure[k]
            for c, j in children[k].items():
                failure[j] = self._next(b, c)
                match[j].extend(match[failure[j]])
                q.append(j)

    def _next(self, k, c):
        while True:
            if c in self.children[k]:
                return self.children[k][c]
            if k == 0:
                return 0
            k = self.failure[k]

    def search(self, target):
        match = self.match
        patterns = self.patterns

        k = 0
        matched = []
        for i, c in enumerate(target):
            k = self._next(k, c)
            matched.extend((i - len(patterns[m]) + 1, i, patterns[m]) for m in match[k])
        return matched


class AhoCorasick:
    # https://atcoder.jp/contests/abc419/submissions/68508234
    def __init__(self, sigma=26):
        self.node = [[-1] * sigma]
        self.last = [0]
        self.sigma = sigma

    def add(self, arr, ID):
        v = 0
        for c in arr:
            if self.node[v][c] == -1:
                self.node[v][c] = len(self.node)
                self.node.append([-1] * self.sigma)
                self.last.append(0)
            v = self.node[v][c]
        self.last[v] |= 1 << ID

    def build(self):
        link = [0] * len(self.node)
        que = deque()
        for i in range(self.sigma):
            if self.node[0][i] == -1:
                self.node[0][i] = 0
            else:
                link[self.node[0][i]] = 0
                que.append(self.node[0][i])

        while que:
            v = que.popleft()
            self.last[v] |= self.last[link[v]]
            for i in range(self.sigma):
                u = self.node[v][i]
                if u == -1:
                    self.node[v][i] = self.node[link[v]][i]
                else:
                    link[u] = self.node[link[v]][i]
                    que.append(u)


def main():
    S = SI()
    N = NI()
    C = [SI() for _ in range(N)]
    ahc = AhoCorasick(C)
    print(len(ahc.search(S)))


if __name__ == "__main__":
    main()
