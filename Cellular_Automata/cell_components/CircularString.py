from exceptions.ValueIsNone import ValueIsnone
from exceptions.NodeNotCircular import NodeNotCircular

from .Node import Node
from typing import Any, List


class CircularString():
    def __init__(self):
        # This structure is based on a CircularQueue
        self.__root: Any = None


    @property
    def root(self) -> Any:
        # Getter for the root attribute
        return self.__root


    @root.setter
    def root(self, node: Node) -> None:
        """
        Changes the root of the instance
        
        Arguments:
        node   - Node, it must be not None the node must be circular
        """
        if not node:
            raise ValueIsnone("The node is None")
        if not node.is_circular():
            raise NodeNotCircular("The node is not circular")
        self.__root = node
    
    
    def get_list_value(self) -> List[str]:
        # It gets all values from the circularString
        pos: Node = self.root
        result: List[str] = [pos.value]
        pos = pos.after
        while pos != self.root:
            result.append(pos.value)
            pos = pos.after
        return result
