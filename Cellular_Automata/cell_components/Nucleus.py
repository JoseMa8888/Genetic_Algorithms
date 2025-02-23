from exceptions.ValueIsNone import ValueIsnone
from exceptions.CircularStringInappropriate import CircularStringInappropriate
from .Table import *
from .CircularString import CircularString
from .Node import Node
from typing import List, Dict, Any

class Nucleus:
    def __init__(self, table: Table, circular_string: CircularString):
        """
        Arguments: 
        table   - Table, it must be not None
        reacircular_stringction    - CircularString, it must be not None

        We assume that the table is already correct
        We have to check if the circular_string has a not none root
        """
        if not table:
            raise ValueIsnone("Table must not be not None")
        
        if not circular_string or not circular_string.root:
            raise CircularStringInappropriate("The circular_string must not be None or it has not a root")

        self.__table: Table = table
        self.__dictionary_table: Dict[str, str] = table.set_dictionary()
        self.__circular_string: CircularString = circular_string


    @property
    def table(self) -> Table:
        return self.__table
    
    @property
    def dictionary_table(self) -> Dict[str, str]:
        return self.__dictionary_table
    
    @property
    def circular_string(self) -> CircularString:
        return self.__circular_string
    

    @circular_string.setter
    def circular_string(self, new_circular_string: CircularString):
        """
        Changes the circular_string attribute of the instance
        
        Arguments:
        new_circular_string   - CircularString, it must not be none and neither its root
        """
        if not new_circular_string or not CircularString.root:
            raise CircularStringInappropriate("The circular_string must not be None or it has not a root")
        self.__circular_string = new_circular_string

    
    def change_circular(self) -> CircularString:
        """
        Using the dictionary_table we change each value of CircularString using this transformation,
        We take the neighborhood of the first position and using the dictionary we change this first position
        into its reaction. Then we go to the after node and repeate this proccess. We should know that this must be
        repeated until we reaches the first position and all the values from the output Node should be changed properly:
        Don't use it to make reactions
        """
        length_neighborhood: int = len(self.table.neighborhood[0])
        left_right_neighbors: int = length_neighborhood // 2
        pos: Node = self.circular_string.root
        new_circular_string_list: List[str] = []
        i: int = 0
        while pos != self.circular_string.root or i <= 0:
            neighborhood: str = "".join(get_neighborhood(pos, left_right_neighbors))
            new_circular_string_list.append(self.dictionary_table[neighborhood])
            pos = pos.after
            if pos == self.circular_string.root:
                i = 1
        return create_test_circular_string(new_circular_string_list)


# Auxiliar function to get the neighborhood from a Node (we assume that it is circular) and number of neighbors
def get_neighborhood(pos: Node, number_neighbors: int) -> List[str]:
    list_neighbors_values_left: List[str] = []
    list_position_value: List[str] = [pos.value]
    list_neighbors_values_right: List[str] = []
    for _ in range(number_neighbors):
        list_neighbors_values_left.append(pos.before.value)
        list_neighbors_values_right.append(pos.after.value)
    list_neighbors_values_left = list_neighbors_values_left[::-1]
    return list_neighbors_values_left + list_position_value + list_neighbors_values_right


#Auxiliar function to create a circular_string, it gets a list of strings and connects all of them 
def create_test_circular_string(values: List[str]) -> CircularString:
    nodes = [Node(value) for value in values]
    for i in range(len(nodes)):
        nodes[i].after = nodes[(i + 1) % len(nodes)]
        nodes[i].before = nodes[(i - 1) % len(nodes)]
    circular_string = CircularString()
    circular_string.root = nodes[0]
    return circular_string
