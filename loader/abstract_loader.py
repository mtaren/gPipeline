"""
"""

from abc import ABC, abstractmethod

from pipeline.settings import PipelineSettings


class AbsLoader(ABC):
    def __init__(self, params):
        pass

    @abstractmethod
    def load(self, load_hash):
        """
        given the loader,  load the (previously ran) result if it exists
        :return: result object,  or None if it does not exist
        """
        pass

    @abstractmethod
    def save(self, dict, save_hash):
        """
        given the loader,  load the (previously ran) result if it exists
        :return: output dictionary,  or None if it does not exist
        """
        pass

