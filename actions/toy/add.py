"""
"""

from abc import ABC, abstractmethod

from actions.abstract_action import AbsAction
from pipeline.settings import PipelineSettings
from result.result import Result


class AddAction(AbsAction):
    def __init__(self, input, loader):
        super().__init__(input, loader)
        self.name = 'adder'

    def check_input(self):
        """
        Checks if inputs are numbers 
        Raises an Exception if inputs are invalid
        """
        param1 = self.input['param1']
        param2 = self.input['param2']

        if not isinstance(param1, (int, float, complex)):
            raise Exception("Error: %s is not a valid number!" % str(param1))
        if not isinstance(param2, (int, float, complex)):
            raise Exception("Error: %s is not a valid number!" % str(param2))

    def generate_output_hash(self):
        """
        toy example, hash = result
        """
        param1 = self.input['param1']
        param2 = self.input['param2']
        return str(param1 + param2)

    def load_output(self, output_hash):
        """
        given the loader,  load the (previously ran) result if it exists
        :return: output dictionary,  or None if it does not exist
        """
        return self.loader.load(output_hash)
        pass

    def run(self):
        """
        This is the meat of the action. Given the input, generate an output
        plus an output hash.
        
        If this is run it means that previous output was found
        
        :return: a Result object 
        """
        param1 = self.input['param1']
        param2 = self.input['param2']
        output = Result()
        output.scaler_output = param1 + param2
        return output

    def save_output(self, dict, output_hash):
        """
        given the loader,  load the (previously ran) result if it exists
        :return: output dictionary,  or None if it does not exist
        """
        pass

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
            result = self.load_output(output_hash)
        else:
            result = self.run()
            self.save_output(result, output_hash)

        self.tear_down()

        return result
