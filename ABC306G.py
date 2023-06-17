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


# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>) トポロジカルソート済
# 計算量: O(V+E)
def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

# 縮約後のグラフを構築
def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP


def adjlist(n, edges, directed=False, in_origin=1):
    if len(edges) == 0:
        return [[] for _ in range(n)]

    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]

    res = [[] for _ in range(n)]

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res


# 高速エラストテネス　sieve[n]はnの最小の素因数
def make_prime_table(n):
    sieve = list(range(n + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(4, n + 1, 2):
        sieve[i] = 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i] != i:
            continue
        for j in range(i * i, n + 1, i * 2):
            if sieve[j] == j:
                sieve[j] = i
    return sieve

prime_table = make_prime_table(1000)
# 素数列挙
primes = [p for i, p in enumerate(prime_table) if i == p]

# 素因数分解　上のprime_tableと組み合わせて使う
def prime_factorize(n):
    result = []
    while n != 1:
        p = prime_table[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        result.append((p, e))
    return result


# Nの素因数分解を辞書で返す(単体)
def prime_fact(n):
    root = int(n**0.5) + 1
    prime_dict = {}
    for i in range(2, root):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
    if n != 1:
        prime_dict[n] = 1
    return prime_dict

# 約数列挙（単体）
def divisors(x):
    res = set()
    for i in range(1, int(x**0.5) + 2):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return res


def solve(N, M, UV):
    # SCC
    G = adjlist(N, UV, directed=True)
    RG = adjlist(N, [[v, u] for u, v in UV], directed=True)
    label, group = scc(N, G, RG)
    gt = group[0]
    S = set()
    for i, g in enumerate(group):
        if g == gt:
            S.add(i)

    gcd = None

    # BFS
    steps = [-1] * N
    que = deque()
    que.append(0)
    steps[0] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto in G[now]:
            if goto not in S:
                continue
            if steps[goto] != -1:
                if gcd is None:
                    gcd = step+1 - steps[goto]
                else:
                    gcd = math.gcd(gcd, step + 1 - steps[goto])
                continue
            que.append(goto)
            steps[goto] = step + 1

    if gcd is None:
        print("No")
    else:
        PD = prime_fact(gcd)
        P = set(PD.keys())
        P.discard(1)
        P.discard(2)
        P.discard(5)
        if len(P) == 0:
            print("Yes")
        else:
            print("No")


def main():
    T = NI()
    for _ in range(T):
        N, M = NMI()
        UV = EI(M)
        solve(N, M, UV)


if __name__ == "__main__":
    main()
