"""
This global singleton                                                                                  
"""

"""
Todo - 
limit the number of threads
define a job scheduler factory class - ideally we can replace this with 
potentially other things off the main host computer.
"""

"""
How the queue works
1. Singleton class has a schedule_step function, returns a queue
2. main thread waits (blocking) for output to come back
3. PipelineQueue invokes a job scheduler specified by the settings. 


todo
create a settings singleton with these things in mind
    -  settings should be immutable after a point
    - get /set methods - no one should edit the internal settings manually

"""

class ExecutionPool(object):
    def __init__(self):
        self.executors = []
        self.pipeline_graph = None
