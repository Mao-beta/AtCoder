import sys, math, bisect
from typing import List, Tuple, Dict

# ============================ Utils / IO ============================

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_k(k: int) -> List[int]:
    buf = []
    while len(buf) < k:
        line = sys.stdin.readline()
        if not line:
            break
        parts = line.strip().split()
        if parts:
            buf.extend(map(int, parts))
    return buf[:k]

def print_line(vals: List[int]) -> None:
    sys.stdout.write(" ".join(map(str, vals)) + "\n")
    sys.stdout.flush()

# ====================== Order statistics (U[0,1]) ===================

def order_stats_mu_sigma(M: int) -> Tuple[List[float], List[float]]:
    mu = [0.0]*M
    sig = [0.0]*M
    for j in range(1, M+1):
        a = j
        mu_j  = a / (M + 1.0)
        var_j = (a * (M + 1 - a)) / ((M + 1.0)**2 * (M + 2.0))
        mu[j-1]  = mu_j
        sig[j-1] = math.sqrt(var_j)
    return mu, sig

# ========================= Planning helpers =========================

def synth_residuals(L:int, U:int, mu:List[float], sig:List[float], base_vals:List[int],
                    t: float) -> List[int]:
    """tσ 上振れシナリオの B_(j) を合成し、r_j = max(0, B - base_j) を返す。"""
    W = max(0, U - L)
    M = len(mu)
    r = []
    for j in range(M):
        frac = mu[j] + t*sig[j]
        if frac < 0.0: frac = 0.0
        if frac > 1.0: frac = 1.0
        Bj = L + int(round(W * frac))
        rr = Bj - base_vals[j]
        if rr < 0: rr = 0
        r.append(rr)
    return r

def unlimited_binary_demand(residuals: List[int], v_levels: List[int]) -> Tuple[List[int], int]:
    """
    残差 r を v の大→小で floor 貪欲に割る（供給無制限）。
    戻り値: 各レベル使用枚数 cnt[k], 総改善量 gain
    """
    K = len(v_levels)
    cnt = [0]*K
    gain = 0
    r = residuals[:]  # copy
    for k in range(K-1, -1, -1):
        v = v_levels[k]
        if v <= 0:
            continue
        used_k = 0
        for j in range(len(r)):
            if r[j] >= v:
                t = r[j] // v
                if t > 0:
                    used_k += t
                    r[j] -= t * v
        cnt[k] = used_k
        gain += used_k * v
    return cnt, gain

def simulate_gain_floor_pairs(residuals: List[int], v_levels: List[int], c_levels: List[int]) -> Tuple[int, List[int], List[int]]:
    """
    供給 c_levels で floor を高→低に実行し、その後「一段下の2枚代用」を実施。
    戻り値: 総改善量 gain, 実使用枚数 used[k], 代用で下位(k-1)が使った枚数 pair_used_low[k-1]（2の倍数）
    """
    M = len(residuals)
    K = len(v_levels)
    r = residuals[:]
    supply = c_levels[:]
    used = [0]*K
    pair_low_used = [0]*K
    gain = 0

    # --- Floor: 高→低 ---
    for k in range(K-1, -1, -1):
        v = v_levels[k]
        cnt = supply[k]
        if cnt <= 0:
            continue
        # r>=v の山に入る限り入れ続ける（都度最大 r を探す）
        while cnt > 0:
            j_best = -1
            rbest = v - 1
            for j in range(M):
                if r[j] >= v and r[j] > rbest:
                    rbest = r[j]; j_best = j
            if j_best < 0:
                break
            r[j_best] -= v
            used[k] += 1
            gain += v
            cnt -= 1
        supply[k] = cnt  # 余り

    # --- 代用: k 段の不足を k-1 段 2 枚で補う ---
    for k in range(K-1, 0, -1):
        v  = v_levels[k]
        vL = v_levels[k-1]
        if supply[k] <= 0 and supply[k-1] >= 2:
            # まだ r>=v の山に置ける回数（近似、都度最大 r を探す）
            def count_need():
                c = 0
                for j in range(M):
                    if r[j] >= v:
                        c += r[j] // v
                return c
            shortage = count_need()
            pairs = min(shortage, supply[k-1] // 2)
            for _ in range(pairs):
                j_best = -1
                rbest = v - 1
                for j in range(M):
                    if r[j] >= v and r[j] > rbest:
                        rbest = r[j]; j_best = j
                if j_best < 0:
                    break
                r[j_best] -= 2 * vL
                gain += 2 * vL
            pair_low_used[k-1] += 2 * pairs
            supply[k-1] -= 2 * pairs

    return gain, used, pair_low_used

def choose_levels_counts_refined(N:int, M:int, L:int, U:int, base_vals:List[int],
                                 mu:List[float], sig:List[float],
                                 Kmin:int=9, Kmax:int=20, per_level_cap:int=35
                                 ) -> Tuple[List[int], List[int]]:
    """
    K を走査して、v_levels（小→大）と c_levels（各段枚数）を決定。
    - 各Kで R_max から δ と v_levels を決定（v_k = δ·2^k）
    - シナリオ r(t) で無制限二進分解 → 期待需要 E_cnt[k] を推定
    - 有益スロット Lk = min(ceil(E_cnt[k]), cap) を **上位→下位の貪欲**で配分
    - 余りは **上位→下位ラウンドロビン**で均し配分（最小段一極集中を回避）
    - 供給制約のシミュレーション（floor+代用）で期待改善量を評価し、最良 K を採用
    """
    B = max(0, N - M)
    W = max(0, U - L)
    if W == 0:
        return [1], [B]

    scenarios = [(0.0, 0.20), (1.0, 0.50), (2.0, 0.30)]
    R_max = max(U - b for b in base_vals)
    Kcap_by_delta = max(1, int(math.floor(math.log2(R_max + 1))))  # 2^K - 1 <= R_max
    Kmax = min(Kmax, Kcap_by_delta)

    eprint(f"[PLAN] B={B}  W={W}  R_max={R_max}  K_range=[{Kmin},{Kmax}]")

    best_score = -1.0
    best_v = []
    best_c = []
    best_dbg = {}

    for K in range(Kmin, Kmax+1):
        denom = (1 << K) - 1
        delta = max(1, (R_max + denom - 1) // denom)
        v_levels = [delta << k for k in range(K)]  # 小→大

        # --- 無制限需要（期待） ---
        E_cnt = [0.0]*K
        exp_gain_unlim = 0.0
        for t, w in scenarios:
            r = synth_residuals(L, U, mu, sig, base_vals, t)
            cnt, gain = unlimited_binary_demand(r, v_levels)
            for k in range(K):
                E_cnt[k] += w * cnt[k]
            exp_gain_unlim += w * gain

        # --- 有益スロット Lk（cap で頭打ち）と初期配分（上位優先） ---
        Lk = [min(per_level_cap, int(math.ceil(E_cnt[k]))) for k in range(K)]
        c = [0]*K
        remain = B
        for k in range(K-1, -1, -1):  # 高→低
            if remain <= 0: break
            take = min(Lk[k], remain)
            c[k] = take
            remain -= take

        # --- 余りを均し配分（上位→下位ラウンドロビン） ---
        if remain > 0:
            k_idx = K-1
            # 安全弁：極端なケースでも最悪 B 回で収束
            steps = 0
            while remain > 0 and steps < B * 2:
                if c[k_idx] < per_level_cap:
                    c[k_idx] += 1
                    remain -= 1
                    if remain == 0: break
                k_idx -= 1
                if k_idx < 0: k_idx = K-1
                steps += 1
            if remain > 0:
                # 念のため：まだ残れば最下位へ（極稀）
                c[0] += remain
                remain = 0

        # --- 供給制約シミュレーション（評価） ---
        exp_gain_supply = 0.0
        for t, w in scenarios:
            r = synth_residuals(L, U, mu, sig, base_vals, t)
            gain_s, _, _ = simulate_gain_floor_pairs(r, v_levels, c)
            exp_gain_supply += w * gain_s

        score = exp_gain_supply + 1e-6 * K  # 同点なら K 大を優先
        eprint(f"[PLAN/K] K={K} delta={delta} v0={v_levels[0]} v_top={v_levels[-1]} "
               f"E_sum={int(sum(E_cnt))} alloc_sum={sum(c)} gain_unlim={exp_gain_unlim:.3e} gain_supply={exp_gain_supply:.3e}")

        if score > best_score:
            best_score = score
            best_v = v_levels
            best_c = c
            best_dbg = {
                "K": K, "delta": delta,
                "E_cnt": E_cnt, "Lk": Lk,
                "exp_gain_unlim": exp_gain_unlim,
                "exp_gain_supply": exp_gain_supply
            }

    # --- 採用Kの詳細 ---
    eprint(f"[PLAN/CHOSEN] K={best_dbg['K']} delta={best_dbg['delta']} "
           f"v0={best_v[0]} v_top={best_v[-1]}  alloc_sum={sum(best_c)} / B={B}")
    eprint("[PLAN/CHOSEN] level (k, v, E_cnt≈, Lk, c):")
    for k in range(len(best_v)-1, -1, -1):
        v = best_v[k]
        e_cnt = best_dbg["E_cnt"][k]
        Lk = min(per_level_cap, int(math.ceil(e_cnt)))
        eprint(f"  k={k:2d}  v={v}  E_cnt≈{e_cnt:.1f}  Lk={Lk}  c={best_c[k]}")

    return best_v, best_c

# ========================= Runtime allocation ========================

def allocate_floor_level(residuals: List[int], X: List[int], pos_list: List[int], v: int) -> int:
    """
    値 v のカードを r>=v の山に、入れられる限り入れ続ける。
    （毎回 r 最大の山を探し、1 枚置く→再検索。positions の順序には依存しない）
    """
    if not pos_list:
        return 0
    used = 0
    M = len(residuals)
    while pos_list:
        j_best = -1
        rbest = v - 1
        for j in range(M):
            rj = residuals[j]
            if rj >= v and rj > rbest:
                rbest = rj; j_best = j
        if j_best < 0:
            break  # これ以上 v を置けない
        idx = pos_list.pop()  # どのカードでも同じ
        X[idx] = j_best + 1
        residuals[j_best] -= v
        used += 1
    return used

def allocate_pairs_from_lower(residuals: List[int], X: List[int],
                              pos_low: List[int], v_low: int,
                              v_target: int, max_pairs: int) -> int:
    """
    v_target (= 2*v_low) 不足分を、v_low を同一山に 2 枚入れて代用。
    r>=v_target の最大 r の山を毎回選ぶ。
    """
    if max_pairs <= 0 or len(pos_low) < 2:
        return 0
    used_pairs = 0
    M = len(residuals)
    while used_pairs < max_pairs and len(pos_low) >= 2:
        j_best = -1
        rbest = v_target - 1
        for j in range(M):
            rj = residuals[j]
            if rj >= v_target and rj > rbest:
                rbest = rj; j_best = j
        if j_best < 0:
            break
        idx1 = pos_low.pop()
        idx2 = pos_low.pop()
        X[idx1] = j_best + 1
        X[idx2] = j_best + 1
        residuals[j_best] -= 2 * v_low
        used_pairs += 1
    return used_pairs

def improvement_signed(s: int, v: int) -> int:
    """
    Δ = |s| - |s - v|。s>=0 を想定。Δ>0 のときだけ価値あり。
      - s >= v : Δ = v
      - s < v  : Δ = 2s - v (正: s < v <= 2s)
    """
    if s <= 0:
        return -1
    if s >= v:
        return v
    return 2*s - v

def allocate_nearest_global(residuals: List[int], X: List[int],
                            leftover_by_value: Dict[int, List[int]]) -> int:
    """
    残カード全体から、毎回 Δ 最大の (山j, 値v) を選んで 1枚ずつ置く。
    Δ<=0 になったら停止。
    """
    if not leftover_by_value:
        return 0
    values = sorted(leftover_by_value.keys())
    counts = {v: len(leftover_by_value[v]) for v in values}
    placed = 0
    steps = 0

    while True:
        best_delta = 0
        best_j = -1
        best_v = None

        # 各山ごとに候補 v を2系統で探索（v<=s の最大 / s<v<=2s の最小）
        for j, s in enumerate(residuals):
            if s <= 0:
                continue
            # v<=s の最大
            idx1 = bisect.bisect_right(values, s) - 1
            v1 = None; d1 = 0
            while idx1 >= 0:
                vv = values[idx1]
                if counts.get(vv, 0) > 0:
                    v1 = vv; d1 = vv
                    break
                idx1 -= 1
            # s<v<=2s の最小
            v2 = None; d2 = 0
            idx2 = bisect.bisect_right(values, s)
            while idx2 < len(values) and values[idx2] <= 2*s:
                vv = values[idx2]
                if counts.get(vv, 0) > 0:
                    v2 = vv; d2 = 2*s - vv
                    break
                idx2 += 1

            if d2 > d1:
                v_choice, delta = v2, d2
            else:
                v_choice, delta = v1, d1

            if v_choice is not None and delta > best_delta:
                best_delta = delta; best_j = j; best_v = v_choice

        if best_delta <= 0 or best_v is None or best_j < 0:
            break

        # 割り当て
        idx_list = leftover_by_value[best_v]
        idx_card = idx_list.pop()
        counts[best_v] -= 1
        X[idx_card] = best_j + 1
        residuals[best_j] -= best_v
        placed += 1
        steps += 1

        if not idx_list:
            del leftover_by_value[best_v]
            values = sorted(leftover_by_value.keys())  # 値の種類が減ったら更新

        if steps > 200000:  # 安全弁
            eprint("[NEAREST] safety break (steps>2e5)")
            break

    return placed

# =============================== Main ===============================

def main():
    # ---- 入力 ----
    t = read_k(4)
    if len(t) < 4:
        return
    N, M, L, U = t
    W = max(0, U - L)
    lam = 2.5  # ベースライン b_j = mu - lam*sigma

    eprint(f"[INIT] N={N} M={M} L={L} U={U} W={W} lam={lam}")

    # ---- ベースライン（順序統計：mu - lam*sigma を [L,U] にクリップ）----
    mu, sig = order_stats_mu_sigma(M)
    base_vals = []
    for j in range(M):
        bf = mu[j] - lam * sig[j]
        if bf < 0.0: bf = 0.0
        if bf > 1.0: bf = 1.0
        base_vals.append(L + int(round(W * bf)))
    eprint(f"[BASE] base min={min(base_vals)} max={max(base_vals)} mean={sum(base_vals)/M:.3f}")

    # ---- K と各段枚数を決定（最小段厚めになりすぎない分配）----
    v_levels, c_levels = choose_levels_counts_refined(
        N=N, M=M, L=L, U=U, base_vals=base_vals, mu=mu, sig=sig,
        Kmin=15, Kmax=20, per_level_cap=35
    )
    v_levels = [10000000, 122074038, 244148076, 488296152, 976592304, 1953184608, 3906369216, 7812738432, 15625476864, 31250953728,
     62501907456, 125003814912, 250007629824, 500015259648, 1000030519296, 2000061038592]
    c_levels = [1, 29, 34, 34, 34, 30, 30, 31, 35, 32, 35, 25, 25, 25, 10, 7]
    K = len(v_levels)

    # ---- A 構築（A は1行出力）----
    A: List[int] = []
    base_pos = list(range(len(A), len(A) + M))
    A.extend(base_vals)

    level_positions: List[List[int]] = []
    for k in range(K):
        cnt = c_levels[k]
        if cnt > 0:
            pos = list(range(len(A), len(A) + cnt))
            A.extend([v_levels[k]] * cnt)
            level_positions.append(pos)
        else:
            level_positions.append([])

    # 余りが出たら高→低ラウンドロビンで配る（最小段偏重を回避）
    if len(A) < N and K > 0:
        pad = N - len(A)
        k_idx = K - 1
        while pad > 0:
            level_positions[k_idx].append(len(A))
            A.append(v_levels[k_idx])
            pad -= 1
            k_idx -= 1
            if k_idx < 0: k_idx = K - 1

    eprint(f"[A] total_cards={len(A)} (base={M}, levels={len(A)-M}) "
           f"K={K} v0={v_levels[0]} v_top={v_levels[-1]}")
    print_line(A)  # ---- A を 1行で出力 ----

    # ---- B 読み込み ----
    B = read_k(M)
    if len(B) < M:
        return

    # ---- X 構築（X は1行出力）----
    X = [0] * N
    for j in range(M):
        X[base_pos[j]] = j + 1

    residuals = [B[j] - base_vals[j] for j in range(M)]
    neg_cnt = sum(1 for r in residuals if r < 0)
    if neg_cnt > 0:
        eprint(f"[RESID] negative residual piles={neg_cnt} -> set to 0 for floor")
    for j in range(M):
        if residuals[j] < 0:
            residuals[j] = 0

    eprint(f"[RESID] before floor: min={min(residuals)} max={max(residuals)} sum={sum(residuals)}")

    # ---- Floor 配布：高→低。入れられる限り while で入れる（バグ修正）----
    used_each = [0]*K
    for k in range(K-1, -1, -1):
        v = v_levels[k]
        pos_k = [idx for idx in level_positions[k] if X[idx] == 0]
        need_k = sum(r // v for r in residuals)
        used_k = allocate_floor_level(residuals, X, pos_k, v)
        used_each[k] += used_k
        left_cards = len([i for i in level_positions[k] if X[i] == 0])
        eprint(f"[FLOOR] k={k:2d} v={v} need≈{need_k} used={used_k} left_cards={left_cards}")

        # 足りなければ一段下の2枚で代用
        if k > 0:
            shortage = max(0, need_k - used_k)
            if shortage > 0:
                pos_low_free = [idx for idx in level_positions[k-1] if X[idx] == 0]
                pairs_possible = len(pos_low_free) // 2
                pairs = min(shortage, pairs_possible)
                if pairs > 0:
                    pairs_used = allocate_pairs_from_lower(residuals, X, pos_low_free, v_levels[k-1], v, pairs)
                    used_each[k-1] += 2 * pairs_used
                    eprint(f"[PAIR ] k={k:2d} v={v} pairs_used={pairs_used} (low_v={v_levels[k-1]})")

    eprint(f"[RESID] after floor: min={min(residuals)} max={max(residuals)} sum={sum(residuals)}")

    # ---- 仕上げ：グローバル nearest（Δ>0 の限り詰める）----
    leftover_by_value: Dict[int, List[int]] = {}
    total_left = 0
    for k in range(K):
        rem = [idx for idx in level_positions[k] if X[idx] == 0]
        if rem:
            v = v_levels[k]
            leftover_by_value.setdefault(v, []).extend(rem)
            total_left += len(rem)
    eprint(f"[NEAREST] leftover cards total={total_left} kinds={len(leftover_by_value)}")

    placed = allocate_nearest_global(residuals, X, leftover_by_value)
    eprint(f"[NEAREST] placed={placed}")

    # ---- 終了統計 ----
    over_cnt = sum(1 for r in residuals if r < 0)
    E_total  = sum(abs(r) for r in residuals)
    eprint(f"[FINAL] overshoot_piles={over_cnt}  E_total={E_total}  "
           f"resid_min={min(residuals)} resid_max={max(residuals)}  "
           f"used_levels={list(reversed(used_each))}")

    print_line(X)  # ---- X を 1行で出力 ----

if __name__ == "__main__":
    main()
