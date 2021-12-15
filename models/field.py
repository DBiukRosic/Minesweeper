from typing import List
from enum import Enum

class Type(Enum):
    bomb = 1
    empty = 0

class Field():
    def __init__(self,is_hidden: bool, surrounding_bombs: int, type: Type):
        self.is_hidden = is_hidden
        self.surrounding_bombs = surrounding_bombs
        self.type = type
 
    def __repr__(self):
        field_string = (f"{self.type.name} - {self.is_hidden} - {self.surrounding_bombs}")
        return field_string