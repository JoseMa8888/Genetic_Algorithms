from exceptions.ValueIsNone import ValueIsnone
from typing import Any

class Node:
    def __init__(self, value: str) -> None:
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
    def value(self) -> str:
        #  Returns the value attribute
        return self.__value
    

    @value.setter
    def value(self, new_value: str) -> None:
        """
        Changes the value attribute of the instance
        
        Arguments:
        new_value   - str, it must be not None
        """
        if not new_value:
            raise ValueIsnone("The new_value must not be None")
        self.__value = new_value

    
    @property
    def next(self) -> Any:
        #  Returns the next attribute
        return self.__next
    

    @next.setter
    def next(self, new_node) -> None:
        """
        Changes the next attribute of the instance
        
        Arguments:
        new_node   - Node, it must be not None
        """
        if not new_node:
            raise ValueIsnone("The new_node must not be None")
        self.__next = new_node

    
    def is_circular(self) -> bool:
        """
        Return true if the node is circular.
        We consider the node being circular if we can return to the 
        first node walking through the structure
        """
        try:
            next = self.next
            i: int = 0
            while next != self and i < 1000000:
                next = next.next
                i += 1
            return next == self
        except:
            return False