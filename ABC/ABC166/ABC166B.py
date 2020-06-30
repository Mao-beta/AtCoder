N, K = map(int, input().split())
have = set()
for k in range(K):
    d = int(input())
    a = set(map(int, input().split()))
    for i in a:
        have.add(i)
print(N - len(have))