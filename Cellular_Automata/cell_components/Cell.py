from uuid import uuid4
from exceptions.IntegerError import IntegerError

class Cell:
    
    def __init__(self, time: int) -> None:
        """ 
        The Cell is a component of the evolution. This is the father of all following versions of cell.
        Those Cell will have different components, structures and methos for their corresponding development. 
        
        Arguments: 
        time    - int, it must be greater than 0
        """

        if time <= 0:
            raise IntegerError("Time value must be greater than 0")
        
        self.__time: int = time
        self.__id = uuid4() # Creating an id for storage

