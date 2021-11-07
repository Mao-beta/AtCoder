import sys
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def printf(*strings):
    print(*strings)
    sys.stdout.flush()


class Task:
    def __init__(self, ID, diff, pars, is_ready=False, assigned=None, is_complete=False):
        self.ID = ID
        self.diff = diff
        self.pars = pars
        self.is_ready = is_ready
        self.assigned = assigned
        self.is_complete = is_complete

    def assign(self, member_id):
        self.is_ready = False
        self.assigned = member_id

    def release(self):
        self.is_ready = False
        self.is_complete = True


class Member:
    def __init__(self, ID, true_skill, pred_skill, task=None, start=None):
        self.ID = ID
        self.true_skill = true_skill
        self.pred_skill = pred_skill
        self.task = task
        self.start = start

    def assign(self, task_id, day):
        self.task = task_id
        self.start = day

    def release(self):
        self.task = None
        self.start = None



class Scheduler:
    def __init__(self, N, M, K, R, is_local, true_days):
        self.N = N
        self.M = M
        self.K = K
        self.R = R
        self.is_local = is_local
        self.true_days = true_days
        self.day = 1
        self.events = [[] for _ in range(3001)]
        self.members = None
        self.tasks = None
        self.release_num = 0
        self.finish_flag = False
        self.free_member = self.M
        self.task_depth = None

    def register_members(self, pred_skills, true_skills):
        self.members = []

        for i, (ps, ts) in enumerate(zip(pred_skills, true_skills)):
            member = Member(ID=i, pred_skill=ps, true_skill=ts)
            self.members.append(member)

    def register_tasks(self, task_diffs, task_deps):
        self.tasks = []

        for i, (diff, pars) in enumerate(zip(task_diffs, task_deps)):
            task = Task(ID=i, diff=diff, pars=pars)
            self.tasks.append(task)

    def is_task_assignable(self, task):
        if task.assigned is not None:
            return False
        elif task.is_complete:
            return False
        else:
            pars = task.pars
            is_ready = True
            for par in pars:
                par_task = self.tasks[par]
                if not par_task.is_complete:
                    is_ready = False
            task.is_ready = is_ready
            return is_ready

    @staticmethod
    def calc_day(diff, skill):
        assert len(diff) == len(skill)
        w = sum([max(0, d - s) for d, s in zip(diff, skill)])
        if w == 0:
            return 1
        else:
            r = 0
            # r = random.randint(-3, 3)
            return max(1, w + r)

    def process_day(self):
        printf(f"# day{self.day} start")
        #printf(f"# {self.release_num}")
        self.assign()
        finish_members = self.work()
        self.release(finish_members)
        self.day += 1
        #printf(f"# {[[m.ID, m.task] for m in self.members]}")
        if self.finish_flag:
            exit()

    def assign(self):
        assigns = self.make_assigns_topological()
        self.output_assign(assigns)

    def output_assign(self, assigns: list):
        res = [len(assigns)]
        for member, task in assigns:
            res += [member.ID + 1, task.ID + 1]
        res = " ".join(map(str, res))
        printf(res)

    def modify_pred(self, member, new_skill):
        member.pred_skill = new_skill[:]
        printf("#s", member.ID+1, *new_skill)

    def make_assigns_topological(self):
        """
        :return: [Member, Task]のlist
        """
        assigns = []

        sorted_members = sorted(self.members, key=lambda x: sum(x.pred_skill))
        if self.task_depth is None:
            self.task_depth = self.task_topo()
            self.task_depth = [[d, i] for i, d in enumerate(self.task_depth)]
            self.task_depth.sort(key=lambda x: (x[0], -max(self.tasks[x[1]].diff)))
            printf("#", self.task_depth)

        for d, idx in self.task_depth:
            task = self.tasks[idx]
            if not self.is_task_assignable(task):
                continue

            diff = task.diff
            m_id = None
            m_day = 10000
            for member in sorted_members:
                if member.task is not None:
                    continue

                skill = member.pred_skill
                pred_day = self.calc_day(diff, skill)
                if pred_day < m_day:
                    m_id = member.ID
                    m_day = pred_day

            if m_day > 25 and self.free_member < 1:
                continue

            if m_id is not None:
                member = self.members[m_id]
                member.assign(task.ID, self.day)
                task.assign(member.ID)
                self.free_member -= 1
                if self.is_local:
                    elapse = self.true_days[task.ID][member.ID]
                    release_day = self.day + elapse - 1
                    self.events[release_day].append(member)
                assigns.append([member, task])

        return assigns

    def make_assigns_sorted_members_by_two(self):
        """
        :return: [Member, Task]のlist
        """
        assigns = []

        sorted_members = sorted(self.members, key=lambda x: sum(x.pred_skill))

        for task in self.tasks:
            if not self.is_task_assignable(task):
                continue

            diff = task.diff
            m_id = None
            m_day = 10000
            for member in sorted_members:
                if member.task is not None:
                    continue

                skill = member.pred_skill
                pred_day = self.calc_day(diff, skill)
                if pred_day < m_day:
                    m_id = member.ID
                    m_day = pred_day

            if m_day > 25 and self.free_member < 2:
                continue

            if m_id is not None:
                member = self.members[m_id]
                member.assign(task.ID, self.day)
                task.assign(member.ID)
                self.free_member -= 1
                if self.is_local:
                    elapse = self.true_days[task.ID][member.ID]
                    release_day = self.day + elapse - 1
                    self.events[release_day].append(member)
                assigns.append([member, task])

        return assigns

    def make_assigns_sorted_members(self):
        """
        :return: [Member, Task]のlist
        """
        assigns = []
        sorted_members = sorted(self.members, key=lambda x: sum(x.pred_skill))

        for task in self.tasks:
            if not self.is_task_assignable(task):
                continue

            diff = task.diff
            m_id = None
            m_day = 10000
            for member in self.members:
                if member.task is not None:
                    continue

                skill = member.pred_skill
                pred_day = self.calc_day(diff, skill)
                if pred_day < m_day:
                    m_id = member.ID
                    m_day = pred_day

            if m_id is not None:
                member = self.members[m_id]
                member.assign(task.ID, self.day)
                task.assign(member.ID)
                if self.is_local:
                    elapse = self.true_days[task.ID][member.ID]
                    release_day = self.day + elapse - 1
                    self.events[release_day].append(member)
                assigns.append([member, task])

        return assigns

    def make_assigns_brute_force(self):
        """
        コアの戦略部分, assign処理も行う
        :return: [Member, Task]のlist
        """
        assigns = []

        for task in self.tasks:
            if not self.is_task_assignable(task):
                continue

            diff = task.diff
            m_id = None
            m_day = 10000
            for member in self.members:
                if member.task is not None:
                    continue

                skill = member.pred_skill
                pred_day = self.calc_day(diff, skill)
                if pred_day < m_day:
                    m_id = member.ID
                    m_day = pred_day

            if m_id is not None:
                member = self.members[m_id]
                member.assign(task.ID, self.day)
                task.assign(member.ID)
                if self.is_local:
                    elapse = self.true_days[task.ID][member.ID]
                    release_day = self.day + elapse - 1
                    self.events[release_day].append(member)
                assigns.append([member, task])

        return assigns

    def make_assigns_only(self):
        """member0を酷使"""
        assigns = []

        for task in self.tasks:
            if not self.is_task_assignable(task):
                continue

            diff = task.diff
            member = self.members[0]
            if member.task is not None:
                return assigns

            member.assign(task.ID, self.day)
            task.assign(member.ID)
            if self.is_local:
                elapse = self.true_days[task.ID][member.ID]
                release_day = self.day + elapse - 1
                self.events[release_day].append(member)

            assigns.append([member, task])
            break

        return assigns


    def task_topo(self):
        topograph = [[] for _ in range(self.N)]
        for task in self.tasks:
            ID = task.ID
            adj = task.pars
            for p in adj:
                topograph[p].append(ID)

        depth = [self.N] * self.N

        for start in range(self.N):
            if depth[start] != self.N:
                continue
            que = deque([start])
            depth[start] = min(depth[start], 0)
            while que:
                now = que.popleft()
                now_depth = depth[now]
                for goto in topograph[now]:
                    if now_depth + 1 < depth[goto]:
                        que.append(goto)
                        depth[goto] = min(depth[goto], now_depth + 1)

        return depth


    def work(self):
        """
        その日にtaskを終えたMemberのリストを返す
        """
        if self.is_local:
            today = self.events[self.day]
            return today

        else:
            res = NLI()
            #printf("# " + str(res))
            if res[0] == -1:
                self.finish_flag = True
                return []
            elif res[0] == 0:
                return []
            else:
                res = [self.members[r-1] for r in res[1:]]
                return res

    def release(self, members):
        for member in members:
            elapsed = self.day - member.start + 1
            task_id = member.task
            task = self.tasks[task_id]
            pred = self.calc_day(task.diff, member.pred_skill)
            member.release()
            task.release()
            self.release_num += 1
            self.free_member += 1
            self.feedback(member, task, pred, elapsed)

        if self.is_local:
            if self.release_num >= self.N or self.day >= 2000:
                self.finish_flag = True


    def feedback(self, member, task, pred, elapsed):
        gap = elapsed - pred
        skill = member.pred_skill[:]
        diff = task.diff[:]
        diff_i = [[d, i] for i, d in enumerate(diff)]
        diff_i.sort(reverse=True)

        new_skill = skill[:]
        if elapsed <= 1:
            new_skill = [max(s, d) for s, d in zip(skill, diff)]
        elif gap > 5:
            for j in range(5):
                d, idx = diff_i[j]
                new_skill[idx] = max(0, skill[idx] - 2)
        elif gap > 2:
            for j in range(5):
                d, idx = diff_i[j]
                new_skill[idx] = max(0, skill[idx] - 1)
        elif gap < -5:
            for j in range(5):
                d, idx = diff_i[j]
                new_skill[idx] = skill[idx] + 3
        elif gap < -2:
            for j in range(5):
                d, idx = diff_i[j]
                new_skill[idx] = skill[idx] + 2


        self.modify_pred(member, new_skill)


def main():
    IS_LOCAL = False

    try:
        import numpy as np
        IS_LOCAL = True
    except Exception as e:
        pass

    # task数、member数、技能数、制約数
    N, M, K, R = NMI()
    # taskの難易度ベクトル
    task_difficulty = [NLI() for _ in range(N)]
    # task制約の隣接リスト
    task_dependency = [[] for _ in range(N)]
    for i in range(R):
        temp = NLI()
        task_dependency[temp[1] - 1].append(temp[0] - 1)

    pred_skills = [[10]*K for _ in range(M)]
    true_skills = [[None]*K for _ in range(M)]
    true_days = [[None]*M for _ in range(N)]

    if IS_LOCAL:
        # 真の技能値のベクトル
        true_skills = [NLI() for _ in range(M)]
        # 仕事iにメンバーjが費やす真の日数t[i][j]
        true_days = [NLI() for _ in range(N)]

    scheduler = Scheduler(N, M, K, R, is_local=IS_LOCAL, true_days=true_days)
    scheduler.register_members(pred_skills, true_skills)
    scheduler.register_tasks(task_difficulty, task_dependency)

    while True:
        scheduler.process_day()


if __name__ == "__main__":
    main()
