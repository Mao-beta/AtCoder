C = []
for i in range(3):
    C.append(list(map(int, input().split())))

d1 = C[0][0] + C[1][1] + C[2][2]
d2 = C[1][0] + C[2][1] + C[0][2]
d3 = C[2][0] + C[0][1] + C[1][2]
if d1 == d2 == d3:
    print('Yes')
else:
    print('No')