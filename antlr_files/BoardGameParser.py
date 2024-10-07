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
        4,1,70,288,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,4,0,50,8,0,11,0,12,0,51,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        3,3,71,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,83,8,4,1,
        5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,127,8,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,139,8,8,1,9,1,9,1,9,1,9,1,9,3,9,146,
        8,9,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,156,8,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,170,8,
        11,10,11,12,11,173,9,11,1,12,1,12,1,12,1,12,1,12,3,12,180,8,12,1,
        13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,217,8,17,1,18,1,
        18,1,18,1,18,1,18,1,18,3,18,225,8,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,3,18,235,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,3,18,245,8,18,1,18,1,18,3,18,249,8,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,263,8,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,277,8,20,1,21,
        1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,0,1,22,23,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,3,1,0,3,
        9,1,0,64,67,2,0,42,45,47,50,307,0,46,1,0,0,0,2,55,1,0,0,0,4,61,1,
        0,0,0,6,70,1,0,0,0,8,82,1,0,0,0,10,84,1,0,0,0,12,86,1,0,0,0,14,126,
        1,0,0,0,16,138,1,0,0,0,18,145,1,0,0,0,20,147,1,0,0,0,22,155,1,0,
        0,0,24,179,1,0,0,0,26,181,1,0,0,0,28,186,1,0,0,0,30,193,1,0,0,0,
        32,198,1,0,0,0,34,216,1,0,0,0,36,248,1,0,0,0,38,262,1,0,0,0,40,276,
        1,0,0,0,42,278,1,0,0,0,44,283,1,0,0,0,46,47,5,1,0,0,47,49,5,68,0,
        0,48,50,3,2,1,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,
        1,0,0,0,52,53,1,0,0,0,53,54,3,4,2,0,54,1,1,0,0,0,55,56,5,2,0,0,56,
        57,5,68,0,0,57,58,5,55,0,0,58,59,3,6,3,0,59,60,5,25,0,0,60,3,1,0,
        0,0,61,62,5,24,0,0,62,63,5,55,0,0,63,64,3,6,3,0,64,65,5,25,0,0,65,
        5,1,0,0,0,66,67,3,8,4,0,67,68,3,6,3,0,68,71,1,0,0,0,69,71,3,8,4,
        0,70,66,1,0,0,0,70,69,1,0,0,0,71,7,1,0,0,0,72,83,3,26,13,0,73,83,
        3,36,18,0,74,83,3,28,14,0,75,83,3,30,15,0,76,83,3,32,16,0,77,83,
        3,34,17,0,78,83,3,38,19,0,79,83,3,40,20,0,80,83,3,44,22,0,81,83,
        3,42,21,0,82,72,1,0,0,0,82,73,1,0,0,0,82,74,1,0,0,0,82,75,1,0,0,
        0,82,76,1,0,0,0,82,77,1,0,0,0,82,78,1,0,0,0,82,79,1,0,0,0,82,80,
        1,0,0,0,82,81,1,0,0,0,83,9,1,0,0,0,84,85,7,0,0,0,85,11,1,0,0,0,86,
        87,7,1,0,0,87,13,1,0,0,0,88,89,5,68,0,0,89,90,5,57,0,0,90,127,3,
        14,7,0,91,92,5,68,0,0,92,93,5,46,0,0,93,94,3,12,6,0,94,95,5,57,0,
        0,95,96,3,14,7,0,96,127,1,0,0,0,97,98,5,68,0,0,98,99,5,46,0,0,99,
        100,5,68,0,0,100,101,5,57,0,0,101,127,3,14,7,0,102,103,5,68,0,0,
        103,104,5,46,0,0,104,127,3,12,6,0,105,106,5,68,0,0,106,107,5,46,
        0,0,107,127,5,68,0,0,108,109,5,30,0,0,109,110,5,57,0,0,110,127,3,
        14,7,0,111,112,5,29,0,0,112,113,5,57,0,0,113,127,3,14,7,0,114,115,
        5,31,0,0,115,116,5,57,0,0,116,127,3,14,7,0,117,127,5,68,0,0,118,
        127,5,31,0,0,119,127,5,30,0,0,120,127,5,29,0,0,121,122,3,12,6,0,
        122,123,5,57,0,0,123,124,3,14,7,0,124,127,1,0,0,0,125,127,3,12,6,
        0,126,88,1,0,0,0,126,91,1,0,0,0,126,97,1,0,0,0,126,102,1,0,0,0,126,
        105,1,0,0,0,126,108,1,0,0,0,126,111,1,0,0,0,126,114,1,0,0,0,126,
        117,1,0,0,0,126,118,1,0,0,0,126,119,1,0,0,0,126,120,1,0,0,0,126,
        121,1,0,0,0,126,125,1,0,0,0,127,15,1,0,0,0,128,129,5,68,0,0,129,
        130,5,56,0,0,130,139,3,10,5,0,131,132,3,10,5,0,132,133,5,56,0,0,
        133,134,5,68,0,0,134,139,1,0,0,0,135,136,5,68,0,0,136,137,5,56,0,
        0,137,139,5,68,0,0,138,128,1,0,0,0,138,131,1,0,0,0,138,135,1,0,0,
        0,139,17,1,0,0,0,140,146,5,20,0,0,141,146,5,21,0,0,142,143,5,3,0,
        0,143,144,5,56,0,0,144,146,5,68,0,0,145,140,1,0,0,0,145,141,1,0,
        0,0,145,142,1,0,0,0,146,19,1,0,0,0,147,148,7,2,0,0,148,21,1,0,0,
        0,149,150,6,11,-1,0,150,156,5,68,0,0,151,156,3,12,6,0,152,153,5,
        68,0,0,153,154,5,56,0,0,154,156,5,68,0,0,155,149,1,0,0,0,155,151,
        1,0,0,0,155,152,1,0,0,0,156,171,1,0,0,0,157,158,10,4,0,0,158,159,
        5,51,0,0,159,170,3,22,11,5,160,161,10,3,0,0,161,162,5,52,0,0,162,
        170,3,22,11,4,163,164,10,2,0,0,164,165,5,53,0,0,165,170,3,22,11,
        3,166,167,10,1,0,0,167,168,5,54,0,0,168,170,3,22,11,2,169,157,1,
        0,0,0,169,160,1,0,0,0,169,163,1,0,0,0,169,166,1,0,0,0,170,173,1,
        0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,23,1,0,0,0,173,171,1,0,
        0,0,174,175,3,22,11,0,175,176,3,20,10,0,176,177,3,24,12,0,177,180,
        1,0,0,0,178,180,3,22,11,0,179,174,1,0,0,0,179,178,1,0,0,0,180,25,
        1,0,0,0,181,182,3,10,5,0,182,183,5,58,0,0,183,184,3,14,7,0,184,185,
        5,59,0,0,185,27,1,0,0,0,186,187,5,10,0,0,187,188,5,68,0,0,188,189,
        5,11,0,0,189,190,3,16,8,0,190,191,5,12,0,0,191,192,3,18,9,0,192,
        29,1,0,0,0,193,194,5,14,0,0,194,195,5,58,0,0,195,196,3,14,7,0,196,
        197,5,59,0,0,197,31,1,0,0,0,198,199,5,15,0,0,199,200,5,68,0,0,200,
        201,5,58,0,0,201,202,3,24,12,0,202,203,5,59,0,0,203,33,1,0,0,0,204,
        205,5,16,0,0,205,206,5,68,0,0,206,207,5,17,0,0,207,217,5,64,0,0,
        208,209,5,16,0,0,209,210,5,68,0,0,210,211,5,18,0,0,211,212,5,68,
        0,0,212,213,5,58,0,0,213,214,3,14,7,0,214,215,5,59,0,0,215,217,1,
        0,0,0,216,204,1,0,0,0,216,208,1,0,0,0,217,35,1,0,0,0,218,219,5,16,
        0,0,219,220,5,68,0,0,220,221,5,19,0,0,221,224,5,58,0,0,222,225,3,
        14,7,0,223,225,3,18,9,0,224,222,1,0,0,0,224,223,1,0,0,0,225,226,
        1,0,0,0,226,227,5,59,0,0,227,249,1,0,0,0,228,229,5,22,0,0,229,230,
        5,68,0,0,230,231,5,19,0,0,231,234,5,58,0,0,232,235,3,14,7,0,233,
        235,3,18,9,0,234,232,1,0,0,0,234,233,1,0,0,0,235,236,1,0,0,0,236,
        237,5,59,0,0,237,249,1,0,0,0,238,239,5,23,0,0,239,240,5,68,0,0,240,
        241,5,19,0,0,241,244,5,58,0,0,242,245,3,14,7,0,243,245,3,18,9,0,
        244,242,1,0,0,0,244,243,1,0,0,0,245,246,1,0,0,0,246,247,5,59,0,0,
        247,249,1,0,0,0,248,218,1,0,0,0,248,228,1,0,0,0,248,238,1,0,0,0,
        249,37,1,0,0,0,250,251,5,22,0,0,251,252,5,68,0,0,252,253,5,17,0,
        0,253,263,5,64,0,0,254,255,5,22,0,0,255,256,5,68,0,0,256,257,5,18,
        0,0,257,258,5,68,0,0,258,259,5,58,0,0,259,260,3,14,7,0,260,261,5,
        59,0,0,261,263,1,0,0,0,262,250,1,0,0,0,262,254,1,0,0,0,263,39,1,
        0,0,0,264,265,5,23,0,0,265,266,5,68,0,0,266,267,5,17,0,0,267,277,
        5,64,0,0,268,269,5,23,0,0,269,270,5,68,0,0,270,271,5,18,0,0,271,
        272,5,68,0,0,272,273,5,58,0,0,273,274,3,14,7,0,274,275,5,59,0,0,
        275,277,1,0,0,0,276,264,1,0,0,0,276,268,1,0,0,0,277,41,1,0,0,0,278,
        279,5,26,0,0,279,280,5,68,0,0,280,281,5,27,0,0,281,282,3,18,9,0,
        282,43,1,0,0,0,283,284,5,28,0,0,284,285,5,68,0,0,285,286,3,42,21,
        0,286,45,1,0,0,0,17,51,70,82,126,138,145,155,169,171,179,216,224,
        234,244,248,262,276
    ]

class BoardGameParser ( Parser ):

    grammarFileName = "BoardGameParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'GAME'", "'DEFINE'", "'BOARD'", "'PLAYERS'", 
                     "'CONDITIONS'", "'RULES'", "'PIECES'", "'OBSTACLES'", 
                     "'BOOSTERS'", "'PLAYER'", "'COLOR'", "'AT'", "'ORDER'", 
                     "'CONDITION'", "'RULE'", "'PIECE'", "'COUNT'", "'ACTION'", 
                     "'SETUP'", "<INVALID>", "<INVALID>", "'OBSTACLE'", 
                     "'BOOSTER'", "'START'", "'END'", "'MOVE'", "'TO'", 
                     "'TURN'", "'ALL'", "'ANY'", "'NONE'", "'IF'", "'ELSE'", 
                     "'FOR'", "'WHILE'", "'INPUT'", "'PRINT'", "'RETURN'", 
                     "'IN'", "'BREAK'", "'ERROR'", "'AND'", "'OR'", "'NOT'", 
                     "'=='", "'='", "'<'", "'<='", "'>'", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "':'", "'.'", "','", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "GAME", "DEFINE", "BOARD", "PLAYERS", 
                      "CONDITIONS", "RULES", "PIECES", "OBSTACLES", "BOOSTERS", 
                      "PLAYER", "COLOR", "AT", "ORDER", "CONDITION", "RULE", 
                      "PIECE", "COUNT", "ACTION", "SETUP", "BOARD_ROW", 
                      "BOARD_COLUMN", "OBSTACLE", "BOOSTER", "START", "END", 
                      "MOVE", "TO", "TURN", "ALL", "ANY", "NONE", "IF", 
                      "ELSE", "FOR", "WHILE", "INPUT", "PRINT", "RETURN", 
                      "IN", "BREAK", "ERROR", "AND_OPT", "OR_OPT", "NOT_OPT", 
                      "EQUAL_OPT", "ASSIGN_OPT", "LESS_THAN_OPT", "LESS_EQUAL_OPT", 
                      "GREATER_THAN_OPT", "GREATER_EQUAL_OPT", "ADD_OPT", 
                      "SUB_OPT", "MUL_OPT", "DIV_OPT", "COLON", "DOT", "COMMA", 
                      "OPEN_PAR", "CLOSE_PAR", "OPEN_BRACKET", "CLOSE_BRACKET", 
                      "OPEN_BRACE", "CLOSE_BRACE", "INT_LITERAL", "FLOAT_LITERAL", 
                      "STRING_LITERAL", "BOOLEAN_LITERAL", "IDENTIFIER", 
                      "COMMENT", "WS" ]

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
    RULE_game_entities_statement = 13
    RULE_player_statement = 14
    RULE_condition_statement = 15
    RULE_rule_statement = 16
    RULE_piece_statement = 17
    RULE_board_statement = 18
    RULE_obstacle_statement = 19
    RULE_booster_statement = 20
    RULE_move_statement = 21
    RULE_turn_statement = 22

    ruleNames =  [ "program", "define_block", "gameplay_block", "code_block", 
                   "statement", "game_entities", "literal", "param_list", 
                   "object_access", "board_pos", "conditional", "expression", 
                   "conditional_expression", "game_entities_statement", 
                   "player_statement", "condition_statement", "rule_statement", 
                   "piece_statement", "board_statement", "obstacle_statement", 
                   "booster_statement", "move_statement", "turn_statement" ]

    EOF = Token.EOF
    GAME=1
    DEFINE=2
    BOARD=3
    PLAYERS=4
    CONDITIONS=5
    RULES=6
    PIECES=7
    OBSTACLES=8
    BOOSTERS=9
    PLAYER=10
    COLOR=11
    AT=12
    ORDER=13
    CONDITION=14
    RULE=15
    PIECE=16
    COUNT=17
    ACTION=18
    SETUP=19
    BOARD_ROW=20
    BOARD_COLUMN=21
    OBSTACLE=22
    BOOSTER=23
    START=24
    END=25
    MOVE=26
    TO=27
    TURN=28
    ALL=29
    ANY=30
    NONE=31
    IF=32
    ELSE=33
    FOR=34
    WHILE=35
    INPUT=36
    PRINT=37
    RETURN=38
    IN=39
    BREAK=40
    ERROR=41
    AND_OPT=42
    OR_OPT=43
    NOT_OPT=44
    EQUAL_OPT=45
    ASSIGN_OPT=46
    LESS_THAN_OPT=47
    LESS_EQUAL_OPT=48
    GREATER_THAN_OPT=49
    GREATER_EQUAL_OPT=50
    ADD_OPT=51
    SUB_OPT=52
    MUL_OPT=53
    DIV_OPT=54
    COLON=55
    DOT=56
    COMMA=57
    OPEN_PAR=58
    CLOSE_PAR=59
    OPEN_BRACKET=60
    CLOSE_BRACKET=61
    OPEN_BRACE=62
    CLOSE_BRACE=63
    INT_LITERAL=64
    FLOAT_LITERAL=65
    STRING_LITERAL=66
    BOOLEAN_LITERAL=67
    IDENTIFIER=68
    COMMENT=69
    WS=70

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
            self.state = 46
            self.match(BoardGameParser.GAME)
            self.state = 47
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.define_block()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 53
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
            self.state = 55
            self.match(BoardGameParser.DEFINE)
            self.state = 56
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 57
            self.match(BoardGameParser.COLON)
            self.state = 58
            self.code_block()
            self.state = 59
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
            self.state = 61
            self.match(BoardGameParser.START)
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


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(BoardGameParser.StatementContext,0)


        def code_block(self):
            return self.getTypedRuleContext(BoardGameParser.Code_blockContext,0)


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
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.statement()
                self.state = 67
                self.code_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.statement()
                pass


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
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.game_entities_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.board_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.player_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.condition_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.rule_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.piece_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 78
                self.obstacle_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 79
                self.booster_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 80
                self.turn_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 81
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
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1016) != 0)):
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
            self.state = 86
            _la = self._input.LA(1)
            if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 15) != 0)):
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

        def COMMA(self):
            return self.getToken(BoardGameParser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)

        def literal(self):
            return self.getTypedRuleContext(BoardGameParser.LiteralContext,0)


        def ANY(self):
            return self.getToken(BoardGameParser.ANY, 0)

        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)

        def NONE(self):
            return self.getToken(BoardGameParser.NONE, 0)

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
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 89
                self.match(BoardGameParser.COMMA)
                self.state = 90
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 92
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 93
                self.literal()
                self.state = 94
                self.match(BoardGameParser.COMMA)
                self.state = 95
                self.param_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 98
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 99
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 100
                self.match(BoardGameParser.COMMA)
                self.state = 101
                self.param_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 103
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 104
                self.literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 105
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 106
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 107
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.match(BoardGameParser.ANY)
                self.state = 109
                self.match(BoardGameParser.COMMA)
                self.state = 110
                self.param_list()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 111
                self.match(BoardGameParser.ALL)
                self.state = 112
                self.match(BoardGameParser.COMMA)
                self.state = 113
                self.param_list()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 114
                self.match(BoardGameParser.NONE)
                self.state = 115
                self.match(BoardGameParser.COMMA)
                self.state = 116
                self.param_list()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 117
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 118
                self.match(BoardGameParser.NONE)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 119
                self.match(BoardGameParser.ANY)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 120
                self.match(BoardGameParser.ALL)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 121
                self.literal()
                self.state = 122
                self.match(BoardGameParser.COMMA)
                self.state = 123
                self.param_list()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 125
                self.literal()
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

        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)

        def game_entities(self):
            return self.getTypedRuleContext(BoardGameParser.Game_entitiesContext,0)


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
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 129
                self.match(BoardGameParser.DOT)
                self.state = 130
                self.game_entities()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.game_entities()
                self.state = 132
                self.match(BoardGameParser.DOT)
                self.state = 133
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 136
                self.match(BoardGameParser.DOT)
                self.state = 137
                self.match(BoardGameParser.IDENTIFIER)
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

        def BOARD_ROW(self):
            return self.getToken(BoardGameParser.BOARD_ROW, 0)

        def BOARD_COLUMN(self):
            return self.getToken(BoardGameParser.BOARD_COLUMN, 0)

        def BOARD(self):
            return self.getToken(BoardGameParser.BOARD, 0)

        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

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
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(BoardGameParser.BOARD_ROW)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(BoardGameParser.BOARD_COLUMN)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.match(BoardGameParser.BOARD)
                self.state = 143
                self.match(BoardGameParser.DOT)
                self.state = 144
                self.match(BoardGameParser.IDENTIFIER)
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
            self.state = 147
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2177033022996480) != 0)):
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
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 150
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 151
                self.literal()
                pass

            elif la_ == 3:
                self.state = 152
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 153
                self.match(BoardGameParser.DOT)
                self.state = 154
                self.match(BoardGameParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 169
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 158
                        self.match(BoardGameParser.ADD_OPT)
                        self.state = 159
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 160
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 161
                        self.match(BoardGameParser.SUB_OPT)
                        self.state = 162
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 163
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 164
                        self.match(BoardGameParser.MUL_OPT)
                        self.state = 165
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 167
                        self.match(BoardGameParser.DIV_OPT)
                        self.state = 168
                        self.expression(2)
                        pass

             
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.expression(0)
                self.state = 175
                self.conditional()
                self.state = 176
                self.conditional_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.expression(0)
                pass


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
        self.enterRule(localctx, 26, self.RULE_game_entities_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.game_entities()
            self.state = 182
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 183
            self.param_list()
            self.state = 184
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
        self.enterRule(localctx, 28, self.RULE_player_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(BoardGameParser.PLAYER)
            self.state = 187
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 188
            self.match(BoardGameParser.COLOR)
            self.state = 189
            self.object_access()
            self.state = 190
            self.match(BoardGameParser.AT)
            self.state = 191
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
        self.enterRule(localctx, 30, self.RULE_condition_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(BoardGameParser.CONDITION)
            self.state = 194
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 195
            self.param_list()
            self.state = 196
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
        self.enterRule(localctx, 32, self.RULE_rule_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(BoardGameParser.RULE)
            self.state = 199
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 200
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 201
            self.conditional_expression()
            self.state = 202
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
        self.enterRule(localctx, 34, self.RULE_piece_statement)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(BoardGameParser.PIECE)
                self.state = 205
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 206
                self.match(BoardGameParser.COUNT)
                self.state = 207
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(BoardGameParser.PIECE)
                self.state = 209
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 210
                self.match(BoardGameParser.ACTION)
                self.state = 211
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 212
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 213
                self.param_list()
                self.state = 214
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
        self.enterRule(localctx, 36, self.RULE_board_statement)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(BoardGameParser.PIECE)
                self.state = 219
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 220
                self.match(BoardGameParser.SETUP)
                self.state = 221
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 224
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [29, 30, 31, 64, 65, 66, 67, 68]:
                    self.state = 222
                    self.param_list()
                    pass
                elif token in [3, 20, 21]:
                    self.state = 223
                    self.board_pos()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 226
                self.match(BoardGameParser.CLOSE_PAR)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(BoardGameParser.OBSTACLE)
                self.state = 229
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 230
                self.match(BoardGameParser.SETUP)
                self.state = 231
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 234
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [29, 30, 31, 64, 65, 66, 67, 68]:
                    self.state = 232
                    self.param_list()
                    pass
                elif token in [3, 20, 21]:
                    self.state = 233
                    self.board_pos()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 236
                self.match(BoardGameParser.CLOSE_PAR)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.match(BoardGameParser.BOOSTER)
                self.state = 239
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 240
                self.match(BoardGameParser.SETUP)
                self.state = 241
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 244
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [29, 30, 31, 64, 65, 66, 67, 68]:
                    self.state = 242
                    self.param_list()
                    pass
                elif token in [3, 20, 21]:
                    self.state = 243
                    self.board_pos()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 246
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
        self.enterRule(localctx, 38, self.RULE_obstacle_statement)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(BoardGameParser.OBSTACLE)
                self.state = 251
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 252
                self.match(BoardGameParser.COUNT)
                self.state = 253
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(BoardGameParser.OBSTACLE)
                self.state = 255
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 256
                self.match(BoardGameParser.ACTION)
                self.state = 257
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 258
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 259
                self.param_list()
                self.state = 260
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
        self.enterRule(localctx, 40, self.RULE_booster_statement)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(BoardGameParser.BOOSTER)
                self.state = 265
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 266
                self.match(BoardGameParser.COUNT)
                self.state = 267
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(BoardGameParser.BOOSTER)
                self.state = 269
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 270
                self.match(BoardGameParser.ACTION)
                self.state = 271
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 272
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 273
                self.param_list()
                self.state = 274
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
        self.enterRule(localctx, 42, self.RULE_move_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(BoardGameParser.MOVE)
            self.state = 279
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 280
            self.match(BoardGameParser.TO)
            self.state = 281
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
        self.enterRule(localctx, 44, self.RULE_turn_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(BoardGameParser.TURN)
            self.state = 284
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 285
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
         




