N, G, E = map(int, input().split())
girls = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)