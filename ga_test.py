import unittest
import ga_6
from ga_6 import cxOrdered, mutShuffleIndexes
import graph_show

class Genetic_algrorithm(unittest.TestCase):
    def test_cxOrdered(self):
        res = cxOrdered([[3, 2, 4, 1, 0, 5], [5, 4, 2, 3, 1, 0], [5, 3, 1, 2, 0, 4], [5, 4, 0, 1, 2, 3], [1, 4, 0, 5, 2, 3], [4, 2, 5, 1, 0, 3]], [[0, 1, 2, 4, 5, 3], [2, 1, 0, 4, 5, 3], [0, 3, 5, 4, 2, 1], [0, 1, 4, 5, 3, 2], [5, 0, 2, 4, 3, 1], [1, 3, 5, 0, 4, 2]])
        resutltEqual =  cxOrdered([[3, 2, 4, 1, 0, 5], [5, 4, 2, 3, 1, 0], [5, 3, 1, 2, 0, 4], [5, 4, 0, 1, 2, 3], [1, 4, 0, 5, 2, 3], [4, 2, 5, 1, 0, 3]], [[0, 1, 2, 4, 5, 3], [2, 1, 0, 4, 5, 3], [0, 3, 5, 4, 2, 1], [0, 1, 4, 5, 3, 2], [5, 0, 2, 4, 3, 1], [1, 3, 5, 0, 4, 2]])
        self.assertEqual(res, resutltEqual)
    def test_mutShuffleIndexes(self):
        res = mutShuffleIndexes([[0, 2, 1, 4, 5, 3], [5, 2, 0, 1, 4, 3], [2, 0, 4, 1, 3, 5], [3, 1, 0, 2, 5, 4], [1, 0, 4, 3, 2, 5], [4, 5, 2, 1, 0, 3]], 0.0027777777777777775)
        resultEqual = [[0, 2, 1, 4, 5, 3], [5, 2, 0, 1, 4, 3], [2, 0, 4, 1, 3, 5], [3, 1, 0, 2, 5, 4], [1, 0, 4, 3, 2, 5], [4, 5, 2, 1, 0, 3]]
        self.assertEqual(res, resultEqual)
    def test_graph_show(self):
        res
        resultEqual
        self.assertEqual(res, resultEqual)
if __name__ == "__main__":
    unittest.main()