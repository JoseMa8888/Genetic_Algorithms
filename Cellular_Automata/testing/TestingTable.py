import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from exceptions.NeighborhoodIncorrect import NeighborhoodIncorrect
from exceptions.ReactionIncorrect import ReactionIncorrect
from exceptions.ValueIsNone import ValueIsnone
from cell_components.Table import *

class TestTable(unittest.TestCase):

    def test_neighborhood_is_none(self):
        with self.assertRaises(ValueIsnone):
            Table(None, ["1", "0"])


    def test_reaction_is_none(self):
        with self.assertRaises(ValueIsnone):
            Table(["00", "01"], None)


    def test_neighborhood_incorrect(self):
        with self.assertRaises(NeighborhoodIncorrect):
            Table(["00", "01", "10"], ["1", "0", "1"])


    def test_reaction_incorrect(self):
        with self.assertRaises(ReactionIncorrect):
            Table(["00", "01", "10", "11"], ["1", "0", "10"])


    def test_neighborhood_unique(self):
        with self.assertRaises(NeighborhoodIncorrect):
            Table(["00", "01", "00", "11"], ["1", "0", "1", "1"])


    def test_neighborhood_length_exponent(self):
        with self.assertRaises(NeighborhoodIncorrect):
            Table(["00", "01", "10", "211"], ["1", "0", "1", "0"])


    def test_reaction_length_one(self):
        with self.assertRaises(ReactionIncorrect):
            Table(["00", "01", "10", "11"], ["10", "1", "10", "1"])


    def test_valid_neighborhood_and_reaction(self):
        table = Table(["00", "01", "10", "11"], ["1", "0", "1", "0"])
        self.assertEqual(table.neighborhood, ["00", "01", "10", "11"])
        self.assertEqual(table.reaction, ["1", "0", "1", "0"])


if __name__ == '__main__':
    unittest.main()
