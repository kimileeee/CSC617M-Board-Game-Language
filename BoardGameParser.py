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
        4,1,73,322,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,4,0,52,8,0,11,0,12,
        0,53,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,4,3,
        70,8,3,11,3,12,3,71,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        84,8,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,93,8,7,10,7,12,7,96,9,7,1,
        7,1,7,1,7,1,7,1,7,5,7,103,8,7,10,7,12,7,106,9,7,1,7,1,7,1,7,1,7,
        1,7,5,7,113,8,7,10,7,12,7,116,9,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,124,
        8,7,10,7,12,7,127,9,7,1,7,1,7,1,7,3,7,132,8,7,1,8,1,8,1,8,1,8,1,
        8,1,8,5,8,140,8,8,10,8,12,8,143,9,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,
        151,8,8,10,8,12,8,154,9,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,162,8,8,10,
        8,12,8,165,9,8,3,8,167,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,1,11,3,11,181,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,5,11,195,8,11,10,11,12,11,198,9,11,1,
        12,1,12,1,12,1,12,1,12,3,12,205,8,12,1,13,1,13,1,13,1,13,5,13,211,
        8,13,10,13,12,13,214,9,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,
        1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,3,18,251,8,18,1,19,1,19,1,19,1,19,1,19,1,19,3,19,259,8,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,269,8,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,3,19,279,8,19,1,19,1,19,3,19,283,8,19,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,
        297,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,3,21,311,8,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,
        1,23,0,1,22,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,0,3,2,0,3,5,9,12,1,0,66,69,2,0,43,46,48,51,343,
        0,48,1,0,0,0,2,57,1,0,0,0,4,63,1,0,0,0,6,69,1,0,0,0,8,83,1,0,0,0,
        10,85,1,0,0,0,12,87,1,0,0,0,14,131,1,0,0,0,16,166,1,0,0,0,18,168,
        1,0,0,0,20,172,1,0,0,0,22,180,1,0,0,0,24,204,1,0,0,0,26,206,1,0,
        0,0,28,215,1,0,0,0,30,220,1,0,0,0,32,227,1,0,0,0,34,232,1,0,0,0,
        36,250,1,0,0,0,38,282,1,0,0,0,40,296,1,0,0,0,42,310,1,0,0,0,44,312,
        1,0,0,0,46,317,1,0,0,0,48,49,5,1,0,0,49,51,5,70,0,0,50,52,3,2,1,
        0,51,50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,55,
        1,0,0,0,55,56,3,4,2,0,56,1,1,0,0,0,57,58,5,2,0,0,58,59,5,70,0,0,
        59,60,5,56,0,0,60,61,3,6,3,0,61,62,5,26,0,0,62,3,1,0,0,0,63,64,5,
        25,0,0,64,65,5,56,0,0,65,66,3,6,3,0,66,67,5,26,0,0,67,5,1,0,0,0,
        68,70,3,8,4,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,0,71,72,1,
        0,0,0,72,7,1,0,0,0,73,84,3,28,14,0,74,84,3,38,19,0,75,84,3,30,15,
        0,76,84,3,32,16,0,77,84,3,34,17,0,78,84,3,36,18,0,79,84,3,40,20,
        0,80,84,3,42,21,0,81,84,3,46,23,0,82,84,3,44,22,0,83,73,1,0,0,0,
        83,74,1,0,0,0,83,75,1,0,0,0,83,76,1,0,0,0,83,77,1,0,0,0,83,78,1,
        0,0,0,83,79,1,0,0,0,83,80,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,
        9,1,0,0,0,85,86,7,0,0,0,86,11,1,0,0,0,87,88,7,1,0,0,88,13,1,0,0,
        0,89,94,5,70,0,0,90,91,5,58,0,0,91,93,5,70,0,0,92,90,1,0,0,0,93,
        96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,132,1,0,0,0,96,94,1,0,
        0,0,97,98,5,70,0,0,98,99,5,47,0,0,99,104,3,12,6,0,100,101,5,58,0,
        0,101,103,3,14,7,0,102,100,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,
        0,104,105,1,0,0,0,105,132,1,0,0,0,106,104,1,0,0,0,107,108,5,70,0,
        0,108,109,5,47,0,0,109,114,5,70,0,0,110,111,5,58,0,0,111,113,3,14,
        7,0,112,110,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,
        0,0,115,132,1,0,0,0,116,114,1,0,0,0,117,118,5,70,0,0,118,119,5,47,
        0,0,119,132,3,12,6,0,120,125,3,12,6,0,121,122,5,58,0,0,122,124,3,
        14,7,0,123,121,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,
        0,0,0,126,132,1,0,0,0,127,125,1,0,0,0,128,132,5,32,0,0,129,132,5,
        31,0,0,130,132,5,30,0,0,131,89,1,0,0,0,131,97,1,0,0,0,131,107,1,
        0,0,0,131,117,1,0,0,0,131,120,1,0,0,0,131,128,1,0,0,0,131,129,1,
        0,0,0,131,130,1,0,0,0,132,15,1,0,0,0,133,134,5,70,0,0,134,135,5,
        57,0,0,135,141,3,10,5,0,136,137,5,57,0,0,137,140,3,10,5,0,138,140,
        5,70,0,0,139,136,1,0,0,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,
        1,0,0,0,141,142,1,0,0,0,142,167,1,0,0,0,143,141,1,0,0,0,144,145,
        3,10,5,0,145,146,5,57,0,0,146,152,5,70,0,0,147,148,5,57,0,0,148,
        151,3,10,5,0,149,151,5,70,0,0,150,147,1,0,0,0,150,149,1,0,0,0,151,
        154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,167,1,0,0,0,154,
        152,1,0,0,0,155,156,5,70,0,0,156,157,5,57,0,0,157,163,5,70,0,0,158,
        159,5,57,0,0,159,162,3,10,5,0,160,162,5,70,0,0,161,158,1,0,0,0,161,
        160,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,
        167,1,0,0,0,165,163,1,0,0,0,166,133,1,0,0,0,166,144,1,0,0,0,166,
        155,1,0,0,0,167,17,1,0,0,0,168,169,5,3,0,0,169,170,5,57,0,0,170,
        171,3,16,8,0,171,19,1,0,0,0,172,173,7,2,0,0,173,21,1,0,0,0,174,175,
        6,11,-1,0,175,181,5,70,0,0,176,181,3,12,6,0,177,178,5,70,0,0,178,
        179,5,57,0,0,179,181,5,70,0,0,180,174,1,0,0,0,180,176,1,0,0,0,180,
        177,1,0,0,0,181,196,1,0,0,0,182,183,10,4,0,0,183,184,5,52,0,0,184,
        195,3,22,11,5,185,186,10,3,0,0,186,187,5,53,0,0,187,195,3,22,11,
        4,188,189,10,2,0,0,189,190,5,54,0,0,190,195,3,22,11,3,191,192,10,
        1,0,0,192,193,5,55,0,0,193,195,3,22,11,2,194,182,1,0,0,0,194,185,
        1,0,0,0,194,188,1,0,0,0,194,191,1,0,0,0,195,198,1,0,0,0,196,194,
        1,0,0,0,196,197,1,0,0,0,197,23,1,0,0,0,198,196,1,0,0,0,199,200,3,
        22,11,0,200,201,3,20,10,0,201,202,3,24,12,0,202,205,1,0,0,0,203,
        205,3,22,11,0,204,199,1,0,0,0,204,203,1,0,0,0,205,25,1,0,0,0,206,
        212,3,22,11,0,207,208,3,20,10,0,208,209,3,22,11,0,209,211,1,0,0,
        0,210,207,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,
        0,213,27,1,0,0,0,214,212,1,0,0,0,215,216,3,10,5,0,216,217,5,59,0,
        0,217,218,3,14,7,0,218,219,5,60,0,0,219,29,1,0,0,0,220,221,5,13,
        0,0,221,222,5,70,0,0,222,223,5,14,0,0,223,224,3,16,8,0,224,225,5,
        15,0,0,225,226,3,18,9,0,226,31,1,0,0,0,227,228,5,17,0,0,228,229,
        5,59,0,0,229,230,3,14,7,0,230,231,5,60,0,0,231,33,1,0,0,0,232,233,
        5,18,0,0,233,234,5,70,0,0,234,235,5,59,0,0,235,236,3,24,12,0,236,
        237,5,60,0,0,237,35,1,0,0,0,238,239,5,19,0,0,239,240,5,70,0,0,240,
        241,5,20,0,0,241,251,5,66,0,0,242,243,5,19,0,0,243,244,5,70,0,0,
        244,245,5,21,0,0,245,246,5,70,0,0,246,247,5,59,0,0,247,248,3,14,
        7,0,248,249,5,60,0,0,249,251,1,0,0,0,250,238,1,0,0,0,250,242,1,0,
        0,0,251,37,1,0,0,0,252,253,5,19,0,0,253,254,5,70,0,0,254,255,5,22,
        0,0,255,258,5,59,0,0,256,259,3,14,7,0,257,259,3,18,9,0,258,256,1,
        0,0,0,258,257,1,0,0,0,259,260,1,0,0,0,260,261,5,60,0,0,261,283,1,
        0,0,0,262,263,5,23,0,0,263,264,5,70,0,0,264,265,5,22,0,0,265,268,
        5,59,0,0,266,269,3,14,7,0,267,269,3,18,9,0,268,266,1,0,0,0,268,267,
        1,0,0,0,269,270,1,0,0,0,270,271,5,60,0,0,271,283,1,0,0,0,272,273,
        5,24,0,0,273,274,5,70,0,0,274,275,5,22,0,0,275,278,5,59,0,0,276,
        279,3,14,7,0,277,279,3,18,9,0,278,276,1,0,0,0,278,277,1,0,0,0,279,
        280,1,0,0,0,280,281,5,60,0,0,281,283,1,0,0,0,282,252,1,0,0,0,282,
        262,1,0,0,0,282,272,1,0,0,0,283,39,1,0,0,0,284,285,5,23,0,0,285,
        286,5,70,0,0,286,287,5,20,0,0,287,297,5,66,0,0,288,289,5,23,0,0,
        289,290,5,70,0,0,290,291,5,21,0,0,291,292,5,70,0,0,292,293,5,59,
        0,0,293,294,3,14,7,0,294,295,5,60,0,0,295,297,1,0,0,0,296,284,1,
        0,0,0,296,288,1,0,0,0,297,41,1,0,0,0,298,299,5,24,0,0,299,300,5,
        70,0,0,300,301,5,20,0,0,301,311,5,66,0,0,302,303,5,24,0,0,303,304,
        5,70,0,0,304,305,5,21,0,0,305,306,5,70,0,0,306,307,5,59,0,0,307,
        308,3,14,7,0,308,309,5,60,0,0,309,311,1,0,0,0,310,298,1,0,0,0,310,
        302,1,0,0,0,311,43,1,0,0,0,312,313,5,27,0,0,313,314,5,70,0,0,314,
        315,5,28,0,0,315,316,3,18,9,0,316,45,1,0,0,0,317,318,5,29,0,0,318,
        319,5,70,0,0,319,320,3,44,22,0,320,47,1,0,0,0,27,53,71,83,94,104,
        114,125,131,139,141,150,152,161,163,166,180,194,196,204,212,250,
        258,268,278,282,296,310
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
                     "'TURN'", "'ALL'", "'ANY'", "'NONE'", "'IF'", "'ELSE'", 
                     "'FOR'", "'WHILE'", "'INPUT'", "'PRINT'", "'RETURN'", 
                     "'IN'", "'BREAK'", "'ERROR'", "'AND'", "'OR'", "'NOT'", 
                     "'=='", "'='", "'<'", "'<='", "'>'", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "':'", "'.'", "','", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "'...'" ]

    symbolicNames = [ "<INVALID>", "GAME", "DEFINE", "BOARD", "PLAYERS", 
                      "CONDITIONS", "TIMER", "SCORE", "DICE", "RULES", "PIECES", 
                      "OBSTACLES", "BOOSTERS", "PLAYER", "COLOR", "AT", 
                      "ORDER", "CONDITION", "RULE", "PIECE", "COUNT", "ACTION", 
                      "SETUP", "OBSTACLE", "BOOSTER", "START", "END", "MOVE", 
                      "TO", "TURN", "ALL", "ANY", "NONE", "IF", "ELSE", 
                      "FOR", "WHILE", "INPUT", "PRINT", "RETURN", "IN", 
                      "BREAK", "ERROR", "AND_OPT", "OR_OPT", "NOT_OPT", 
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
    RULE_object_access = 8
    RULE_board_pos = 9
    RULE_conditional = 10
    RULE_expression = 11
    RULE_conditional_expression = 12
    RULE_conditional_expression_2 = 13
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
                   "object_access", "board_pos", "conditional", "expression", 
                   "conditional_expression", "conditional_expression_2", 
                   "game_entities_statement", "player_statement", "condition_statement", 
                   "rule_statement", "piece_statement", "board_statement", 
                   "obstacle_statement", "booster_statement", "move_statement", 
                   "turn_statement" ]

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
    ALL=30
    ANY=31
    NONE=32
    IF=33
    ELSE=34
    FOR=35
    WHILE=36
    INPUT=37
    PRINT=38
    RETURN=39
    IN=40
    BREAK=41
    ERROR=42
    AND_OPT=43
    OR_OPT=44
    NOT_OPT=45
    EQUAL_OPT=46
    ASSIGN_OPT=47
    LESS_THAN_OPT=48
    LESS_EQUAL_OPT=49
    GREATER_THAN_OPT=50
    GREATER_EQUAL_OPT=51
    ADD_OPT=52
    SUB_OPT=53
    MUL_OPT=54
    DIV_OPT=55
    COLON=56
    DOT=57
    COMMA=58
    OPEN_PAR=59
    CLOSE_PAR=60
    OPEN_BRACKET=61
    CLOSE_BRACKET=62
    OPEN_BRACE=63
    CLOSE_BRACE=64
    ELIPSIS=65
    INT_LITERAL=66
    FLOAT_LITERAL=67
    STRING_LITERAL=68
    BOOLEAN_LITERAL=69
    IDENTIFIER=70
    COMMENT=71
    WS=72
    INVALID_IDENTIFIER=73

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

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(BoardGameParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(BoardGameParser.Code_blockContext,0)


        def END(self):
            return self.getToken(BoardGameParser.END, 0)

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
            self.state = 58
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 59
            self.match(BoardGameParser.COLON)
            self.state = 60
            self.code_block()
            self.state = 61
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
            self.state = 63
            self.match(BoardGameParser.START)
            self.state = 64
            self.match(BoardGameParser.COLON)
            self.state = 65
            self.code_block()
            self.state = 66
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
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.statement()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 697187896) != 0)):
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
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.game_entities_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.board_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.player_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.condition_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.rule_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.piece_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 79
                self.obstacle_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 80
                self.booster_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 81
                self.turn_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 82
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
            self.state = 85
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7736) != 0)):
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
            self.state = 87
            _la = self._input.LA(1)
            if not(((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 15) != 0)):
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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 90
                        self.match(BoardGameParser.COMMA)
                        self.state = 91
                        self.match(BoardGameParser.IDENTIFIER) 
                    self.state = 96
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 98
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 99
                self.literal()
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 100
                        self.match(BoardGameParser.COMMA)
                        self.state = 101
                        self.param_list() 
                    self.state = 106
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 108
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 109
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 110
                        self.match(BoardGameParser.COMMA)
                        self.state = 111
                        self.param_list() 
                    self.state = 116
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 117
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 118
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 119
                self.literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 120
                self.literal()
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 121
                        self.match(BoardGameParser.COMMA)
                        self.state = 122
                        self.param_list() 
                    self.state = 127
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 128
                self.match(BoardGameParser.NONE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 129
                self.match(BoardGameParser.ANY)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 130
                self.match(BoardGameParser.ALL)
                pass


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
        self.enterRule(localctx, 16, self.RULE_object_access)
        self._la = 0 # Token type
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 134
                self.match(BoardGameParser.DOT)
                self.state = 135
                self.game_entities()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==57 or _la==70:
                    self.state = 139
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [57]:
                        self.state = 136
                        self.match(BoardGameParser.DOT)
                        self.state = 137
                        self.game_entities()
                        pass
                    elif token in [70]:
                        self.state = 138
                        self.match(BoardGameParser.IDENTIFIER)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 143
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.game_entities()
                self.state = 145
                self.match(BoardGameParser.DOT)
                self.state = 146
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==57 or _la==70:
                    self.state = 150
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [57]:
                        self.state = 147
                        self.match(BoardGameParser.DOT)
                        self.state = 148
                        self.game_entities()
                        pass
                    elif token in [70]:
                        self.state = 149
                        self.match(BoardGameParser.IDENTIFIER)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 156
                self.match(BoardGameParser.DOT)
                self.state = 157
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==57 or _la==70:
                    self.state = 161
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [57]:
                        self.state = 158
                        self.match(BoardGameParser.DOT)
                        self.state = 159
                        self.game_entities()
                        pass
                    elif token in [70]:
                        self.state = 160
                        self.match(BoardGameParser.IDENTIFIER)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 165
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

        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


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
        self.enterRule(localctx, 18, self.RULE_board_pos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(BoardGameParser.BOARD)
            self.state = 169
            self.match(BoardGameParser.DOT)
            self.state = 170
            self.object_access()
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
        self.enterRule(localctx, 20, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4354066045992960) != 0)):
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 175
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 176
                self.literal()
                pass

            elif la_ == 3:
                self.state = 177
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 178
                self.match(BoardGameParser.DOT)
                self.state = 179
                self.match(BoardGameParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 194
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 182
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 183
                        self.match(BoardGameParser.ADD_OPT)
                        self.state = 184
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 186
                        self.match(BoardGameParser.SUB_OPT)
                        self.state = 187
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 188
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 189
                        self.match(BoardGameParser.MUL_OPT)
                        self.state = 190
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 191
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 192
                        self.match(BoardGameParser.DIV_OPT)
                        self.state = 193
                        self.expression(2)
                        pass

             
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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

        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def conditional(self):
            return self.getTypedRuleContext(BoardGameParser.ConditionalContext,0)


        def conditional_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Conditional_expressionContext,0)


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
        self.enterRule(localctx, 24, self.RULE_conditional_expression)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.expression(0)
                self.state = 200
                self.conditional()
                self.state = 201
                self.conditional_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_expression_2Context(ParserRuleContext):
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
            return BoardGameParser.RULE_conditional_expression_2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_expression_2" ):
                listener.enterConditional_expression_2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_expression_2" ):
                listener.exitConditional_expression_2(self)




    def conditional_expression_2(self):

        localctx = BoardGameParser.Conditional_expression_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_conditional_expression_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.expression(0)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4354066045992960) != 0):
                self.state = 207
                self.conditional()
                self.state = 208
                self.expression(0)
                self.state = 214
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
            self.state = 215
            self.game_entities()
            self.state = 216
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 217
            self.param_list()
            self.state = 218
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
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(BoardGameParser.PLAYER)
            self.state = 221
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 222
            self.match(BoardGameParser.COLOR)
            self.state = 223
            self.object_access()
            self.state = 224
            self.match(BoardGameParser.AT)
            self.state = 225
            self.board_pos()
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
            self.state = 227
            self.match(BoardGameParser.CONDITION)
            self.state = 228
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 229
            self.param_list()
            self.state = 230
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
            self.state = 232
            self.match(BoardGameParser.RULE)
            self.state = 233
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 234
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 235
            self.conditional_expression()
            self.state = 236
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
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(BoardGameParser.PIECE)
                self.state = 239
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 240
                self.match(BoardGameParser.COUNT)
                self.state = 241
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(BoardGameParser.PIECE)
                self.state = 243
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 244
                self.match(BoardGameParser.ACTION)
                self.state = 245
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 246
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 247
                self.param_list()
                self.state = 248
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
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(BoardGameParser.PIECE)
                self.state = 253
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 254
                self.match(BoardGameParser.SETUP)
                self.state = 255
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 258
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [30, 31, 32, 66, 67, 68, 69, 70]:
                    self.state = 256
                    self.param_list()
                    pass
                elif token in [3]:
                    self.state = 257
                    self.board_pos()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 260
                self.match(BoardGameParser.CLOSE_PAR)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.match(BoardGameParser.OBSTACLE)
                self.state = 263
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 264
                self.match(BoardGameParser.SETUP)
                self.state = 265
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 268
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [30, 31, 32, 66, 67, 68, 69, 70]:
                    self.state = 266
                    self.param_list()
                    pass
                elif token in [3]:
                    self.state = 267
                    self.board_pos()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 270
                self.match(BoardGameParser.CLOSE_PAR)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.match(BoardGameParser.BOOSTER)
                self.state = 273
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 274
                self.match(BoardGameParser.SETUP)
                self.state = 275
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 278
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [30, 31, 32, 66, 67, 68, 69, 70]:
                    self.state = 276
                    self.param_list()
                    pass
                elif token in [3]:
                    self.state = 277
                    self.board_pos()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 280
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
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(BoardGameParser.OBSTACLE)
                self.state = 285
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 286
                self.match(BoardGameParser.COUNT)
                self.state = 287
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.match(BoardGameParser.OBSTACLE)
                self.state = 289
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 290
                self.match(BoardGameParser.ACTION)
                self.state = 291
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 292
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 293
                self.param_list()
                self.state = 294
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
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(BoardGameParser.BOOSTER)
                self.state = 299
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 300
                self.match(BoardGameParser.COUNT)
                self.state = 301
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.match(BoardGameParser.BOOSTER)
                self.state = 303
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 304
                self.match(BoardGameParser.ACTION)
                self.state = 305
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 306
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 307
                self.param_list()
                self.state = 308
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
            self.state = 312
            self.match(BoardGameParser.MOVE)
            self.state = 313
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 314
            self.match(BoardGameParser.TO)
            self.state = 315
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
            self.state = 317
            self.match(BoardGameParser.TURN)
            self.state = 318
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 319
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
        self._predicates[11] = self.expression_sempred
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
         




