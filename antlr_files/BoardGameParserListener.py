# Generated from BoardGameParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BoardGameParser import BoardGameParser
else:
    from BoardGameParser import BoardGameParser

# This class defines a complete listener for a parse tree produced by BoardGameParser.
class BoardGameParserListener(ParseTreeListener):

    # Enter a parse tree produced by BoardGameParser#program.
    def enterProgram(self, ctx:BoardGameParser.ProgramContext):
        print("Entered GAME")

    # Exit a parse tree produced by BoardGameParser#program.
    def exitProgram(self, ctx:BoardGameParser.ProgramContext):
        pass


    # Enter a parse tree produced by BoardGameParser#define_block.
    def enterDefine_block(self, ctx:BoardGameParser.Define_blockContext):
        pass

    # Exit a parse tree produced by BoardGameParser#define_block.
    def exitDefine_block(self, ctx:BoardGameParser.Define_blockContext):
        pass


    # Enter a parse tree produced by BoardGameParser#gameplay_block.
    def enterGameplay_block(self, ctx:BoardGameParser.Gameplay_blockContext):
        pass

    # Exit a parse tree produced by BoardGameParser#gameplay_block.
    def exitGameplay_block(self, ctx:BoardGameParser.Gameplay_blockContext):
        pass


    # Enter a parse tree produced by BoardGameParser#code_block.
    def enterCode_block(self, ctx:BoardGameParser.Code_blockContext):
        pass

    # Exit a parse tree produced by BoardGameParser#code_block.
    def exitCode_block(self, ctx:BoardGameParser.Code_blockContext):
        pass


    # Enter a parse tree produced by BoardGameParser#statement.
    def enterStatement(self, ctx:BoardGameParser.StatementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#statement.
    def exitStatement(self, ctx:BoardGameParser.StatementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#game_entities.
    def enterGame_entities(self, ctx:BoardGameParser.Game_entitiesContext):
        pass

    # Exit a parse tree produced by BoardGameParser#game_entities.
    def exitGame_entities(self, ctx:BoardGameParser.Game_entitiesContext):
        pass


    # Enter a parse tree produced by BoardGameParser#literal.
    def enterLiteral(self, ctx:BoardGameParser.LiteralContext):
        pass

    # Exit a parse tree produced by BoardGameParser#literal.
    def exitLiteral(self, ctx:BoardGameParser.LiteralContext):
        pass


    # Enter a parse tree produced by BoardGameParser#literal_list.
    def enterLiteral_list(self, ctx:BoardGameParser.Literal_listContext):
        pass

    # Exit a parse tree produced by BoardGameParser#literal_list.
    def exitLiteral_list(self, ctx:BoardGameParser.Literal_listContext):
        pass


    # Enter a parse tree produced by BoardGameParser#list_literal.
    def enterList_literal(self, ctx:BoardGameParser.List_literalContext):
        pass

    # Exit a parse tree produced by BoardGameParser#list_literal.
    def exitList_literal(self, ctx:BoardGameParser.List_literalContext):
        pass


    # Enter a parse tree produced by BoardGameParser#param_list.
    def enterParam_list(self, ctx:BoardGameParser.Param_listContext):
        pass

    # Exit a parse tree produced by BoardGameParser#param_list.
    def exitParam_list(self, ctx:BoardGameParser.Param_listContext):
        pass


    # Enter a parse tree produced by BoardGameParser#board_pos.
    def enterBoard_pos(self, ctx:BoardGameParser.Board_posContext):
        pass

    # Exit a parse tree produced by BoardGameParser#board_pos.
    def exitBoard_pos(self, ctx:BoardGameParser.Board_posContext):
        pass


    # Enter a parse tree produced by BoardGameParser#conditional.
    def enterConditional(self, ctx:BoardGameParser.ConditionalContext):
        pass

    # Exit a parse tree produced by BoardGameParser#conditional.
    def exitConditional(self, ctx:BoardGameParser.ConditionalContext):
        pass


    # Enter a parse tree produced by BoardGameParser#expression.
    def enterExpression(self, ctx:BoardGameParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BoardGameParser#expression.
    def exitExpression(self, ctx:BoardGameParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BoardGameParser#conditional_expression.
    def enterConditional_expression(self, ctx:BoardGameParser.Conditional_expressionContext):
        pass

    # Exit a parse tree produced by BoardGameParser#conditional_expression.
    def exitConditional_expression(self, ctx:BoardGameParser.Conditional_expressionContext):
        pass


    # Enter a parse tree produced by BoardGameParser#game_entities_statement.
    def enterGame_entities_statement(self, ctx:BoardGameParser.Game_entities_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#game_entities_statement.
    def exitGame_entities_statement(self, ctx:BoardGameParser.Game_entities_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#player_statement.
    def enterPlayer_statement(self, ctx:BoardGameParser.Player_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#player_statement.
    def exitPlayer_statement(self, ctx:BoardGameParser.Player_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#condition_statement.
    def enterCondition_statement(self, ctx:BoardGameParser.Condition_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#condition_statement.
    def exitCondition_statement(self, ctx:BoardGameParser.Condition_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#rule_statement.
    def enterRule_statement(self, ctx:BoardGameParser.Rule_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#rule_statement.
    def exitRule_statement(self, ctx:BoardGameParser.Rule_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#piece_statement.
    def enterPiece_statement(self, ctx:BoardGameParser.Piece_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#piece_statement.
    def exitPiece_statement(self, ctx:BoardGameParser.Piece_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#board_statement.
    def enterBoard_statement(self, ctx:BoardGameParser.Board_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#board_statement.
    def exitBoard_statement(self, ctx:BoardGameParser.Board_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#obstacle_statement.
    def enterObstacle_statement(self, ctx:BoardGameParser.Obstacle_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#obstacle_statement.
    def exitObstacle_statement(self, ctx:BoardGameParser.Obstacle_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#booster_statement.
    def enterBooster_statement(self, ctx:BoardGameParser.Booster_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#booster_statement.
    def exitBooster_statement(self, ctx:BoardGameParser.Booster_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#move_statement.
    def enterMove_statement(self, ctx:BoardGameParser.Move_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#move_statement.
    def exitMove_statement(self, ctx:BoardGameParser.Move_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#turn_statement.
    def enterTurn_statement(self, ctx:BoardGameParser.Turn_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#turn_statement.
    def exitTurn_statement(self, ctx:BoardGameParser.Turn_statementContext):
        pass



del BoardGameParser