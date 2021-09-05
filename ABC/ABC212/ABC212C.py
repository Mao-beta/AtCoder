import sys
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M = NMI()
    A = NLI()
    B = NLI()
    A.sort()
    B.sort()
    ans = 10**10
    for a in A:
        idx = bisect.bisect_left(B, a)
        if idx != 0:
            bl = B[idx-1]
            ans = min(ans, abs(bl-a))
        if idx != M:
            br = B[idx]
            ans = min(ans, abs(br-a))
    print(ans)



if __name__ == "__main__":
    main()
