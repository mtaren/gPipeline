"""
This global singleton                                                                                  
"""
from utils.singleton import Singleton

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
3. PipelineQueue invokes a job schedular specified by the settings. 


todo
create a settings singleton with these things in mind
    -  settings should be immutable after awhile
    - get /set methods - no one should edit the internal settings manually

"""

class PipelineQueue(metaclass=Singleton):
    pass
