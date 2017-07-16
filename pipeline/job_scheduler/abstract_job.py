"""
Seperating this out from job_scheduler.py to remove circular import
"""


from abc import ABC, abstractmethod

from pipeline.job_scheduler.local_job import LocalJobScheduler


class JobScheduler(ABC):

    @abstractmethod
    def schedule_job(self, job, settings_overrides=None):
        pass
