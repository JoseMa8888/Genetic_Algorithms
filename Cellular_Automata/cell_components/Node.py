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
        self.__before: Any = None
        self.__after: Any = None

    
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
    def before(self) -> Any:
        return self.__before
    
    @property
    def after(self) -> Any:
        return self.__after
    

    @before.setter
    def before(self, new_node) -> None:
        """
        Changes the before attribute of the instance
        
        Arguments:
        new_node   - Node, it must be not None
        """
        if not new_node:
            raise ValueIsnone("The new_node must not be None")
        self.__before = new_node


    @after.setter
    def after(self, new_node) -> None:
        """
        Changes the after attribute of the instance
        
        Arguments:
        new_node   - Node, it must be not None
        """
        if not new_node:
            raise ValueIsnone("The new_node must not be None")
        self.__after = new_node

    
    def is_circular(self) -> bool:
        """
        Return true if the node is circular.
        We consider the node being circular if we can return to the 
        first node walking through the structure through after and before
        """
        try:
            node_after = self.after
            node_before = self.before
            i: int = 0
            while node_after != self and node_before != self and i < 1000000:
                if node_after != self:
                    node_after = node_after.after
                if node_before != self:
                    node_before = node_before.before
                i += 1
            if i > 1000000:
                return False
            return True
        except:
            return False