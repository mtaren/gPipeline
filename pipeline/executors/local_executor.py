"""

executor that runs on the local machine. Simplest executor

"""

from abc import ABC, abstractmethod
from threading import Thread

from pipeline.executors.abstract_executor import AbsExecutor


class LocalExecutor(AbsExecutor):
    def __init__(self, result_queue, callback):
        super().__init__(result_queue, callback)

    def _execute_work(self, input, node):
        """
        super simple, do the work locally
        """
        return node.action.main()


