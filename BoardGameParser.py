# Generated from BoardGameParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,75,335,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,4,0,52,8,0,11,0,12,
        0,53,1,0,1,0,1,1,1,1,1,1,3,1,61,8,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,
        1,2,1,2,1,3,4,3,73,8,3,11,3,12,3,74,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,87,8,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,96,8,7,10,
        7,12,7,99,9,7,1,7,1,7,1,7,1,7,1,7,5,7,106,8,7,10,7,12,7,109,9,7,
        1,7,1,7,1,7,1,7,1,7,5,7,116,8,7,10,7,12,7,119,9,7,1,7,1,7,1,7,1,
        7,1,7,1,7,5,7,127,8,7,10,7,12,7,130,9,7,1,7,1,7,1,7,3,7,135,8,7,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,147,8,9,10,9,12,9,150,
        9,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,158,8,9,10,9,12,9,161,9,9,1,9,1,
        9,1,9,1,9,1,9,1,9,5,9,169,8,9,10,9,12,9,172,9,9,3,9,174,8,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,184,8,10,1,11,1,11,1,12,
        1,12,1,12,1,12,1,12,1,12,3,12,194,8,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,208,8,12,10,12,12,12,211,
        9,12,1,13,1,13,1,13,1,13,5,13,217,8,13,10,13,12,13,220,9,13,1,14,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,3,15,239,8,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,3,18,264,8,18,1,19,1,19,1,19,1,19,1,19,1,19,3,19,
        272,8,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,282,8,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,292,8,19,1,19,1,19,3,
        19,296,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,3,20,310,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,3,21,324,8,21,1,22,1,22,1,22,1,22,1,22,1,23,1,
        23,1,23,1,23,1,23,0,1,24,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,0,4,3,0,3,5,9,12,14,14,1,0,68,71,1,
        0,30,31,2,0,45,48,50,53,358,0,48,1,0,0,0,2,57,1,0,0,0,4,66,1,0,0,
        0,6,72,1,0,0,0,8,86,1,0,0,0,10,88,1,0,0,0,12,90,1,0,0,0,14,134,1,
        0,0,0,16,136,1,0,0,0,18,173,1,0,0,0,20,183,1,0,0,0,22,185,1,0,0,
        0,24,193,1,0,0,0,26,212,1,0,0,0,28,221,1,0,0,0,30,238,1,0,0,0,32,
        240,1,0,0,0,34,245,1,0,0,0,36,263,1,0,0,0,38,295,1,0,0,0,40,309,
        1,0,0,0,42,323,1,0,0,0,44,325,1,0,0,0,46,330,1,0,0,0,48,49,5,1,0,
        0,49,51,5,72,0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,53,1,0,0,0,53,51,
        1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,3,4,2,0,56,1,1,0,0,0,57,
        60,5,2,0,0,58,61,5,72,0,0,59,61,3,18,9,0,60,58,1,0,0,0,60,59,1,0,
        0,0,61,62,1,0,0,0,62,63,5,58,0,0,63,64,3,6,3,0,64,65,5,26,0,0,65,
        3,1,0,0,0,66,67,5,25,0,0,67,68,5,58,0,0,68,69,3,6,3,0,69,70,5,26,
        0,0,70,5,1,0,0,0,71,73,3,8,4,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,
        1,0,0,0,74,75,1,0,0,0,75,7,1,0,0,0,76,87,3,28,14,0,77,87,3,38,19,
        0,78,87,3,30,15,0,79,87,3,32,16,0,80,87,3,34,17,0,81,87,3,36,18,
        0,82,87,3,40,20,0,83,87,3,42,21,0,84,87,3,46,23,0,85,87,3,44,22,
        0,86,76,1,0,0,0,86,77,1,0,0,0,86,78,1,0,0,0,86,79,1,0,0,0,86,80,
        1,0,0,0,86,81,1,0,0,0,86,82,1,0,0,0,86,83,1,0,0,0,86,84,1,0,0,0,
        86,85,1,0,0,0,87,9,1,0,0,0,88,89,7,0,0,0,89,11,1,0,0,0,90,91,7,1,
        0,0,91,13,1,0,0,0,92,97,5,72,0,0,93,94,5,60,0,0,94,96,5,72,0,0,95,
        93,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,135,1,0,
        0,0,99,97,1,0,0,0,100,101,5,72,0,0,101,102,5,49,0,0,102,107,3,12,
        6,0,103,104,5,60,0,0,104,106,3,14,7,0,105,103,1,0,0,0,106,109,1,
        0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,135,1,0,0,0,109,107,1,
        0,0,0,110,111,5,72,0,0,111,112,5,49,0,0,112,117,5,72,0,0,113,114,
        5,60,0,0,114,116,3,14,7,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,
        1,0,0,0,117,118,1,0,0,0,118,135,1,0,0,0,119,117,1,0,0,0,120,121,
        5,72,0,0,121,122,5,49,0,0,122,135,3,12,6,0,123,128,3,12,6,0,124,
        125,5,60,0,0,125,127,3,14,7,0,126,124,1,0,0,0,127,130,1,0,0,0,128,
        126,1,0,0,0,128,129,1,0,0,0,129,135,1,0,0,0,130,128,1,0,0,0,131,
        135,5,34,0,0,132,135,5,33,0,0,133,135,5,32,0,0,134,92,1,0,0,0,134,
        100,1,0,0,0,134,110,1,0,0,0,134,120,1,0,0,0,134,123,1,0,0,0,134,
        131,1,0,0,0,134,132,1,0,0,0,134,133,1,0,0,0,135,15,1,0,0,0,136,137,
        5,63,0,0,137,138,3,14,7,0,138,139,5,64,0,0,139,17,1,0,0,0,140,141,
        5,72,0,0,141,142,5,59,0,0,142,148,3,10,5,0,143,144,5,59,0,0,144,
        147,3,10,5,0,145,147,5,72,0,0,146,143,1,0,0,0,146,145,1,0,0,0,147,
        150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,174,1,0,0,0,150,
        148,1,0,0,0,151,152,3,10,5,0,152,153,5,59,0,0,153,159,5,72,0,0,154,
        155,5,59,0,0,155,158,3,10,5,0,156,158,5,72,0,0,157,154,1,0,0,0,157,
        156,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,
        174,1,0,0,0,161,159,1,0,0,0,162,163,5,72,0,0,163,164,5,59,0,0,164,
        170,5,72,0,0,165,166,5,59,0,0,166,169,3,10,5,0,167,169,5,72,0,0,
        168,165,1,0,0,0,168,167,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,
        170,171,1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,173,140,1,0,0,0,
        173,151,1,0,0,0,173,162,1,0,0,0,174,19,1,0,0,0,175,176,5,3,0,0,176,
        177,5,59,0,0,177,184,3,18,9,0,178,179,5,3,0,0,179,180,5,59,0,0,180,
        181,7,2,0,0,181,182,5,59,0,0,182,184,5,68,0,0,183,175,1,0,0,0,183,
        178,1,0,0,0,184,21,1,0,0,0,185,186,7,3,0,0,186,23,1,0,0,0,187,188,
        6,12,-1,0,188,194,5,72,0,0,189,194,3,12,6,0,190,191,5,72,0,0,191,
        192,5,59,0,0,192,194,5,72,0,0,193,187,1,0,0,0,193,189,1,0,0,0,193,
        190,1,0,0,0,194,209,1,0,0,0,195,196,10,4,0,0,196,197,5,54,0,0,197,
        208,3,24,12,5,198,199,10,3,0,0,199,200,5,55,0,0,200,208,3,24,12,
        4,201,202,10,2,0,0,202,203,5,56,0,0,203,208,3,24,12,3,204,205,10,
        1,0,0,205,206,5,57,0,0,206,208,3,24,12,2,207,195,1,0,0,0,207,198,
        1,0,0,0,207,201,1,0,0,0,207,204,1,0,0,0,208,211,1,0,0,0,209,207,
        1,0,0,0,209,210,1,0,0,0,210,25,1,0,0,0,211,209,1,0,0,0,212,218,3,
        24,12,0,213,214,3,22,11,0,214,215,3,24,12,0,215,217,1,0,0,0,216,
        213,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,
        27,1,0,0,0,220,218,1,0,0,0,221,222,3,10,5,0,222,223,5,61,0,0,223,
        224,3,14,7,0,224,225,5,62,0,0,225,29,1,0,0,0,226,227,5,13,0,0,227,
        228,5,72,0,0,228,229,5,14,0,0,229,230,3,18,9,0,230,231,5,15,0,0,
        231,232,3,20,10,0,232,239,1,0,0,0,233,234,5,16,0,0,234,235,5,61,
        0,0,235,236,3,16,8,0,236,237,5,62,0,0,237,239,1,0,0,0,238,226,1,
        0,0,0,238,233,1,0,0,0,239,31,1,0,0,0,240,241,5,17,0,0,241,242,5,
        61,0,0,242,243,3,14,7,0,243,244,5,62,0,0,244,33,1,0,0,0,245,246,
        5,18,0,0,246,247,5,72,0,0,247,248,5,61,0,0,248,249,3,26,13,0,249,
        250,5,62,0,0,250,35,1,0,0,0,251,252,5,19,0,0,252,253,5,72,0,0,253,
        254,5,20,0,0,254,264,5,68,0,0,255,256,5,19,0,0,256,257,5,72,0,0,
        257,258,5,21,0,0,258,259,5,72,0,0,259,260,5,61,0,0,260,261,3,14,
        7,0,261,262,5,62,0,0,262,264,1,0,0,0,263,251,1,0,0,0,263,255,1,0,
        0,0,264,37,1,0,0,0,265,266,5,19,0,0,266,267,5,72,0,0,267,268,5,22,
        0,0,268,271,5,61,0,0,269,272,3,14,7,0,270,272,3,20,10,0,271,269,
        1,0,0,0,271,270,1,0,0,0,272,273,1,0,0,0,273,274,5,62,0,0,274,296,
        1,0,0,0,275,276,5,23,0,0,276,277,5,72,0,0,277,278,5,22,0,0,278,281,
        5,61,0,0,279,282,3,14,7,0,280,282,3,20,10,0,281,279,1,0,0,0,281,
        280,1,0,0,0,282,283,1,0,0,0,283,284,5,62,0,0,284,296,1,0,0,0,285,
        286,5,24,0,0,286,287,5,72,0,0,287,288,5,22,0,0,288,291,5,61,0,0,
        289,292,3,14,7,0,290,292,3,20,10,0,291,289,1,0,0,0,291,290,1,0,0,
        0,292,293,1,0,0,0,293,294,5,62,0,0,294,296,1,0,0,0,295,265,1,0,0,
        0,295,275,1,0,0,0,295,285,1,0,0,0,296,39,1,0,0,0,297,298,5,23,0,
        0,298,299,5,72,0,0,299,300,5,20,0,0,300,310,5,68,0,0,301,302,5,23,
        0,0,302,303,5,72,0,0,303,304,5,21,0,0,304,305,5,72,0,0,305,306,5,
        61,0,0,306,307,3,14,7,0,307,308,5,62,0,0,308,310,1,0,0,0,309,297,
        1,0,0,0,309,301,1,0,0,0,310,41,1,0,0,0,311,312,5,24,0,0,312,313,
        5,72,0,0,313,314,5,20,0,0,314,324,5,68,0,0,315,316,5,24,0,0,316,
        317,5,72,0,0,317,318,5,21,0,0,318,319,5,72,0,0,319,320,5,61,0,0,
        320,321,3,14,7,0,321,322,5,62,0,0,322,324,1,0,0,0,323,311,1,0,0,
        0,323,315,1,0,0,0,324,43,1,0,0,0,325,326,5,27,0,0,326,327,5,72,0,
        0,327,328,5,28,0,0,328,329,3,20,10,0,329,45,1,0,0,0,330,331,5,29,
        0,0,331,332,5,72,0,0,332,333,3,44,22,0,333,47,1,0,0,0,29,53,60,74,
        86,97,107,117,128,134,146,148,157,159,168,170,173,183,193,207,209,
        218,238,263,271,281,291,295,309,323
    ]

class BoardGameParser ( Parser ):

    grammarFileName = "BoardGameParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'GAME'", "'DEFINE'", "'BOARD'", "'PLAYERS'", 
                     "'CONDITIONS'", "'TIMER'", "'SCORE'", "'DICE'", "'RULES'", 
                     "'PIECES'", "'OBSTACLES'", "'BOOSTERS'", "'PLAYER'", 
                     "'COLOR'", "'AT'", "'ORDER'", "'CONDITION'", "'RULE'", 
                     "'PIECE'", "'COUNT'", "'ACTION'", "'SETUP'", "'OBSTACLE'", 
                     "'BOOSTER'", "'START'", "'END'", "'MOVE'", "'TO'", 
                     "'TURN'", "'ROW'", "'COLUMN'", "'ALL'", "'ANY'", "'NONE'", 
                     "'IF'", "'ELSE'", "'FOR'", "'WHILE'", "'INPUT'", "'PRINT'", 
                     "'RETURN'", "'IN'", "'BREAK'", "'ERROR'", "'AND'", 
                     "'OR'", "'NOT'", "'=='", "'='", "'<'", "'<='", "'>'", 
                     "'>='", "'+'", "'-'", "'*'", "'/'", "':'", "'.'", "','", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'...'" ]

    symbolicNames = [ "<INVALID>", "GAME", "DEFINE", "BOARD", "PLAYERS", 
                      "CONDITIONS", "TIMER", "SCORE", "DICE", "RULES", "PIECES", 
                      "OBSTACLES", "BOOSTERS", "PLAYER", "COLOR", "AT", 
                      "ORDER", "CONDITION", "RULE", "PIECE", "COUNT", "ACTION", 
                      "SETUP", "OBSTACLE", "BOOSTER", "START", "END", "MOVE", 
                      "TO", "TURN", "ROW", "COLUMN", "ALL", "ANY", "NONE", 
                      "IF", "ELSE", "FOR", "WHILE", "INPUT", "PRINT", "RETURN", 
                      "IN", "BREAK", "ERROR", "AND_OPT", "OR_OPT", "NOT_OPT", 
                      "EQUAL_OPT", "ASSIGN_OPT", "LESS_THAN_OPT", "LESS_EQUAL_OPT", 
                      "GREATER_THAN_OPT", "GREATER_EQUAL_OPT", "ADD_OPT", 
                      "SUB_OPT", "MUL_OPT", "DIV_OPT", "COLON", "DOT", "COMMA", 
                      "OPEN_PAR", "CLOSE_PAR", "OPEN_BRACKET", "CLOSE_BRACKET", 
                      "OPEN_BRACE", "CLOSE_BRACE", "ELIPSIS", "INT_LITERAL", 
                      "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "IDENTIFIER", "COMMENT", "WS", "INVALID_IDENTIFIER" ]

    RULE_program = 0
    RULE_define_block = 1
    RULE_gameplay_block = 2
    RULE_code_block = 3
    RULE_statement = 4
    RULE_game_entities = 5
    RULE_literal = 6
    RULE_param_list = 7
    RULE_list = 8
    RULE_object_access = 9
    RULE_board_pos = 10
    RULE_conditional = 11
    RULE_expression = 12
    RULE_conditional_expression = 13
    RULE_game_entities_statement = 14
    RULE_player_statement = 15
    RULE_condition_statement = 16
    RULE_rule_statement = 17
    RULE_piece_statement = 18
    RULE_board_statement = 19
    RULE_obstacle_statement = 20
    RULE_booster_statement = 21
    RULE_move_statement = 22
    RULE_turn_statement = 23

    ruleNames =  [ "program", "define_block", "gameplay_block", "code_block", 
                   "statement", "game_entities", "literal", "param_list", 
                   "list", "object_access", "board_pos", "conditional", 
                   "expression", "conditional_expression", "game_entities_statement", 
                   "player_statement", "condition_statement", "rule_statement", 
                   "piece_statement", "board_statement", "obstacle_statement", 
                   "booster_statement", "move_statement", "turn_statement" ]

    EOF = Token.EOF
    GAME=1
    DEFINE=2
    BOARD=3
    PLAYERS=4
    CONDITIONS=5
    TIMER=6
    SCORE=7
    DICE=8
    RULES=9
    PIECES=10
    OBSTACLES=11
    BOOSTERS=12
    PLAYER=13
    COLOR=14
    AT=15
    ORDER=16
    CONDITION=17
    RULE=18
    PIECE=19
    COUNT=20
    ACTION=21
    SETUP=22
    OBSTACLE=23
    BOOSTER=24
    START=25
    END=26
    MOVE=27
    TO=28
    TURN=29
    ROW=30
    COLUMN=31
    ALL=32
    ANY=33
    NONE=34
    IF=35
    ELSE=36
    FOR=37
    WHILE=38
    INPUT=39
    PRINT=40
    RETURN=41
    IN=42
    BREAK=43
    ERROR=44
    AND_OPT=45
    OR_OPT=46
    NOT_OPT=47
    EQUAL_OPT=48
    ASSIGN_OPT=49
    LESS_THAN_OPT=50
    LESS_EQUAL_OPT=51
    GREATER_THAN_OPT=52
    GREATER_EQUAL_OPT=53
    ADD_OPT=54
    SUB_OPT=55
    MUL_OPT=56
    DIV_OPT=57
    COLON=58
    DOT=59
    COMMA=60
    OPEN_PAR=61
    CLOSE_PAR=62
    OPEN_BRACKET=63
    CLOSE_BRACKET=64
    OPEN_BRACE=65
    CLOSE_BRACE=66
    ELIPSIS=67
    INT_LITERAL=68
    FLOAT_LITERAL=69
    STRING_LITERAL=70
    BOOLEAN_LITERAL=71
    IDENTIFIER=72
    COMMENT=73
    WS=74
    INVALID_IDENTIFIER=75

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GAME(self):
            return self.getToken(BoardGameParser.GAME, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def gameplay_block(self):
            return self.getTypedRuleContext(BoardGameParser.Gameplay_blockContext,0)


        def define_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Define_blockContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Define_blockContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = BoardGameParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(BoardGameParser.GAME)
            self.state = 49
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.define_block()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 55
            self.gameplay_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(BoardGameParser.DEFINE, 0)

        def COLON(self):
            return self.getToken(BoardGameParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(BoardGameParser.Code_blockContext,0)


        def END(self):
            return self.getToken(BoardGameParser.END, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_define_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_block" ):
                listener.enterDefine_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_block" ):
                listener.exitDefine_block(self)




    def define_block(self):

        localctx = BoardGameParser.Define_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_define_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(BoardGameParser.DEFINE)
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 58
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 59
                self.object_access()
                pass


            self.state = 62
            self.match(BoardGameParser.COLON)
            self.state = 63
            self.code_block()
            self.state = 64
            self.match(BoardGameParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gameplay_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(BoardGameParser.START, 0)

        def COLON(self):
            return self.getToken(BoardGameParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(BoardGameParser.Code_blockContext,0)


        def END(self):
            return self.getToken(BoardGameParser.END, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_gameplay_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGameplay_block" ):
                listener.enterGameplay_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGameplay_block" ):
                listener.exitGameplay_block(self)




    def gameplay_block(self):

        localctx = BoardGameParser.Gameplay_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_gameplay_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(BoardGameParser.START)
            self.state = 67
            self.match(BoardGameParser.COLON)
            self.state = 68
            self.code_block()
            self.state = 69
            self.match(BoardGameParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.StatementContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.StatementContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)




    def code_block(self):

        localctx = BoardGameParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.statement()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 697269816) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def game_entities_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Game_entities_statementContext,0)


        def board_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Board_statementContext,0)


        def player_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Player_statementContext,0)


        def condition_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Condition_statementContext,0)


        def rule_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Rule_statementContext,0)


        def piece_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Piece_statementContext,0)


        def obstacle_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Obstacle_statementContext,0)


        def booster_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Booster_statementContext,0)


        def turn_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Turn_statementContext,0)


        def move_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Move_statementContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = BoardGameParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.game_entities_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.board_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.player_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.condition_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.rule_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.piece_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.obstacle_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.booster_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 84
                self.turn_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 85
                self.move_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Game_entitiesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOARD(self):
            return self.getToken(BoardGameParser.BOARD, 0)

        def PLAYERS(self):
            return self.getToken(BoardGameParser.PLAYERS, 0)

        def CONDITIONS(self):
            return self.getToken(BoardGameParser.CONDITIONS, 0)

        def RULES(self):
            return self.getToken(BoardGameParser.RULES, 0)

        def PIECES(self):
            return self.getToken(BoardGameParser.PIECES, 0)

        def OBSTACLES(self):
            return self.getToken(BoardGameParser.OBSTACLES, 0)

        def BOOSTERS(self):
            return self.getToken(BoardGameParser.BOOSTERS, 0)

        def COLOR(self):
            return self.getToken(BoardGameParser.COLOR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_game_entities

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGame_entities" ):
                listener.enterGame_entities(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGame_entities" ):
                listener.exitGame_entities(self)




    def game_entities(self):

        localctx = BoardGameParser.Game_entitiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_game_entities)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(BoardGameParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(BoardGameParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(BoardGameParser.STRING_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(BoardGameParser.BOOLEAN_LITERAL, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = BoardGameParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not(((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 15) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.COMMA)
            else:
                return self.getToken(BoardGameParser.COMMA, i)

        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)

        def literal(self):
            return self.getTypedRuleContext(BoardGameParser.LiteralContext,0)


        def param_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Param_listContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Param_listContext,i)


        def NONE(self):
            return self.getToken(BoardGameParser.NONE, 0)

        def ANY(self):
            return self.getToken(BoardGameParser.ANY, 0)

        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)




    def param_list(self):

        localctx = BoardGameParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param_list)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 93
                        self.match(BoardGameParser.COMMA)
                        self.state = 94
                        self.match(BoardGameParser.IDENTIFIER) 
                    self.state = 99
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 101
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 102
                self.literal()
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 103
                        self.match(BoardGameParser.COMMA)
                        self.state = 104
                        self.param_list() 
                    self.state = 109
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 111
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 112
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 113
                        self.match(BoardGameParser.COMMA)
                        self.state = 114
                        self.param_list() 
                    self.state = 119
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 121
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 122
                self.literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.literal()
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 124
                        self.match(BoardGameParser.COMMA)
                        self.state = 125
                        self.param_list() 
                    self.state = 130
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 131
                self.match(BoardGameParser.NONE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 132
                self.match(BoardGameParser.ANY)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 133
                self.match(BoardGameParser.ALL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(BoardGameParser.OPEN_BRACKET, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(BoardGameParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = BoardGameParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(BoardGameParser.OPEN_BRACKET)
            self.state = 137
            self.param_list()
            self.state = 138
            self.match(BoardGameParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.DOT)
            else:
                return self.getToken(BoardGameParser.DOT, i)

        def game_entities(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Game_entitiesContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Game_entitiesContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_object_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_access" ):
                listener.enterObject_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_access" ):
                listener.exitObject_access(self)




    def object_access(self):

        localctx = BoardGameParser.Object_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_object_access)
        self._la = 0 # Token type
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 141
                self.match(BoardGameParser.DOT)
                self.state = 142
                self.game_entities()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==59 or _la==72:
                    self.state = 146
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [59]:
                        self.state = 143
                        self.match(BoardGameParser.DOT)
                        self.state = 144
                        self.game_entities()
                        pass
                    elif token in [72]:
                        self.state = 145
                        self.match(BoardGameParser.IDENTIFIER)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 150
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.game_entities()
                self.state = 152
                self.match(BoardGameParser.DOT)
                self.state = 153
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==59 or _la==72:
                    self.state = 157
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [59]:
                        self.state = 154
                        self.match(BoardGameParser.DOT)
                        self.state = 155
                        self.game_entities()
                        pass
                    elif token in [72]:
                        self.state = 156
                        self.match(BoardGameParser.IDENTIFIER)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 163
                self.match(BoardGameParser.DOT)
                self.state = 164
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==59 or _la==72:
                    self.state = 168
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [59]:
                        self.state = 165
                        self.match(BoardGameParser.DOT)
                        self.state = 166
                        self.game_entities()
                        pass
                    elif token in [72]:
                        self.state = 167
                        self.match(BoardGameParser.IDENTIFIER)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Board_posContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOARD(self):
            return self.getToken(BoardGameParser.BOARD, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.DOT)
            else:
                return self.getToken(BoardGameParser.DOT, i)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def ROW(self):
            return self.getToken(BoardGameParser.ROW, 0)

        def COLUMN(self):
            return self.getToken(BoardGameParser.COLUMN, 0)

        def INT_LITERAL(self):
            return self.getToken(BoardGameParser.INT_LITERAL, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_board_pos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoard_pos" ):
                listener.enterBoard_pos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoard_pos" ):
                listener.exitBoard_pos(self)




    def board_pos(self):

        localctx = BoardGameParser.Board_posContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_board_pos)
        self._la = 0 # Token type
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(BoardGameParser.BOARD)
                self.state = 176
                self.match(BoardGameParser.DOT)
                self.state = 177
                self.object_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(BoardGameParser.BOARD)
                self.state = 179
                self.match(BoardGameParser.DOT)
                self.state = 180
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 181
                self.match(BoardGameParser.DOT)

                self.state = 182
                self.match(BoardGameParser.INT_LITERAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND_OPT(self):
            return self.getToken(BoardGameParser.AND_OPT, 0)

        def OR_OPT(self):
            return self.getToken(BoardGameParser.OR_OPT, 0)

        def NOT_OPT(self):
            return self.getToken(BoardGameParser.NOT_OPT, 0)

        def EQUAL_OPT(self):
            return self.getToken(BoardGameParser.EQUAL_OPT, 0)

        def LESS_THAN_OPT(self):
            return self.getToken(BoardGameParser.LESS_THAN_OPT, 0)

        def LESS_EQUAL_OPT(self):
            return self.getToken(BoardGameParser.LESS_EQUAL_OPT, 0)

        def GREATER_THAN_OPT(self):
            return self.getToken(BoardGameParser.GREATER_THAN_OPT, 0)

        def GREATER_EQUAL_OPT(self):
            return self.getToken(BoardGameParser.GREATER_EQUAL_OPT, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = BoardGameParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17416264183971840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def literal(self):
            return self.getTypedRuleContext(BoardGameParser.LiteralContext,0)


        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.ExpressionContext,i)


        def ADD_OPT(self):
            return self.getToken(BoardGameParser.ADD_OPT, 0)

        def SUB_OPT(self):
            return self.getToken(BoardGameParser.SUB_OPT, 0)

        def MUL_OPT(self):
            return self.getToken(BoardGameParser.MUL_OPT, 0)

        def DIV_OPT(self):
            return self.getToken(BoardGameParser.DIV_OPT, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BoardGameParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 188
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 189
                self.literal()
                pass

            elif la_ == 3:
                self.state = 190
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 191
                self.match(BoardGameParser.DOT)
                self.state = 192
                self.match(BoardGameParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 207
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 195
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 196
                        self.match(BoardGameParser.ADD_OPT)
                        self.state = 197
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 199
                        self.match(BoardGameParser.SUB_OPT)
                        self.state = 200
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 202
                        self.match(BoardGameParser.MUL_OPT)
                        self.state = 203
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 204
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 205
                        self.match(BoardGameParser.DIV_OPT)
                        self.state = 206
                        self.expression(2)
                        pass

             
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Conditional_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.ExpressionContext,i)


        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.ConditionalContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_conditional_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_expression" ):
                listener.enterConditional_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_expression" ):
                listener.exitConditional_expression(self)




    def conditional_expression(self):

        localctx = BoardGameParser.Conditional_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_conditional_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.expression(0)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17416264183971840) != 0):
                self.state = 213
                self.conditional()
                self.state = 214
                self.expression(0)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Game_entities_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def game_entities(self):
            return self.getTypedRuleContext(BoardGameParser.Game_entitiesContext,0)


        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_game_entities_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGame_entities_statement" ):
                listener.enterGame_entities_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGame_entities_statement" ):
                listener.exitGame_entities_statement(self)




    def game_entities_statement(self):

        localctx = BoardGameParser.Game_entities_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_game_entities_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.game_entities()
            self.state = 222
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 223
            self.param_list()
            self.state = 224
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Player_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLAYER(self):
            return self.getToken(BoardGameParser.PLAYER, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def COLOR(self):
            return self.getToken(BoardGameParser.COLOR, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def AT(self):
            return self.getToken(BoardGameParser.AT, 0)

        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)


        def ORDER(self):
            return self.getToken(BoardGameParser.ORDER, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def list_(self):
            return self.getTypedRuleContext(BoardGameParser.ListContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_player_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayer_statement" ):
                listener.enterPlayer_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayer_statement" ):
                listener.exitPlayer_statement(self)




    def player_statement(self):

        localctx = BoardGameParser.Player_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_player_statement)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(BoardGameParser.PLAYER)
                self.state = 227
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 228
                self.match(BoardGameParser.COLOR)
                self.state = 229
                self.object_access()
                self.state = 230
                self.match(BoardGameParser.AT)
                self.state = 231
                self.board_pos()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(BoardGameParser.ORDER)
                self.state = 234
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 235
                self.list_()
                self.state = 236
                self.match(BoardGameParser.CLOSE_PAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONDITION(self):
            return self.getToken(BoardGameParser.CONDITION, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_condition_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_statement" ):
                listener.enterCondition_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_statement" ):
                listener.exitCondition_statement(self)




    def condition_statement(self):

        localctx = BoardGameParser.Condition_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(BoardGameParser.CONDITION)
            self.state = 241
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 242
            self.param_list()
            self.state = 243
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE(self):
            return self.getToken(BoardGameParser.RULE, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def conditional_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Conditional_expressionContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_rule_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_statement" ):
                listener.enterRule_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_statement" ):
                listener.exitRule_statement(self)




    def rule_statement(self):

        localctx = BoardGameParser.Rule_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_rule_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(BoardGameParser.RULE)
            self.state = 246
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 247
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 248
            self.conditional_expression()
            self.state = 249
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Piece_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIECE(self):
            return self.getToken(BoardGameParser.PIECE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def COUNT(self):
            return self.getToken(BoardGameParser.COUNT, 0)

        def INT_LITERAL(self):
            return self.getToken(BoardGameParser.INT_LITERAL, 0)

        def ACTION(self):
            return self.getToken(BoardGameParser.ACTION, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_piece_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPiece_statement" ):
                listener.enterPiece_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPiece_statement" ):
                listener.exitPiece_statement(self)




    def piece_statement(self):

        localctx = BoardGameParser.Piece_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_piece_statement)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(BoardGameParser.PIECE)
                self.state = 252
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 253
                self.match(BoardGameParser.COUNT)
                self.state = 254
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(BoardGameParser.PIECE)
                self.state = 256
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 257
                self.match(BoardGameParser.ACTION)
                self.state = 258
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 259
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 260
                self.param_list()
                self.state = 261
                self.match(BoardGameParser.CLOSE_PAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Board_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIECE(self):
            return self.getToken(BoardGameParser.PIECE, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def SETUP(self):
            return self.getToken(BoardGameParser.SETUP, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)


        def OBSTACLE(self):
            return self.getToken(BoardGameParser.OBSTACLE, 0)

        def BOOSTER(self):
            return self.getToken(BoardGameParser.BOOSTER, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_board_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoard_statement" ):
                listener.enterBoard_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoard_statement" ):
                listener.exitBoard_statement(self)




    def board_statement(self):

        localctx = BoardGameParser.Board_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_board_statement)
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(BoardGameParser.PIECE)
                self.state = 266
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 267
                self.match(BoardGameParser.SETUP)
                self.state = 268
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 271
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32, 33, 34, 68, 69, 70, 71, 72]:
                    self.state = 269
                    self.param_list()
                    pass
                elif token in [3]:
                    self.state = 270
                    self.board_pos()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 273
                self.match(BoardGameParser.CLOSE_PAR)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(BoardGameParser.OBSTACLE)
                self.state = 276
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 277
                self.match(BoardGameParser.SETUP)
                self.state = 278
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 281
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32, 33, 34, 68, 69, 70, 71, 72]:
                    self.state = 279
                    self.param_list()
                    pass
                elif token in [3]:
                    self.state = 280
                    self.board_pos()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 283
                self.match(BoardGameParser.CLOSE_PAR)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 285
                self.match(BoardGameParser.BOOSTER)
                self.state = 286
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 287
                self.match(BoardGameParser.SETUP)
                self.state = 288
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 291
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32, 33, 34, 68, 69, 70, 71, 72]:
                    self.state = 289
                    self.param_list()
                    pass
                elif token in [3]:
                    self.state = 290
                    self.board_pos()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 293
                self.match(BoardGameParser.CLOSE_PAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obstacle_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBSTACLE(self):
            return self.getToken(BoardGameParser.OBSTACLE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def COUNT(self):
            return self.getToken(BoardGameParser.COUNT, 0)

        def INT_LITERAL(self):
            return self.getToken(BoardGameParser.INT_LITERAL, 0)

        def ACTION(self):
            return self.getToken(BoardGameParser.ACTION, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_obstacle_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObstacle_statement" ):
                listener.enterObstacle_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObstacle_statement" ):
                listener.exitObstacle_statement(self)




    def obstacle_statement(self):

        localctx = BoardGameParser.Obstacle_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_obstacle_statement)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(BoardGameParser.OBSTACLE)
                self.state = 298
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 299
                self.match(BoardGameParser.COUNT)
                self.state = 300
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.match(BoardGameParser.OBSTACLE)
                self.state = 302
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 303
                self.match(BoardGameParser.ACTION)
                self.state = 304
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 305
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 306
                self.param_list()
                self.state = 307
                self.match(BoardGameParser.CLOSE_PAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Booster_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOSTER(self):
            return self.getToken(BoardGameParser.BOOSTER, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def COUNT(self):
            return self.getToken(BoardGameParser.COUNT, 0)

        def INT_LITERAL(self):
            return self.getToken(BoardGameParser.INT_LITERAL, 0)

        def ACTION(self):
            return self.getToken(BoardGameParser.ACTION, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_booster_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooster_statement" ):
                listener.enterBooster_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooster_statement" ):
                listener.exitBooster_statement(self)




    def booster_statement(self):

        localctx = BoardGameParser.Booster_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_booster_statement)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(BoardGameParser.BOOSTER)
                self.state = 312
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 313
                self.match(BoardGameParser.COUNT)
                self.state = 314
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(BoardGameParser.BOOSTER)
                self.state = 316
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 317
                self.match(BoardGameParser.ACTION)
                self.state = 318
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 319
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 320
                self.param_list()
                self.state = 321
                self.match(BoardGameParser.CLOSE_PAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Move_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVE(self):
            return self.getToken(BoardGameParser.MOVE, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def TO(self):
            return self.getToken(BoardGameParser.TO, 0)

        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_move_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove_statement" ):
                listener.enterMove_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove_statement" ):
                listener.exitMove_statement(self)




    def move_statement(self):

        localctx = BoardGameParser.Move_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_move_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(BoardGameParser.MOVE)
            self.state = 326
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 327
            self.match(BoardGameParser.TO)
            self.state = 328
            self.board_pos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Turn_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TURN(self):
            return self.getToken(BoardGameParser.TURN, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def move_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Move_statementContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_turn_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTurn_statement" ):
                listener.enterTurn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTurn_statement" ):
                listener.exitTurn_statement(self)




    def turn_statement(self):

        localctx = BoardGameParser.Turn_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_turn_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(BoardGameParser.TURN)
            self.state = 331
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 332
            self.move_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




