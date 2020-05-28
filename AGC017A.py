N, P = map(int, input().split())
A = list(map(lambda x: int(x)%2, input().split()))

odd = A.count(1)
even = N - odd
if odd:
    print(2 ** (N-1))
else:
    print(0 if P else 2 ** N)