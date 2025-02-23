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


    def test_changing_after_before(self):
        self.node1.after = self.node2
        self.node1.before = self.node3
        self.assertEqual(self.node1.after, self.node2)
        self.assertEqual(self.node1.before, self.node3)

        with self.assertRaises(ValueIsnone):
            self.node1.after = None


    def test_is_circular(self):
        node1 = Node("A")
        node2 = Node("B")
        node3 = Node("C")
        
        node1.after = node2
        node2.after = node3
        node3.after = node1
        
        node1.before = node3
        node2.before = node1
        node3.before = node2
        
        self.assertTrue(node1.is_circular())
        self.assertTrue(node2.is_circular())
        self.assertTrue(node3.is_circular())
        

if __name__ == "__main__":
    unittest.main()