from .Cell import Cell 
from .Node import Node
from .Nucleus import *
from .Table import *
from .CircularString import *
from uuid import uuid4
import random
from typing import List
from exceptions.IntegerError import IntegerError
from exceptions.ValueIsNone import ValueIsnone
import tkinter as tk

class Cell_v1(Cell):
    def __init__(self, time: int, length_string: None, length_node: None, circular_string: None, table: Table) -> None:
        """ 
        First version of Cell. In this version we will be working with a simple version of a nucleus which compounds with a table and
        a circular string in which the "DNA" is placed.

        Arguments: 
        length_string   - int, if circular_string does not exist and it is greater than 1
        length_node    - int, if circular_string does not exist and it is greater than 0
        circular_string - CircularString, if circular_string exists
        table   - Table, it is a well built Table
        """
        super().__init__(time)
        
        if circular_string:
            self.__nucleus: Nucleus = Nucleus(table, circular_string) 

        elif not circular_string and length_string and length_node:
            if length_string <= 1:
                raise IntegerError("Length String must be greater than 1")
        
            if length_node <= 0:
                raise IntegerError("Length Node must be greater than 0")
            
            self.__nucleus: Nucleus = self.create_random_nucleus(table, length_string, length_node)

        else:
            raise ValueIsnone("Some values are none and it must not")


    def create_random_nucleus(self, table: Table, length_string: int, length_node: int) -> Nucleus:
        """
        It creates a random nucleus if the circular string is not passed.
        Arguments: 

        length_string   - int, the length of the new random circular string
        length_node    - int, the length of each node of the random circular string
        table   - Table, the table needed for creating the nucleus
        """
        list_values: List[str] = ["".join(map(str,[random.randint(0,1) for _ in range(length_node)])) for _ in range(length_string)]
        circular_string: CircularString = create_test_circular_string(list_values)
        nucleus: Nucleus = Nucleus(table, circular_string)
        return nucleus
        

    def change_nucleus(self) -> List[Nucleus]:
        """
        It creates a list of transformations of the Nucleus.
        The number of transformations depends on the time and they are storaged in a List
        """
        result: List[Nucleus] = []
        new_nucleus: Nucleus = self.__nucleus
        result.append(new_nucleus)
        for _ in self.__time:
            new_string: CircularString = self.__nucleus.change_circular()
            new_nucleus = Nucleus(new_nucleus.table, new_string)
            result.append(new_nucleus)
        return result


    def paint_changing_nucleus(self) -> None:
        """
        It paints with tkinter all the transformations. 
        Each node value will be summed internally for creating a single integer which and the number of colors will depend on the lenght of the values nodes.
        **(In this version we are working with nodes of length one)**
        """
        list_transformations: List[Nucleus] = self.change_nucleus()
        root = tk.Tk()
        root.title("Painting squares")
        length_square: float = (root.winfo_screenwidth()-500) / (self.__length_string)
        for nucleus in list_transformations:
            self.paint_one_nucleus(nucleus, length_square, root)
        root.mainloop()


    def paint_one_nucleus(self, nucleus: Nucleus, length_rect: float, root) -> None:
        """
        Paints only one trasformation.
        Arguments:
        nucleus - Nucleus, it contains the CircularString needed for the painting
        length_rect - float, it is the length of the rectangle (squares are rectangles)
        root    - the root of the tkinters screen.
        """

        list_values: str = nucleus.circular_string.get_list_value
        canvas = tk.Canvas(root, width=len(list_values) * length_rect, height=length_rect)
        canvas.pack()
        for i, valor in enumerate(list_values):
            color = "black" if valor == 1 else "white"
            canvas.create_rectangle(
                i * length_rect, 0, 
                (i + 1) * length_rect, length_rect, 
                fill=color, outline=""
            )
