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
        print("Creating a new board game...")

        print(ctx)

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


    # Enter a parse tree produced by BoardGameParser#int_literal.
    def enterInt_literal(self, ctx:BoardGameParser.Int_literalContext):
        pass

    # Exit a parse tree produced by BoardGameParser#int_literal.
    def exitInt_literal(self, ctx:BoardGameParser.Int_literalContext):
        pass


    # Enter a parse tree produced by BoardGameParser#literal.
    def enterLiteral(self, ctx:BoardGameParser.LiteralContext):
        pass

    # Exit a parse tree produced by BoardGameParser#literal.
    def exitLiteral(self, ctx:BoardGameParser.LiteralContext):
        pass


    # Enter a parse tree produced by BoardGameParser#primary.
    def enterPrimary(self, ctx:BoardGameParser.PrimaryContext):
        pass

    # Exit a parse tree produced by BoardGameParser#primary.
    def exitPrimary(self, ctx:BoardGameParser.PrimaryContext):
        pass


    # Enter a parse tree produced by BoardGameParser#param_list.
    def enterParam_list(self, ctx:BoardGameParser.Param_listContext):
        pass

    # Exit a parse tree produced by BoardGameParser#param_list.
    def exitParam_list(self, ctx:BoardGameParser.Param_listContext):
        pass


    # Enter a parse tree produced by BoardGameParser#list.
    def enterList(self, ctx:BoardGameParser.ListContext):
        pass

    # Exit a parse tree produced by BoardGameParser#list.
    def exitList(self, ctx:BoardGameParser.ListContext):
        pass


    # Enter a parse tree produced by BoardGameParser#object_access.
    def enterObject_access(self, ctx:BoardGameParser.Object_accessContext):
        pass

    # Exit a parse tree produced by BoardGameParser#object_access.
    def exitObject_access(self, ctx:BoardGameParser.Object_accessContext):
        pass


    # Enter a parse tree produced by BoardGameParser#board_pos.
    def enterBoard_pos(self, ctx:BoardGameParser.Board_posContext):
        pass

    # Exit a parse tree produced by BoardGameParser#board_pos.
    def exitBoard_pos(self, ctx:BoardGameParser.Board_posContext):
        pass


    # Enter a parse tree produced by BoardGameParser#conditional_opt.
    def enterConditional_opt(self, ctx:BoardGameParser.Conditional_optContext):
        pass

    # Exit a parse tree produced by BoardGameParser#conditional_opt.
    def exitConditional_opt(self, ctx:BoardGameParser.Conditional_optContext):
        pass


    # Enter a parse tree produced by BoardGameParser#expression.
    def enterExpression(self, ctx:BoardGameParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BoardGameParser#expression.
    def exitExpression(self, ctx:BoardGameParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BoardGameParser#base_expression.
    def enterBase_expression(self, ctx:BoardGameParser.Base_expressionContext):
        pass

    # Exit a parse tree produced by BoardGameParser#base_expression.
    def exitBase_expression(self, ctx:BoardGameParser.Base_expressionContext):
        pass


    # Enter a parse tree produced by BoardGameParser#objects.
    def enterObjects(self, ctx:BoardGameParser.ObjectsContext):
        pass

    # Exit a parse tree produced by BoardGameParser#objects.
    def exitObjects(self, ctx:BoardGameParser.ObjectsContext):
        pass


    # Enter a parse tree produced by BoardGameParser#method_declaration.
    def enterMethod_declaration(self, ctx:BoardGameParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by BoardGameParser#method_declaration.
    def exitMethod_declaration(self, ctx:BoardGameParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by BoardGameParser#method_call.
    def enterMethod_call(self, ctx:BoardGameParser.Method_callContext):
        pass

    # Exit a parse tree produced by BoardGameParser#method_call.
    def exitMethod_call(self, ctx:BoardGameParser.Method_callContext):
        pass


    # Enter a parse tree produced by BoardGameParser#class_define_block.
    def enterClass_define_block(self, ctx:BoardGameParser.Class_define_blockContext):
        pass

    # Exit a parse tree produced by BoardGameParser#class_define_block.
    def exitClass_define_block(self, ctx:BoardGameParser.Class_define_blockContext):
        pass


    # Enter a parse tree produced by BoardGameParser#class_statement.
    def enterClass_statement(self, ctx:BoardGameParser.Class_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#class_statement.
    def exitClass_statement(self, ctx:BoardGameParser.Class_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#conditional_expression.
    def enterConditional_expression(self, ctx:BoardGameParser.Conditional_expressionContext):
        pass

    # Exit a parse tree produced by BoardGameParser#conditional_expression.
    def exitConditional_expression(self, ctx:BoardGameParser.Conditional_expressionContext):
        pass


    # Enter a parse tree produced by BoardGameParser#in_expression.
    def enterIn_expression(self, ctx:BoardGameParser.In_expressionContext):
        pass

    # Exit a parse tree produced by BoardGameParser#in_expression.
    def exitIn_expression(self, ctx:BoardGameParser.In_expressionContext):
        pass


    # Enter a parse tree produced by BoardGameParser#at_expression.
    def enterAt_expression(self, ctx:BoardGameParser.At_expressionContext):
        pass

    # Exit a parse tree produced by BoardGameParser#at_expression.
    def exitAt_expression(self, ctx:BoardGameParser.At_expressionContext):
        pass


    # Enter a parse tree produced by BoardGameParser#any_expression.
    def enterAny_expression(self, ctx:BoardGameParser.Any_expressionContext):
        pass

    # Exit a parse tree produced by BoardGameParser#any_expression.
    def exitAny_expression(self, ctx:BoardGameParser.Any_expressionContext):
        pass


    # Enter a parse tree produced by BoardGameParser#assignment_expression.
    def enterAssignment_expression(self, ctx:BoardGameParser.Assignment_expressionContext):
        pass

    # Exit a parse tree produced by BoardGameParser#assignment_expression.
    def exitAssignment_expression(self, ctx:BoardGameParser.Assignment_expressionContext):
        pass


    # Enter a parse tree produced by BoardGameParser#exponent.
    def enterExponent(self, ctx:BoardGameParser.ExponentContext):
        pass

    # Exit a parse tree produced by BoardGameParser#exponent.
    def exitExponent(self, ctx:BoardGameParser.ExponentContext):
        pass


    # Enter a parse tree produced by BoardGameParser#multiplicative.
    def enterMultiplicative(self, ctx:BoardGameParser.MultiplicativeContext):
        pass

    # Exit a parse tree produced by BoardGameParser#multiplicative.
    def exitMultiplicative(self, ctx:BoardGameParser.MultiplicativeContext):
        pass


    # Enter a parse tree produced by BoardGameParser#additive.
    def enterAdditive(self, ctx:BoardGameParser.AdditiveContext):
        pass

    # Exit a parse tree produced by BoardGameParser#additive.
    def exitAdditive(self, ctx:BoardGameParser.AdditiveContext):
        pass


    # Enter a parse tree produced by BoardGameParser#math_expression.
    def enterMath_expression(self, ctx:BoardGameParser.Math_expressionContext):
        pass

    # Exit a parse tree produced by BoardGameParser#math_expression.
    def exitMath_expression(self, ctx:BoardGameParser.Math_expressionContext):
        pass


    # Enter a parse tree produced by BoardGameParser#logical_opt.
    def enterLogical_opt(self, ctx:BoardGameParser.Logical_optContext):
        pass

    # Exit a parse tree produced by BoardGameParser#logical_opt.
    def exitLogical_opt(self, ctx:BoardGameParser.Logical_optContext):
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


    # Enter a parse tree produced by BoardGameParser#if_statement.
    def enterIf_statement(self, ctx:BoardGameParser.If_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#if_statement.
    def exitIf_statement(self, ctx:BoardGameParser.If_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#for_statement.
    def enterFor_statement(self, ctx:BoardGameParser.For_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#for_statement.
    def exitFor_statement(self, ctx:BoardGameParser.For_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#while_statement.
    def enterWhile_statement(self, ctx:BoardGameParser.While_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#while_statement.
    def exitWhile_statement(self, ctx:BoardGameParser.While_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#input_statement.
    def enterInput_statement(self, ctx:BoardGameParser.Input_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#input_statement.
    def exitInput_statement(self, ctx:BoardGameParser.Input_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#print_statement.
    def enterPrint_statement(self, ctx:BoardGameParser.Print_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#print_statement.
    def exitPrint_statement(self, ctx:BoardGameParser.Print_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#return_statement.
    def enterReturn_statement(self, ctx:BoardGameParser.Return_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#return_statement.
    def exitReturn_statement(self, ctx:BoardGameParser.Return_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#timer_statement.
    def enterTimer_statement(self, ctx:BoardGameParser.Timer_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#timer_statement.
    def exitTimer_statement(self, ctx:BoardGameParser.Timer_statementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#dice_statement.
    def enterDice_statement(self, ctx:BoardGameParser.Dice_statementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#dice_statement.
    def exitDice_statement(self, ctx:BoardGameParser.Dice_statementContext):
        pass



del BoardGameParser