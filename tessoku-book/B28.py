import sys

sys.setrecursionlimit(90000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353


def main():
    N = int(input())
    A = [0] * (N+1)
    A[1] = 1
    for i in range(2, N+1):
        A[i] = A[i-1] + A[i-2]
        A[i] %= MOD
    print(A[N])


if __name__ == "__main__":
    main()
