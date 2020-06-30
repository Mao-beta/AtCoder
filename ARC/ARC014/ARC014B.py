N = int(input())
W = [input() for _ in range(N)]
stock = []
for i, w in enumerate(W):
    if i == 0:
        stock.append(w)
        continue

    first = stock[-1][-1]
    if first != w[0] or w in stock:
        print('WIN' if i%2 else 'LOSE')
        exit()
    stock.append(w)

print('DRAW')