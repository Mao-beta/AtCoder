N, M = map(int, input().split())
H = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

possible = [1] * (N+1)
possible[0] = 0
ans = 0
for t in range(1, N+1):
    if not possible[t]: continue
    for next in graph[t]:
        if H[t] > H[next]:
            possible[next] = 0
        else:
            possible[t] = 0
    if possible[t]:
        ans += 1

print(ans)