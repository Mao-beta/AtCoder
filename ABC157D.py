N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
block = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(K):
    a, b = map(int, input().split())
    block[a].append(b)
    block[b].append(a)

