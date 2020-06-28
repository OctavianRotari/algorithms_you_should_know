import unittest

from algorithms_you_should_know import Sorter

class TestSorterClass(unittest.TestCase):
    def setUp(self):
        self.sorter = Sorter([2, 1, 3, 5, 7, 4, 6])

    def test_initialization(self): 
        self.assertEqual(self.sorter.insertionSort(), [1, 2, 3, 4, 5, 6, 7], 'incorrect sorted order')

if __name__ == '__main__':
    unittest.main()
