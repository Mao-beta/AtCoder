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


def main():
    N, L = NMI()
    S = [SI() for _ in range(N)]



def _main():
    N, L = NMI()
    S = [SI() for _ in range(N)]

    # 各値はNodeで、子のindex[-1]*26+[prev](-3)+[failure](-2)+[終端のときの文字種](-1)をもつ。生成はnew_nodeを次のindexとする
    empty = [-1] * 29
    empty[-2] = 0
    trie = [empty]
    new_node = 1
    for i in range(N):
        now = 0
        for s in S[i]:
            s = ord(s) - ord('a')
            if trie[now][s] == -1:
                trie[now][s] = new_node
                trie.append(empty)
                trie[new_node][-3] = now
                new_node += 1
            now = trie[now][s]
        trie[now][-1] = i

    T = len(trie)
    # failureの更新
    que = deque([0])
    while que:
        v = que.popleft()
        print(v)
        for c in range(26):
            now = trie[v][-3] # prev
            if now == -1:
                continue
            while now > 0 and trie[trie[now][-2]][c] == -1:
                print(now, trie[now][-2])
                now = trie[now][-2]
            if trie[now][c] >= 0:
                trie[v][-2] = trie[now][c]
            else:
                trie[v][-2] = now
            if trie[v][c] != -1:
                que.append(trie[v][c])

    G = [[] for _ in range(len(trie))]
    for i, t in enumerate(trie):
        for j, tt in enumerate(t[:26]):
            if tt != -1:
                G[i].append(tt)

    # i文字見て現在がjで状態がk
    dp = [[[0]*(1<<N) for _ in range(T)] for _ in range(L+1)]
    dp[0][0][0] = 1
    for i in range(L):
        ni = i+1
        for j in range(T):
            for k in range(1<<N):
                if dp[i][j][k] == 0:
                    continue
                print(i, j, k, dp[i][j][k])
                for l in range(26):
                    if trie[j][l] == -1:
                        nj = trie[j][-2]
                    else:
                        nj = trie[j][l]
                    if trie[nj][-1] >= 0:
                        nk = k | (1 << trie[nj][-1])
                    else:
                        nk = k
                    dp[ni][nj][nk] += dp[i][j][k]
                    dp[ni][nj][nk] %= MOD99
    ans = 0
    for j in range(T):
        ans += dp[L][j][-1]
        ans %= MOD99
    print(ans)
    print(*trie, sep="\n")
    print(len(trie))


if __name__ == "__main__":
    main()
