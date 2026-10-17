import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M = NMI()
    is_ok = [[0]*M for _ in range(N)]
    for i in range(N):
        phone = NLI()
        for a in phone[1:]:
            a -= 1
            is_ok[i][a] = 1

    P, Q = NMI()
    B = NLI()
    ans = 0
    for phone in is_ok:
        cnt = 0
        for b in B:
            b -= 1
            if phone[b]:
                cnt += 1
        if cnt >= Q:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
