P = float(input())
left = 0.0
right = P
midL = P/3
midR = P*2/3


def calc_time(P, x):
    return P * 2.0 ** (-x/1.5) + x

for i in range(100000):
    results = [calc_time(P, left), calc_time(P, midL), calc_time(P, midR), calc_time(P, right)]
    #print(left, midL, midR, right)
    if midR - midL <= 0.000000001:
        break
    if results[1] > results[2]:
        left, midL, midR, right = midL, (midL*2 + right)/3, (midL + right*2)/3, right
    else:
        left, midL, midR, right = left, (left * 2 + midR) / 3, (left + midR * 2) / 3, midR

print(results[1])