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


    # Visit a parse tree produced by BoardGameParser#Define.
    def visitDefine(self, ctx:BoardGameParser.DefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#MethodDeclaration.
    def visitMethodDeclaration(self, ctx:BoardGameParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#Gameplay.
    def visitGameplay(self, ctx:BoardGameParser.GameplayContext):
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


    # Visit a parse tree produced by BoardGameParser#int_literal.
    def visitInt_literal(self, ctx:BoardGameParser.Int_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#Integer.
    def visitInteger(self, ctx:BoardGameParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#Float.
    def visitFloat(self, ctx:BoardGameParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#String.
    def visitString(self, ctx:BoardGameParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#Boolean.
    def visitBoolean(self, ctx:BoardGameParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#primary.
    def visitPrimary(self, ctx:BoardGameParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#ScoreParam.
    def visitScoreParam(self, ctx:BoardGameParser.ScoreParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#AllAnyNoneParam.
    def visitAllAnyNoneParam(self, ctx:BoardGameParser.AllAnyNoneParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#AssignmentParam.
    def visitAssignmentParam(self, ctx:BoardGameParser.AssignmentParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#LiteralParam.
    def visitLiteralParam(self, ctx:BoardGameParser.LiteralParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#VariableParam.
    def visitVariableParam(self, ctx:BoardGameParser.VariableParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#BoardPosParam.
    def visitBoardPosParam(self, ctx:BoardGameParser.BoardPosParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#ObjectAccessParam.
    def visitObjectAccessParam(self, ctx:BoardGameParser.ObjectAccessParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#ListLiteralParam.
    def visitListLiteralParam(self, ctx:BoardGameParser.ListLiteralParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#SingleParam.
    def visitSingleParam(self, ctx:BoardGameParser.SingleParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#list.
    def visitList(self, ctx:BoardGameParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#ObjectEntityAccess.
    def visitObjectEntityAccess(self, ctx:BoardGameParser.ObjectEntityAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#GameEntityAccess.
    def visitGameEntityAccess(self, ctx:BoardGameParser.GameEntityAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#IdentifierAccess.
    def visitIdentifierAccess(self, ctx:BoardGameParser.IdentifierAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#BoardPosRowCol.
    def visitBoardPosRowCol(self, ctx:BoardGameParser.BoardPosRowColContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#BoardPosIdentifier.
    def visitBoardPosIdentifier(self, ctx:BoardGameParser.BoardPosIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#BoardPosRange.
    def visitBoardPosRange(self, ctx:BoardGameParser.BoardPosRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#conditional_opt.
    def visitConditional_opt(self, ctx:BoardGameParser.Conditional_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#expression.
    def visitExpression(self, ctx:BoardGameParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#CountEntity.
    def visitCountEntity(self, ctx:BoardGameParser.CountEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#CountIdentifier.
    def visitCountIdentifier(self, ctx:BoardGameParser.CountIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#CountObjectAccess.
    def visitCountObjectAccess(self, ctx:BoardGameParser.CountObjectAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#base_expression.
    def visitBase_expression(self, ctx:BoardGameParser.Base_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#objects.
    def visitObjects(self, ctx:BoardGameParser.ObjectsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#method_declaration.
    def visitMethod_declaration(self, ctx:BoardGameParser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#method_call.
    def visitMethod_call(self, ctx:BoardGameParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#class_define_block.
    def visitClass_define_block(self, ctx:BoardGameParser.Class_define_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#class_statement.
    def visitClass_statement(self, ctx:BoardGameParser.Class_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#conditional_expression.
    def visitConditional_expression(self, ctx:BoardGameParser.Conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:BoardGameParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#StringRelationalExpression.
    def visitStringRelationalExpression(self, ctx:BoardGameParser.StringRelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#in_expression.
    def visitIn_expression(self, ctx:BoardGameParser.In_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#at_expression.
    def visitAt_expression(self, ctx:BoardGameParser.At_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#any_expression.
    def visitAny_expression(self, ctx:BoardGameParser.Any_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#AssignExpression.
    def visitAssignExpression(self, ctx:BoardGameParser.AssignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#AssignEvaluate.
    def visitAssignEvaluate(self, ctx:BoardGameParser.AssignEvaluateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#AssignMethodCall.
    def visitAssignMethodCall(self, ctx:BoardGameParser.AssignMethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#AssignInput.
    def visitAssignInput(self, ctx:BoardGameParser.AssignInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#eval_base_expressions.
    def visitEval_base_expressions(self, ctx:BoardGameParser.Eval_base_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#eval_expression.
    def visitEval_expression(self, ctx:BoardGameParser.Eval_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#not_expression.
    def visitNot_expression(self, ctx:BoardGameParser.Not_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#evaluate_statement.
    def visitEvaluate_statement(self, ctx:BoardGameParser.Evaluate_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#primary_eval.
    def visitPrimary_eval(self, ctx:BoardGameParser.Primary_evalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#unary.
    def visitUnary(self, ctx:BoardGameParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#exponent.
    def visitExponent(self, ctx:BoardGameParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#multiplicative.
    def visitMultiplicative(self, ctx:BoardGameParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#additive.
    def visitAdditive(self, ctx:BoardGameParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#math_expression.
    def visitMath_expression(self, ctx:BoardGameParser.Math_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#logical_opt.
    def visitLogical_opt(self, ctx:BoardGameParser.Logical_optContext):
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


    # Visit a parse tree produced by BoardGameParser#IfElseExpression.
    def visitIfElseExpression(self, ctx:BoardGameParser.IfElseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#IfExpression.
    def visitIfExpression(self, ctx:BoardGameParser.IfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#IfElseEvaluate.
    def visitIfElseEvaluate(self, ctx:BoardGameParser.IfElseEvaluateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#IfEvaluate.
    def visitIfEvaluate(self, ctx:BoardGameParser.IfEvaluateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#for_statement.
    def visitFor_statement(self, ctx:BoardGameParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#while_statement.
    def visitWhile_statement(self, ctx:BoardGameParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#input_statement.
    def visitInput_statement(self, ctx:BoardGameParser.Input_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#print_statement.
    def visitPrint_statement(self, ctx:BoardGameParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#return_statement.
    def visitReturn_statement(self, ctx:BoardGameParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#dice_statement.
    def visitDice_statement(self, ctx:BoardGameParser.Dice_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#convert_statement.
    def visitConvert_statement(self, ctx:BoardGameParser.Convert_statementContext):
        return self.visitChildren(ctx)



del BoardGameParser