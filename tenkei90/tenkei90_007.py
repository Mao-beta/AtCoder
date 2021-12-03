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
    N = NI()
    A = NLI() + [-10**10, 10**10]
    A.sort()
    Q = NI()
    for _ in range(Q):
        q = NI()
        idx = bisect.bisect_left(A, q)
        ans = min(abs(A[idx-1]-q), abs(A[idx]-q))
        print(ans)


if __name__ == "__main__":
    main()
