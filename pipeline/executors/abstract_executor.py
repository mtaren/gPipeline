"""

purposed of executor

call the methods of the "action" object that is passed in

deal with the different platforms of executing code.


"""

from abc import ABC, abstractmethod
from threading import Thread


class AbsExecutor(ABC):
    def __init__(self, result_queue, callback):
        self.result_q = result_queue
        self.callback_func = callback
        self.busy = False

    @abstractmethod
    def _execute_work(self, input, node):
        """
        commonly overridden function to do work locally/remote/specialized
        
        :param input: 
        :param node: 
        :return: dict , result
        """

        pass

    def start_execution(self, input, node):
        """
        kicks this thread off, should 'immediately' return
        This should be common across all executors
        :param input: 
        :param node: 
        :return: 
        """
        self.busy = True
        # start thread
        thread = Thread(target=self.executor_thread, args=(input, node))
        thread.start()

    def executor_thread(self, input, node):
        # TODO record metrics (time taken)
        try:
            result = self._execute_work(input, node)
        except Exception as e:
            result = "Error Running %s: %s" % (node.name, str(e))

        self.result_q.put(result)
        self.busy = False
        self.callback_func()
