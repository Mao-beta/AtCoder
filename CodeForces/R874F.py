import sys
from collections import deque, defaultdict, Counter

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
    T = NI()
    pws = [1]
    for i in range(1, 200005):
        pws.append(pow(i, -1, MOD))

    for _ in range(T):
        N, M = NMI()
        A = NLI()
        if M == 1:
            print(N)
            continue
        C = Counter(A)
        S = sorted(C.keys())
        ans = 0
        cnt = 0
        prev = 0
        now = 1
        for s in S:
            if s - prev > 1:
                cnt = 0
                now = 1
            cnt += 1
            now = now * C[s] % MOD
            if cnt > M:
                now = now * pws[C[s-M]] % MOD
                cnt = M
            if cnt == M:
                ans += now
                ans %= MOD
            prev = s
        print(ans)


if __name__ == "__main__":
    main()
