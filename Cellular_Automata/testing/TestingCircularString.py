import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from exceptions.ValueIsNone import ValueIsnone
from exceptions.NodeNotCircular import NodeNotCircular
from cell_components.Node import *
from cell_components.CircularString import *


class TestCircularString(unittest.TestCase):

    def setUp(self):
        self.node1 = Node("A")
        self.node2 = Node("B")
        self.node3 = Node("C")
        self.node1.next = self.node2
        self.node2.next = self.node3
        self.node3.next = self.node1
        self.circular_string = CircularString()
    

    def test_create_circular_success(self):
        self.circular_string.root = self.node1
        self.assertEqual(self.circular_string.root, self.node1)

    
    def test_create_circular_with_none(self):
        with self.assertRaises(ValueIsnone):
            self.circular_string.root = None
    

    def test_create_circular_with_non_circular_node(self):
        non_circular_node = Node("X")
        with self.assertRaises(NodeNotCircular):
            self.circular_string.root = non_circular_node
    
    
    def test_get_list_value(self):
        self.circular_string.root = self.node1
        expected_values = ["A", "B", "C"]
        self.assertEqual(self.circular_string.get_list_value(), expected_values)


if __name__ == "__main__":
    unittest.main()
