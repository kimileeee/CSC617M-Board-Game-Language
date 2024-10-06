# Generated from BoardGameParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BoardGameParser import BoardGameParser
else:
    from BoardGameParser import BoardGameParser

# This class defines a complete generic visitor for a parse tree produced by BoardGameParser.

class BoardGameParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BoardGameParser#program.
    def visitProgram(self, ctx:BoardGameParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#define_block.
    def visitDefine_block(self, ctx:BoardGameParser.Define_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#gameplay_block.
    def visitGameplay_block(self, ctx:BoardGameParser.Gameplay_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#code_block.
    def visitCode_block(self, ctx:BoardGameParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#statement.
    def visitStatement(self, ctx:BoardGameParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#game_entities.
    def visitGame_entities(self, ctx:BoardGameParser.Game_entitiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#literal.
    def visitLiteral(self, ctx:BoardGameParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#literal_list.
    def visitLiteral_list(self, ctx:BoardGameParser.Literal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#list_literal.
    def visitList_literal(self, ctx:BoardGameParser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#param_list.
    def visitParam_list(self, ctx:BoardGameParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#board_pos.
    def visitBoard_pos(self, ctx:BoardGameParser.Board_posContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#conditional.
    def visitConditional(self, ctx:BoardGameParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#expression.
    def visitExpression(self, ctx:BoardGameParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#conditional_expression.
    def visitConditional_expression(self, ctx:BoardGameParser.Conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#game_entities_statement.
    def visitGame_entities_statement(self, ctx:BoardGameParser.Game_entities_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#player_statement.
    def visitPlayer_statement(self, ctx:BoardGameParser.Player_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#condition_statement.
    def visitCondition_statement(self, ctx:BoardGameParser.Condition_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#rule_statement.
    def visitRule_statement(self, ctx:BoardGameParser.Rule_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#piece_statement.
    def visitPiece_statement(self, ctx:BoardGameParser.Piece_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#board_statement.
    def visitBoard_statement(self, ctx:BoardGameParser.Board_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#obstacle_statement.
    def visitObstacle_statement(self, ctx:BoardGameParser.Obstacle_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#booster_statement.
    def visitBooster_statement(self, ctx:BoardGameParser.Booster_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#move_statement.
    def visitMove_statement(self, ctx:BoardGameParser.Move_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#turn_statement.
    def visitTurn_statement(self, ctx:BoardGameParser.Turn_statementContext):
        return self.visitChildren(ctx)



del BoardGameParser