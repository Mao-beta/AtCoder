from _collections import deque
N = int(input())
W = input()
tmp = ''
while tmp != W:
    tmp = W
    W = W.replace('RR', '').replace('GG', '').replace('BB', '')

col = ''
for i, s in enumerate(W):
    if col == '':
        col = s
        continue
    if len(col) == 1:
        if col == s:
            col = ''
            continue
        else:
            col += s
            continue
    if col[0] == s:
        col = col[1:]
        continue
    if col[-1] == s:
        col = col[0:-1]
        continue
    if i == len(W)-1:
        col += s
        continue

    if W[i+1] == col[0]:
        col += s
        continue
    if W[i+1] == col[-1]:
        col = s + col
        continue

print(len(col))