import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cell_components.Table import *
from cell_components.CircularString import CircularString
from cell_components.Node import Node
from cell_components.Nucleus import *
from exceptions.ValueIsNone import ValueIsnone
from exceptions.CircularStringInappropriate import CircularStringInappropriate
 


class TestNucleus(unittest.TestCase):

    def test_create_test_circular_string(self):
        values = ["A", "B", "C", "D"]
        circular_string = create_test_circular_string(values)
        self.assertIsNotNone(circular_string.root, "La raíz no debe ser None")
        current = circular_string.root
        for expected_value in values:
            self.assertEqual(current.value, expected_value, f"El nodo debería tener el valor {expected_value}")
            current = current.after
        self.assertEqual(current.value, values[0], "El último nodo debe enlazar de vuelta al primero")
        current = circular_string.root
        for i in range(len(values)):
            next_node = current.after
            prev_node = current.before
            self.assertEqual(next_node.value, values[(i + 1) % len(values)], "El puntero 'after' es incorrecto")
            self.assertEqual(prev_node.value, values[(i - 1) % len(values)], "El puntero 'before' es incorrecto")
            current = next_node


    def setUp(self):
        self.neighborhood = ["000", "001", "010", "011", "100", "101", "110", "111"]
        self.reaction = ["0", "1", "1", "0", "1", "0", "0", "1"]
        self.table = Table(self.neighborhood, self.reaction)
        self.circular_string = create_test_circular_string(["0", "1", "0", "1", "1", "0", "1", "0", "1", "0"])


    def test_initialization(self):
        nucleus = Nucleus(self.table, self.circular_string)
        self.assertEqual(nucleus.table, self.table)
        self.assertEqual(nucleus.circular_string, self.circular_string)
        self.assertEqual(nucleus.dictionary_table, self.table.set_dictionary())


    def test_initialization_invalid_table(self):
        with self.assertRaises(ValueIsnone):
            Nucleus(None, self.circular_string)
    

    def test_initialization_invalid_circular_string(self):
        with self.assertRaises(CircularStringInappropriate):
            Nucleus(self.table, None)


    def test_initialization_circular_string_no_root(self):
        with self.assertRaises(CircularStringInappropriate):
            Nucleus(self.table, CircularString())


    def test_get_neighborhood(self):
        node_values = ["0", "1", "0", "1", "1", "0", "1", "0", "1", "0"]
        circular_string = create_test_circular_string(node_values)
        node = circular_string.root.after.after  # Selecting a middle node
        neighborhood = get_neighborhood(node, 1)
        expected_neighborhood = ["1", "0", "1"]
        self.assertEqual(neighborhood, expected_neighborhood)


    def test_change_circular(self):
        nucleus = Nucleus(self.table, self.circular_string)
        new_circular_string: CircularString = nucleus.change_circular()
        pos = new_circular_string.root
        expected_values = [nucleus.dictionary_table["001"], nucleus.dictionary_table["010"],
                           nucleus.dictionary_table["101"], nucleus.dictionary_table["011"],
                           nucleus.dictionary_table["110"], nucleus.dictionary_table["101"],
                           nucleus.dictionary_table["010"], nucleus.dictionary_table["101"],
                           nucleus.dictionary_table["010"], nucleus.dictionary_table["100"]]
        for expected in expected_values:
            self.assertEqual(pos.value, expected)
            pos = pos.after
            if pos == new_circular_string.root:
                break

if __name__ == "__main__":
    unittest.main()
