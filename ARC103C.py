from collections import Counter
N = int(input())
v = list(map(int, input().split()))
v_odd = v[0::2]
v_even = v[1::2]
cnt_o = Counter(v_odd).most_common()
cnt_e = Counter(v_even).most_common()
if cnt_o[0][0] != cnt_e[0][0]:
    print(N - cnt_o[0][1] - cnt_e[0][1])
else:
    if len(cnt_o) == 1 and len(cnt_e) == 1:
        print(N // 2)
    elif len(cnt_o) == 1:
        print(len(v_even) - cnt_e[1][1])
    elif len(cnt_e) == 1:
        print(len(v_odd) - cnt_o[1][1])
    else:
        print(min(N - cnt_o[1][1] - cnt_e[0][1], N - cnt_o[0][1] - cnt_e[1][1]))
