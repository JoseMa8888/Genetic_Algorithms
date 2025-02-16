from exceptions.ValueIsNone import ValueIsnone
from typing import Any


class Node:
    def __init__(self, value: str):
        """ 
        Arguments: 
        value   - str, it must be not None
        next    - can be anything, it is for linking Nodes 
        """
        if not value:
            raise ValueIsnone("Value must not be not None")
        
        self.__value: str = value
        self.__next: Any = None

    
    @property
    def value(self):
        #  Returns the value attribute
        return self.__value
    
    
    @property
    def next(self):
        #  Returns the next attribute
        return self.__next
    

    @value.setter
    def change_value(self, new_value):
        """
        Changes the value attribute of the instance
        
        Arguments:
        new_value   - str, it must be not None
        """
        if not new_value:
            raise ValueIsnone("The new_value must not be None")
        self.__value = new_value