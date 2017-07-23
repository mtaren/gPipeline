"""
Pipeline objects are represented as a DAG, with a pointer to the parent.
each node will house the output of the node when finished.

TODO
for large outputs, may need to write to disk on the fly



API's the exectuion queue will use:
get_New_jobs()
    - returns a list of available nodes that can be run. will not
    ever return the same node twice.
is_finished()
    -returns True if there are no more nodes to run
    
"""


class PipelineGraph(object):
    def __init__(self):
        self.completed_nodes = []
        self.head = None
        self.nodes = []
        self.submitted_nodes = []  # nodes that were returned by get_new_jobs

    def _find_node_by_name(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        raise Exception("Error: no node named: " + name)

    def _get_ready_nodes(self, node):
        """
        return a list of nodes that have inputs ready, and have not finished.
        :return: 
        """
        if not node.is_finished():
            return [node]
        elif not node.edges:
            return []

        else:
            ready_nodes = []
            for node in node.edges:
                ready_nodes.extend(self._get_ready_nodes(node))
            return ready_nodes

    def add_node(self, parent_name, node):
        parent_node = self._find_node_by_name(parent_name)
        parent_node.edges.append(node)

    def get_new_jobs(self):
        """
        Gets any jobs that have not been returned by this function
        Calling this after completing a job does not guarantee a new job
        will be available, unless all currently running jobs are finished,
        and there are still available jobs left in the graph
        
        Do a BFS every time, since I don't see graphs being very big
        :return: 
        """
        pass

    def is_finished(self):
        """
        Returns True if no other node in the graph needs to be executed
        :return: 
        """
        if len(self.completed_nodes) == len(self.nodes):
            return True
        return False

    def is_valid(self):
        """
        Checks if the graph created is valid. 
        1. all nodes have unique names
        :return: 
        """
        raise NotImplementedError()
        pass
