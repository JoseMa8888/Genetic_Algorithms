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

    
    def test_neighborhood_not_odd(self):
        with self.assertRaises(NeighborhoodIncorrect):
            Table(["00", "01", "10", "11"], ["1", "0", "1", "0"])


    def test_neighborhood_incorrect(self):
        with self.assertRaises(NeighborhoodIncorrect):
            Table(["000", "001", "010"], ["1", "0", "1"])


    def test_neighborhood_unique(self):
        with self.assertRaises(NeighborhoodIncorrect):
            Table(["000", "001", "000", "011", "100", "101", "110", "111"], ["1", "0", "1", "1"])


    def test_neighborhood_length_exponent(self):
        with self.assertRaises(NeighborhoodIncorrect):
            Table(["000", "001", "010", "011", "100", "101", "1101", "111"], ["1", "0", "1", "0"])


    def test_reaction_incorrect(self):
        with self.assertRaises(ReactionIncorrect):
            Table(["000", "001", "010", "011", "100", "101", "110", "111"], ["1", "0", "0"])


    def test_reaction_length_one(self):
        with self.assertRaises(ReactionIncorrect):
            Table(["000", "001", "010", "011", "100", "101", "110", "111"], ["10", "1", "10", "1", "1", "0", "1", "0"])


    def test_valid_neighborhood_and_reaction(self):
        table = Table(["000", "001", "010", "011", "100", "101", "110", "111"], ["0", "1", "0", "1", "1", "0", "1", "0"])
        self.assertEqual(table.neighborhood, ["000", "001", "010", "011", "100", "101", "110", "111"])
        self.assertEqual(table.reaction, ["0", "1", "0", "1", "1", "0", "1", "0"])

        
    def test_set_dictionary(self):
            neighborhood = ["000", "001", "010", "011", "100", "101", "110", "111"]
            reaction = ["0", "1", "0", "1", "1", "0", "1", "0"]
            table = Table(neighborhood, reaction)
            expected_dict = {
                "000": "0",
                "001": "1",
                "010": "0",
                "011": "1",
                "100": "1",
                "101": "0",
                "110": "1",
                "111": "0"
            }
            self.assertEqual(table.set_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
