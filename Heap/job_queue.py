# python3
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def assign_jobs2(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job
    return result


from heapq import heappop, heappush, heapify
def assign_jobs(n_workers, jobs):
    res = [(i, 0) for i in range(n_workers)]
    H = [(jobs[i], i) for i in range(n_workers)]
    heapify(H)
    for job in jobs[n_workers:]:
        t, i = heappop(H)
        res.append((i, t))
        heappush(H, (job + t, i))
    return res[:len(jobs)]


def assign_jobs2(n_workers, jobs):
    res = []
    H = []
    for job in jobs:
        if len(H) < n_workers:
            idx = len(H)
            res.append((idx, 0))
            heappush(H, (job, idx))
            continue
        t, i = heappop(H)
        res.append((i, t))
        heappush(H, (job + t, i))
    return res

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
