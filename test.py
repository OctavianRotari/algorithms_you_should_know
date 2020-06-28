import unittest

from algorithms import Sorter

class TestSorterClass(unittest.TestCase):
    def setUp(self):
        self.sorter = Sorter([2, 1, 3])

    def test_initialization(self): 
        self.assertEqual(self.sorter.insertionSort(), [1, 2, 3], 'incorrect sorted order')
