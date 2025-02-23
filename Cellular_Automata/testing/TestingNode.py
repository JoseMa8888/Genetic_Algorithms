import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from exceptions.ValueIsNone import ValueIsnone
from cell_components.Node import *
from typing import Any, List


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node1 = Node("1")
        self.node2 = Node("2")
        self.node3 = Node("3")


    def test_creating_node(self):
        self.assertIsInstance(self.node1, Node)
        self.assertEqual(self.node1.value, "1")


    def test_changing_value(self):
        self.node1.value = "10"
        self.assertEqual(self.node1.value, "10")

        with self.assertRaises(ValueIsnone):
            self.node1.value = None


    def test_changing_next(self):
        self.node1.next = self.node2
        self.assertEqual(self.node1.next, self.node2)

        with self.assertRaises(ValueIsnone):
            self.node1.next = None


    def test_circular(self):
        self.node1.next = self.node2
        self.node2.next = self.node3
        self.node3.next = self.node1 
        self.assertTrue(self.node1.is_circular())

if __name__ == "__main__":
    unittest.main()