from exceptions.NeighborhoodIncorrect import NeighborhoodIncorrect
from exceptions.ReactionIncorrect import ReactionIncorrect
from exceptions.ValueIsNone import ValueIsnone
from typing import List, Dict


class Table:
    def __init__(self, neighborhood: List[str], reaction: List[str]) -> None:
        """
        Arguments: 
        neighborhood   - List[str], it must be not None
        reaction    - List[str], it must be not None

        The neighborhood is a list of string of 0 and 1, the length must be 2 ** length of each string,
        they must be unique and each of the string has the same lenght

        Reaction is the output for the neighborhood, it could be a string of 0 or 1, the length of neighborhood
        and reaction is the same, but reaction contains only strings of length one.
        """
        if not neighborhood:
            raise ValueIsnone("Neighborhood must not be not None")
        
        if not reaction:
            raise ValueIsnone("Reaction must not be not None")
        
        if not self.neighborhood_correct(neighborhood):
            raise NeighborhoodIncorrect("The neightborhood is not propriate")
        
        if not self.reaction_correct(reaction, neighborhood):
            raise  ReactionIncorrect("The neightborhood is not propriate")
        
        self.__neighborhood: List[str] = neighborhood
        self.__reaction: List[str] = reaction


    def neighborhood_correct(self, neighborhood: List[str]):
        # Returns true if respects the specifications
        length: int = len(neighborhood)
        exponent: int = len(neighborhood[0])
        is_exponent: bool = 2**exponent == length
        unicos: bool = length == len(set(neighborhood))
        same_lenght_string: bool = all([len(i)==exponent for i in neighborhood])
        return is_exponent and unicos and same_lenght_string


    def reaction_correct(self, reaction: List[str], neighborhood: List[str]):
        # Returns true if respects the specifications
        lenght_reaction: int = len(reaction)
        lenght_neighborhood: int = len(neighborhood)
        same_length: bool = lenght_neighborhood == lenght_reaction
        lenght_one: bool = all([len(i)==1 for i in reaction])
        return same_length and lenght_one


    @property
    def neighborhood(self) -> List[str]:
        return self.__neighborhood


    @property
    def reaction(self) -> List[str]:
        return self.__reaction