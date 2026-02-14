import sys
from heapq import heapify, heappop, heappush
from collections import Counter, deque
from prometheus_client import Counter

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


def solve(N, M, A):
    def judge(X):
        # 中央値をX以上にできるか？
        # X以上の本数をceil((N+M)/2)以上確保したうえであとを割り切れるか？
        rem = M
        k = (N+M+1)//2
        shorts = []
        Xs = []

        for a in A:
            # TODO:X以上の棒を最大限取るような操作をrem回以下で行いたい
            pass

        total = sum([n for x, n in Xs])
        if total < k:
            return False
        Xs.sort()
        add = sum([(x-1)*n for x, n in shorts])
        for i in range(k, len(Xs)):
            x, n = Xs[i]
            add += (x-1)*n
        print(X, Xs, shorts)
        return add >= rem

    ok = 1
    ng = max(A) + 1
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        if judge(X):
            ok = X
        else:
            ng = X

    return ok


def main():
    T = NI()
    for _ in range(T):
        N, M = NLI()
        A = NLI()
        ans = solve(N, M, A)
        print(ans)


if __name__ == "__main__":
    main()
