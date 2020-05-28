N, M = map(int, input().split())
graph = [set() for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)

#print(graph)
for i in range(N):
    ans = 0
    for j in range(N):
        if i == j or j in graph[i]:
            continue
        #print(graph[i] & graph[j])
        if len(graph[i] & graph[j]):
            ans += 1
    print(ans)