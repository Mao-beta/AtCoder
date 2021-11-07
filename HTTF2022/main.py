try:
    # local environment
    import numpy as np
    IS_LOCAL = True
except:
    # online judge
    IS_LOCAL = False

import sys
from itertools import chain

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


class Scheduler:
    def __init__(self, N, M, is_local):
        self.N = N
        self.M = M
        self.day = 1
        self.is_local = is_local

        # -1: not started
        #  0: assigned
        #  1: finished
        self.task_status = [-1] * N

        # -1: ready
        #  i: task i 作業中(0<=i<N)
        self.member_status = [-1] * M
        self.member_start = [-1] * M
        self.release_events = [[] for _ in range(2001)]

    def add_day(self):
        self.day += 1

    def release(self):
        # release_events[day]を順に処理
        # その日に終わる仕事についてtask, memberのstatusを変更
        released = self.release_events[self.day]
        released.sort()

        res = []
        for task, member in released:
            real_day = self.day - self.member_start[member] + 1

            self.task_status[task] = 1
            self.member_status[member] = -1
            res.append([task, member, real_day])

        return res

    def release_one(self, member):
        task = self.member_status[member]
        real_day = self.day - self.member_start[member] + 1
        self.task_status[task] = 1
        self.member_status[member] = -1
        return task, member, real_day


    def assign(self, task, member, need=0):
        self.task_status[task] = 0
        self.member_status[member] = task
        self.member_start[member] = self.day

        if need > 0:
            self.release_events[self.day + need - 1].append([task, member])


def calc_day(D, S):
    assert len(D) == len(S)
    w = sum([max(0, d - s) for d, s in zip(D, S)])
    if w == 0:
        return 1
    else:
        r = 0
        #r = random.randint(-3, 3)
        return max(1, w + r)


def greedy_assign(members, tasks, task_dep):
    """
    空いているmember全員を今可能なtaskにassign
    """
    res = []
    for m, m_status in enumerate(members):
        if m_status != -1:
            continue

        for t, t_status in enumerate(tasks):
            if t_status != -1:
                continue

            parents = task_dep[t]
            is_ok = True
            for par in parents:
                if tasks[par] != 1:
                    is_ok = False

            if is_ok:
                res.append([m, t])
                tasks[t] = 0
                break

    return res


def brute_force_assign(members, tasks, task_dep, task_difficulty, pred_skills):
    """
    taskごとに空いている全員と予測、pred_day最小のmemberをassign
    """
    res = []

    for t, t_status in enumerate(tasks):
        if t_status != -1:
            continue

        parents = task_dep[t]
        is_ok = True
        for par in parents:
            if tasks[par] != 1:
                is_ok = False

        if not is_ok:
            continue

        diff = task_difficulty[t]
        tmp_m = -1
        tmp_pred = 10000
        for m, m_status in enumerate(members):
            if m_status != -1:
                continue

            skill = pred_skills[m]
            pred = calc_day(diff, skill)
            if pred < tmp_pred:
                tmp_m = m
                tmp_pred = pred

        if tmp_m != -1:
            res.append([tmp_m, t])
            members[tmp_m] = t
            tasks[t] = 0

    return res



def feedback(task_difficulty, task_top5, pred_skills, task_member_days):
    for task, member, day in task_member_days:
        diff = task_difficulty[task]
        diff_top5 = task_top5[task]
        skill = pred_skills[member]
        pred_day = calc_day(diff, skill)

        day_gap = day - pred_day
        back = 0
        if day_gap > 5:
            back = -2
        elif day_gap > 2:
            back = -1
        elif day_gap < -2:
            back = 2
        elif day_gap < -5:
            back = 3

        for d in diff_top5:
            pred_skills[member][d] += back

        print("#s", member+1, *pred_skills[member])


def main():
    # Prior information
    N, M, K, R = NMI()
    task_difficulty = [NLI() for _ in range(N)]

    task_top5 = [[0]*5 for _ in range(N)]
    for i, diff in enumerate(task_difficulty):
        diff = [[d, j] for j, d in enumerate(diff)]
        diff = sorted(diff, reverse=True)
        for j in range(5):
            task_top5[i][j] = diff[j][1]

    task_dependency = [[] for _ in range(N)]
    for i in range(R):
        temp = NLI()
        task_dependency[temp[1] - 1].append(temp[0] - 1)

    # 技能予測値のベクトル
    pred_skills = [[10] * K for _ in range(M)]
    for m in range(M):
        print("#s", m+1, *pred_skills[m])
        sys.stdout.flush()

    if IS_LOCAL:
        # 真の技能値のベクトル
        true_skills = [NLI() for _ in range(M)]
        # 仕事iにメンバーjが費やす真の日数t[i][j]
        true_days = [NLI() for _ in range(N)]


    scheduler = Scheduler(N, M, is_local=IS_LOCAL)

    while True:
        #print(f"# day{scheduler.day} start")
        members = scheduler.member_status
        tasks = scheduler.task_status
        #print("#", members)
        #print("#", tasks)
        sys.stdout.flush()

        #assigns = greedy_assign(members, tasks, task_dependency)
        assigns = brute_force_assign(members, tasks, task_dependency,
                                     task_difficulty, pred_skills)
        assign_flat = " ".join(map(lambda x: str(x+1), chain(*assigns)))
        print(len(assigns), assign_flat)
        sys.stdout.flush()

        for member, task in assigns:
            need = 0
            if IS_LOCAL:
                need = true_days[task][member]
            scheduler.assign(task, member, need)

        if IS_LOCAL:
            task_member_days = scheduler.release()
            #print("#", res)
            if scheduler.day == 2000 or sum(scheduler.task_status) == N:
                exit()
        else:
            result = NLI()
            if result[0] == -1:
                exit()
            else:
                task_member_days = []
                for member in result[1:]:
                    member -= 1
                    task_member_days.append(scheduler.release_one(member))

        feedback(task_difficulty, task_top5, pred_skills, task_member_days)
        #print("#s", M, *pred_skills)
        #sys.stdout.flush()
        scheduler.add_day()


if __name__ == "__main__":
    main()
