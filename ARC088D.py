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


def main():
    S = SI()
    N = len(S)
    if N % 2 == 1:
        c = S[N//2]
        ans = N // 2 + 1
        for i in range(1, N//2 + 1):
            l, r = N//2 - i, N//2 + i
            if S[l] == S[r] == c:
                ans += 1
            else:
                print(ans)
                exit()
        print(ans)

    else:
        ans = N // 2
        l, r = N // 2 - 1, N // 2
        for i in range(N//2):
            if S[l] == S[r] == S[N//2]:
                ans += 1
            else:
                print(ans)
                exit()
            l -= 1
            r += 1
        print(ans)



if __name__ == "__main__":
    main()
