"""
Pipline Nodes will populate the pipeline DAG
Nodes within a graph must have unique names, usually defined by user.
"""

NOT_FINISHED = 'not_finished'


class PipelineNode(object):
    def __init__(self):
        self.edges = []
        self.executor_type = 'default'
        self.name = ""
        self.output = NOT_FINISHED
        self.parent = None

    def is_finished(self):
        if self.output == NOT_FINISHED:
            return False
        return True
