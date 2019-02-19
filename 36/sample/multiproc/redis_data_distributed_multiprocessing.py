import multiprocessing
import redis
import random
import time

def read_from_redis(jobs):
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    while True:
        data = r.rpop('test')

        if data is not None:
            jobs.put_nowait(data)

class Processing_task():
    def __init__(self, wk_id, jobs):
        self.wk_id = wk_id
        self.jobs  = jobs

    def do_process(self):
        task_process = multiprocessing.Process(target=self.task, args = (jobs,))
        task_process.start()

        return task_process

    def task(self, jobs):

        while True:
            data = jobs.get()
            slp_tm = random.uniform(0.3, 1.0)

            time.sleep(slp_tm)

            print('wk_id %s : data %s : slp_tm %f' %(self.wk_id, data, slp_tm))

if __name__ == '__main__':
    jobs = multiprocessing.Queue(maxsize = 600)

    read_process = multiprocessing.Process(target=read_from_redis, args = (jobs,))
    read_process.start()

    tasks = []
    for i in range(1,4):
        pt = Processing_task(i, jobs)
        pt.do_process()

        tasks.append(pt)

    read_process.join()

    [p.join() for p in tasks]
