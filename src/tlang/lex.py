from enum import Enum,auto
from dataclasses import dataclass

class TokenType(Enum):
    KWD = auto()    # 关键字
    STR = auto()    # 字符串
    IDER = auto()   # 标识符
    LP = auto()     # (
    RP = auto()     # )
    LMP = auto()    # [
    RMP = auto()    # ]
    LLP= auto()     # {
    RLP = auto()    # }
    OPC = auto()    # +-*/&
    CMP = auto()    # > < >= <= ==
    EQL = auto()    # =
    EXP = auto()    # $
    SEM = auto()    # :
    EDL = auto()    # 行终止符 "\n"

SYMBLE_TABLE:dict = {
    '(': TokenType.LP,
    ')': TokenType.RP,
    '[': TokenType.LMP,
    ']': TokenType.RMP,
    '{': TokenType.LLP,
    '}': TokenType.RLP,
    '=': TokenType.EQL,
    '+': TokenType.OPC,
    '-': TokenType.OPC,
    '*': TokenType.OPC,
    '/': TokenType.OPC,
    '&':TokenType.OPC,
    '>=': TokenType.CMP,
    '<=': TokenType.CMP,
    '==': TokenType.CMP,
    '>': TokenType.CMP,
    '<': TokenType.CMP,
    ':': TokenType.SEM
}

@dataclass
class Token:
    type_:  TokenType
    value_: str
    def __repr__(self):
        return f"({self.type_.name} : {self.value_})"

class Lexer:
    def __init__(self, filename:str):
        self.kwds = [
            "fn","do","end","return",
            "if","else","elif","and","or"
            "match",
            "for","break","cont",
            "var","num","str","arr"
        ]
        self.bsc = [
            ' ','"','\n','\t'
        ]
        self.stc = [
            '+','-','*','/','{','}','[',']',
            '=','>','<','(',')','&','$',':'
        ]
        self.mixable_c = [ # 可能混合的字符 
            '>','<','='
        ]
        # 读取文件
        self.fc: str = ""
        with open(filename, 'r', encoding="utf-8") as fp:
            self.fc = fp.read()
        
    def get_token_type(self,s: str)->(TokenType|None):
        if s == "":
            return None
        if not SYMBLE_TABLE.get(s) is None:
            return SYMBLE_TABLE.get(s)
        if s in self.kwds:
            return TokenType.KWD
        return TokenType.IDER
        
    def get_tokens(self) -> list[Token]:
        tokens: list[Token] = []
        tmp_str: str = ""
        for pos in range(len(self.fc)):
            if self.fc[pos] in self.bsc:
                if tmp_str != "":
                    tokens.append(Token(
                        type_ = self.get_token_type(tmp_str),
                        value_= tmp_str
                    ))
                    tmp_str = ""
                if self.fc[pos] == '"':            # 处理字符串
                    while self.fc[pos+1] != '"':
                        tmp_str += self.fc[pos]
                    pos+=1
                    tokens.append(Token(
                        type_=TokenType.STR,
                        value_=tmp_str
                    ))
                    tmp_str = ""
                    continue
                continue
            elif self.fc[pos] in self.stc:
                stc: str = self.fc[pos]
                if self.fc[pos] in self.mixable_c and self.fc[pos+1]=='=':
                    stc += self.fc[pos]
                    pos = pos+1
                if not self.get_token_type(tmp_str) is None:
                    tokens.append(Token(
                        type_= self.get_token_type(tmp_str),
                        value_=tmp_str
                    ))
                tokens.append(Token(
                    type_= self.get_token_type(stc),
                    value_=stc
                ))
                tmp_str = ""
                continue
            tmp_str += self.fc[pos]
        if tmp_str != "":
            tokens.append(Token(
                type_=self.get_token_type(tmp_str),
                value_=tmp_str
            ))
        #end
        return tokens
            