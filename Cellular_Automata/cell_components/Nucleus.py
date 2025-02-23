from Table import Table
from CircularString import CircularString
from typing import List
from exceptions.ValueIsNone import ValueIsnone
from exceptions.CircularStringInappropriate import CircularStringInappropriate


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
        
        if not circular_string or not CircularString.root:
            raise CircularStringInappropriate("The circular_string must not be None or it has not a root")

        self.__table: Table = table
        self.__circular_string: CircularString = circular_string


    @property
    def table(self) -> Table:
        return self.__table
    

    @property
    def circular_string(self) -> CircularString:
        return self.__circular_string
    

    @circular_string.setter
    def circular_string(self, new_circular_string: CircularString):
        if not new_circular_string or not CircularString.root:
            raise CircularStringInappropriate("The circular_string must not be None or it has not a root")
        self.__circular_string = new_circular_string