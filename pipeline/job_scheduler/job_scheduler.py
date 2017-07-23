"""
"""
from pipeline.job_scheduler.local_job import LocalJobScheduler

"""
Todo - 
methods:
schedule_job
    - either creates a thread )base), or submits a job to a job scheduler
    - returns a object that you can call "wait" on, or check if result done yet
    
flow would be something like
- Executor gets a job. calls schedule_job on that job
- Executor waits for that job to finish, potentially waiting for other jobs
lto finish as well.

"""


def get_scheduler(sched_type):
    # return eval(type + "()")
    if sched_type == "Circle": return LocalJobScheduler()
    raise Exception("Unsupported Scheduler: " + sched_type)
