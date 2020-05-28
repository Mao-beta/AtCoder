import sys
import math
from collections import deque
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


#隣接リスト 1-order
def make_adjlist_d(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


#nCr
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


def main():
    N, K = NMI()
    A = sorted(NLI())
    B = sorted(NLI())

    left_X = 1
    right_X = A[-1] * B[-1] + 1
    mid = (left_X + right_X) // 2
    while right_X - left_X > 1:
        #print(left_X, mid, right_X, count_under_X(A, B, mid))
        if count_under_X(A, B, mid) >= K:
            right_X = mid
            mid = (left_X + right_X) // 2
        else:
            left_X = mid
            mid = (left_X + right_X) // 2
    print(right_X)



def count_under_X(A, B, X):
    res = 0
    for a in A:
        res += bisect.bisect_right(B, X // a)
    return res



if __name__ == "__main__":
    main()