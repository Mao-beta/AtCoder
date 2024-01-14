import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

from typing import List, Tuple


def two_sat(n: int, clause: List[Tuple[int, bool, int, bool]]) -> List[bool] | None:
    """
    clause: [(i, tf_i, j, tf_j), (), ...]

    連言標準形(CNF)形式 (y1∨y2)∧(y3∨y4)∧...∧(y2m−1∨y2m) の論理式をグラフに変換し、
    強連結成分分解(SCC)を行うことで充足可能性の判定を行う。
    # グラフの構築
    N個の論理変数 x1,...,xNを含む論理式について各変数ごとに xiと ¬xiを表す 2個の頂点、全体で 2N個の頂点を用意する。
    論理和 (a∨b) を (¬a⇒b)∧(¬b⇒a) と考え、¬a から b への辺 と ¬b から a への辺 を追加する。
    この v0 から v1 への辺は、v0 が真の場合に v1 も真にする必要があることを表す。

    # 充足可能性の判定
    構築したグラフのSCCを求め、各変数 xi と ¬xi が同じ強連結成分に含まれていないかを判定する。
    # 論理式を満たす割り当て
    強連結成分ごとのトポロジカル順序をもとに論理式が真になる時の各変数の割り当てを決定できる。
    トポロジカル順序で ¬xi が xi より先にくる場合は xi を真、それ以外の場合は偽を割り当てる。

    # 使用法
    ans=two_sat(N,clause)
    ここで、条件を満たすような割当が存在しないならばansはNoneであり、条件を満たすような割当が存在するならばその割当の一つが返ってきます。
    その場合、ansは長さがNのリストであって、各要素はTrueまたはFalseとなります。
    """
    answer = [0] * n
    edges = []
    N = 2 * n
    for s in clause:
        i, f, j, g = s
        edges.append((2 * i + (0 if f else 1), 2 * j + (1 if g else 0)))
        edges.append((2 * j + (0 if g else 1), 2 * i + (1 if f else 0)))
    M = len(edges)
    start = [0] * (N + 1)
    elist = [0] * M
    for e in edges:
        start[e[0] + 1] += 1
    for i in range(1, N + 1):
        start[i] += start[i - 1]
    counter = start[:]
    for e in edges:
        elist[counter[e[0]]] = e[1]
        counter[e[0]] += 1
    visited = []
    low = [0] * N
    Ord = [-1] * N
    ids = [0] * N
    NG = [0, 0]

    def dfs(v):
        stack = [(v, -1, 0), (v, -1, 1)]
        while stack:
            v, bef, t = stack.pop()
            if t:
                if bef != -1 and Ord[v] != -1:
                    low[bef] = min(low[bef], Ord[v])
                    stack.pop()
                    continue
                low[v] = NG[0]
                Ord[v] = NG[0]
                NG[0] += 1
                visited.append(v)
                for i in range(start[v], start[v + 1]):
                    to = elist[i]
                    if Ord[to] == -1:
                        stack.append((to, v, 0))
                        stack.append((to, v, 1))
                    else:
                        low[v] = min(low[v], Ord[to])
            else:
                if low[v] == Ord[v]:
                    while (True):
                        u = visited.pop()
                        Ord[u] = N
                        ids[u] = NG[1]
                        if u == v:
                            break
                    NG[1] += 1
                low[bef] = min(low[bef], low[v])

    for i in range(N):
        if Ord[i] == -1:
            dfs(i)
    for i in range(N):
        ids[i] = NG[1] - 1 - ids[i]
    for i in range(n):
        if ids[2 * i] == ids[2 * i + 1]:
            return None
        answer[i] = (ids[2 * i] < ids[2 * i + 1])
    return answer


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

prime_table = make_prime_table(2000000)
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


def main():
    N = NI()
    AB = [NLI() for _ in range(N)]



if __name__ == "__main__":
    main()
