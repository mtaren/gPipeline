"""
"""

from abc import ABC, abstractmethod

from pipeline.settings import PipelineSettings


class AbsAction(ABC):
    def __init__(self, input, loader):
        self.input = input
        self.loader = loader
        self.name = ''

    @abstractmethod
    def check_input(self):
        """
        Given the input params, check if the input is valid.
        Used to sanity check before kicking off long runs
        
        Raises an Exception if inputs are invalid
        """
        pass

    @abstractmethod
    def generate_output_hash(self):
        """
        Generate a hash based on the input and params. This hash is used 
        for future runs to prevent running the same calculations
        over and over again. Onus is on the User to create a good hash
        to prevent accidental reuse of wrong data.
        """
        pass

    @abstractmethod
    def load_output(self, output_hash):
        """
        given the loader,  load the (previously ran) result if it exists
        :return: output dictionary,  or None if it does not exist
        """
        pass

    @abstractmethod
    def run(self):
        """
        This is the meat of the action. Given the input, generate an output
        plus an output hash.
        
        If this is run it means that previous output was found
        
        :return: 
        """
        pass

    @abstractmethod
    def save_output(self, dict, output_hash):
        """
        given the loader,  load the (previously ran) result if it exists
        :return: output dictionary,  or None if it does not exist
        """
        pass

    @abstractmethod
    def tear_down(self):
        pass

    def main(self):
        """
        1. run check input
        2. generate output hash
        3. check if previous output exists, given hash
            - or if settings file specs out a clean.
        :return: 
        """
        self.check_input()
        output_hash = self.generate_output_hash()
        clean = PipelineSettings().clean
        if output_hash and not clean:
            result = self.load_output()
        else:
            result = self.run()
            self.save_output(result)

        self.tear_down()

        return result


