from enum import Enum,auto
from dataclasses import dataclass

class TokenType(Enum):
    KWD = auto()
    IDER = auto()
    LP = auto()
    RP = auto()
    LMP = auto()
    RMP = auto()
    OPC = auto()
    CMP = auto()
    EQL = auto()
    STPC = auto()
    EDL = auto()

@dataclass
class Token:
    t: TokenType
    v: str

class Lexer:
    def __init__(self, filename:str):
        self.kwds = [
            "fn","do","end","return",
            "if","else","elif","and","or"
            "match",
            "for","break",
            "var","num","str","arr"
        ]
        self.bsc = [
            ' ','"','\n'
        ]
        self.stc = [
            '+','-','*','/','{','}','[',']',
            '=','>','<','(',')','&'
        ]
        
        pass
    def get_tokens(self):
        pass