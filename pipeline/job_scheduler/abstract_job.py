"""
Seperating this out from job_scheduler.py to remove circular import
"""


from abc import ABC, abstractmethod



class JobScheduler(ABC):

    @abstractmethod
    def schedule_job(self, job, settings_overrides=None):
        pass
