from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)

queue = deque()
seen = [-1] * N
steps = [-1] * N
steps[0] = 0
parents = [-1] * N
queue.append(0)
while queue:
    node = queue.popleft()

    seen[node] = 1
    #print("now: "+str(node))
    for next in graph[node]:
        if seen[next] > -1:
            continue
        #print("next: " + str(next))
        queue.append(next)
        seen[next] = 1
        steps[next] = steps[node] + 1
        parents[next] = node

print("Yes")
for a in parents[1:]:
    print(a+1)