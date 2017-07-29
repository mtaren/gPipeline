"""
Mock loader used for testing, or if you just don't want to save results.
"""

from abc import ABC, abstractmethod

from loader.abstract_loader import AbsLoader
from pipeline.settings import PipelineSettings


class MockLoader(AbsLoader):
    def __init__(self, params):
        super().__init__(params)

    def load(self, load_hash):
        """
        given the loader,  load the (previously ran) result if it exists
        :return: output dictionary,  or None if it does not exist
        """
        return None

    def save(self, dict, save_hash):
        """
        given the loader,  load the (previously ran) result if it exists
        :return: output dictionary,  or None if it does not exist
        """
        pass

