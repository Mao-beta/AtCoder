import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
from collections import Counter
from collections import defaultdict
import bisect
from functools import reduce
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    N,M = MI()
    d = defaultdict(list)
    U = UnionFind(N + 1)
    cri = -1
    cri_l = -1
    cri_r = -1
    query_list = list()
    for i in range(M):
        a, b = MI()
        query_list.append((a,b))
        d[a].append(b)
        d[a].sort()
        d[b].append(a)
        d[b].sort()
        la = len(d[a])
        lb = len(d[b])
        if la >=3 or lb >= 3:
            print('No')
            exit()
        if la == 2 and cri_l == -1 and cri_r == -1:
            cri = a
            cri_l = d[a][0]
            cri_r = d[a][1]
        if lb == 2 and cri_l == -1 and cri_r == -1:
            cri = b
            cri_l = d[b][0]
            cri_r = d[b][1]
    #print(query_list)
    #print((cri,cri_l, cri_r), 'cri')
    if cri == -1 or cri_l == -1 or cri_r == -1:
        print('Yes')
        exit()

    for query in query_list:
        a, b = query[0], query[1]
        if a == cri:
            if b == cri_l or b == cri_r:
                continue
        if b == cri:
            if a == cri_l or a == cri_r:
                continue
        U.union(a, b)
    X = U.members(cri_r)
    Y = U.members(cri_l)
    for x in X:
        if x in Y:
            print('No')
            exit()
    print('Yes')

if __name__ == "__main__":
    main()