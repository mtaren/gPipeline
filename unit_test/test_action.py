"""
Uses the add action example to test the abstract action
"""

import unittest

from actions.toy.add import AddAction
from loader.mockloader import MockLoader

INPUT1 = 1
INPUT2 = 2

class ActionTest(unittest.TestCase):
    def setUp(self):
        input = {'param1': INPUT1, 'param2': INPUT2}
        loader = MockLoader({})
        self.action = AddAction(input, loader)


    def test_add(self):
        result = self.action.run().scaler_output
        self.assertEqual(result, INPUT1 + INPUT2)

if __name__ == '__main__':
    unittest.main()