import itertools
N, M, Q = map(int, input().split())
query = []
for i in range(Q):
    query.append(list(map(int, input().split())))

As = list(itertools.combinations_with_replacement(range(1, M+1), N))
ans = 0
for a in As:
    point = 0
    for q in query:
        if a[q[1]-1] - a[q[0]-1] == q[2]:
            #print(a, " + ", q)
            point += q[3]
    ans = max(ans, point)
    #print(point)

#print(As)
#print(query)
print(ans)