from antlr_files.BoardGameLexer import BoardGameLexer
from antlr_files.BoardGameParser import BoardGameParser
from antlr_files.BoardGameParserVisitor import BoardGameParserVisitor

class BoardGameInterpreter(BoardGameParserVisitor):

    def __init__(self) -> None:
        super(BoardGameParserVisitor, self).__init__()
        self.res = {}

    def visitProgram(self, ctx:BoardGameParser.ProgramContext):
        # GAME IDENTIFIER define_block+ gameplay_block
        GAME_NAME = ctx.IDENTIFIER()
        print("Creating a new board game...")
        print(f"Game name: {GAME_NAME}\n")

        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by BoardGameParser#define_block.
    def visitDefine_block(self, ctx:BoardGameParser.Define_blockContext):

        if(ctx.IDENTIFIER()):               # Initializing game settings
            print(ctx.IDENTIFIER())
            self.visitChildren(ctx)

        else:                               # Specifying game conditions
            print(ctx.object_access().getText())
            self.visitChildren(ctx)
        
        print("\n")
        # print(ctx.IDENTIFIER(), ctx.object_access())
        # print(f"Children of define_block: {[child.getText() for child in ctx.children]}")


    # Visit a parse tree produced by BoardGameParser#gameplay_block.
    def visitGameplay_block(self, ctx:BoardGameParser.Gameplay_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#code_block.
    def visitCode_block(self, ctx:BoardGameParser.Code_blockContext):
        # for c in ctx.children:
        #     print(type(c), c)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#statement.
    def visitStatement(self, ctx:BoardGameParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#game_entities.
    def visitGame_entities(self, ctx:BoardGameParser.Game_entitiesContext):

        return self.visitChildren(ctx)


    ########################
    ###     LITERALS     ###
    ########################

    # Visit a parse tree produced by BoardGameParser#int_literal.
    def visitInt_literal(self, ctx:BoardGameParser.Int_literalContext):
        return int(ctx.getText())


    # Visit a parse tree produced by BoardGameParser#literal.
    def visitLiteral(self, ctx:BoardGameParser.LiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BoardGameParser#primary.
    def visitPrimary(self, ctx:BoardGameParser.PrimaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BoardGameParser#param_list.
    def visitParam_list(self, ctx:BoardGameParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#list.
    def visitList(self, ctx:BoardGameParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#object_access.
    def visitObject_access(self, ctx:BoardGameParser.Object_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#board_pos.
    def visitBoard_pos(self, ctx:BoardGameParser.Board_posContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#conditional_opt.
    def visitConditional_opt(self, ctx:BoardGameParser.Conditional_optContext):
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


    ###########################
    ###     EXPRESSIONS     ###
    ###########################

    # Visit a parse tree produced by BoardGameParser#expression.
    def visitExpression(self, ctx:BoardGameParser.ExpressionContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if ctx.logical_opt().text == BoardGameLexer.symbolicNames[BoardGameLexer.AND_OPT]:
            return l and r
        else:
            return l or r

    # Visit a parse tree produced by BoardGameParser#conditional_expression.
    def visitConditional_expression(self, ctx:BoardGameParser.Conditional_expressionContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if ctx.conditional_opt().text == BoardGameLexer.symbolicNames[BoardGameLexer.EQUAL_OPT]:
            return l == r
        elif ctx.conditional_opt().text == BoardGameLexer.symbolicNames[BoardGameLexer.LESS_THAN_OPT]:
            return l < r
        elif ctx.conditional_opt().text == BoardGameLexer.symbolicNames[BoardGameLexer.LESS_EQUAL_OPT]:
            return l <= r
        elif ctx.conditional_opt().text == BoardGameLexer.symbolicNames[BoardGameLexer.GREATER_THAN_OPT]:
            return l > r
        elif ctx.conditional_opt().text == BoardGameLexer.symbolicNames[BoardGameLexer.GREATER_EQUAL_OPT]:
            return l >= r
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#in_expression.
    def visitIn_expression(self, ctx:BoardGameParser.In_expressionContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        for item in r:
            if item == l:
                return True
        
        return False


    # Visit a parse tree produced by BoardGameParser#at_expression.
    def visitAt_expression(self, ctx:BoardGameParser.At_expressionContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#any_expression.
    def visitAny_expression(self, ctx:BoardGameParser.Any_expressionContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#assignment_expression.
    def visitAssignment_expression(self, ctx:BoardGameParser.Assignment_expressionContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#exponent.
    def visitExponent(self, ctx:BoardGameParser.ExponentContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if ctx.EXP_OPT.text:
            return l ** r

    # Visit a parse tree produced by BoardGameParser#multiplicative.
    def visitMultiplicative(self, ctx:BoardGameParser.MultiplicativeContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if ctx.MUL_OPT.text:
            return l * r
        elif ctx.DIV_OPT.text:
            if r == 0:
                raise ZeroDivisionError
            return l / r

    # Visit a parse tree produced by BoardGameParser#additive.
    def visitAdditive(self, ctx:BoardGameParser.AdditiveContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if ctx.ADD_OPT.text:
            return l + r
        elif ctx.SUB_OPT.text:
            return l - r


    # Visit a parse tree produced by BoardGameParser#math_expression.
    def visitMath_expression(self, ctx:BoardGameParser.Math_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#logical_opt.
    def visitLogical_opt(self, ctx:BoardGameParser.Logical_optContext):
        return self.visitChildren(ctx)
    
    
    ##########################
    ###     STATEMENTS     ###
    ##########################

    # Visit a parse tree produced by BoardGameParser#game_entities_statement.
    def visitGame_entities_statement(self, ctx:BoardGameParser.Game_entities_statementContext):
        game_entity = ctx.game_entities().getText()
        
        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.BOARD]:
            print("Setting up board")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.GAME]:
            print("Setting up game")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.PLAYERS]:
            print("Setting up players")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.CONDITIONS]:
            print("Setting up conditions")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.RULES]:
            print("Setting up rules")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.PIECES]:
            print("Setting up pieces")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.OBSTACLES]:
            print("Setting up obstacles")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.BOOSTERS]:
            print("Setting up boosters")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.COLOR]:
            print("Setting up color")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.SCORE]:
            print("Setting up score")



    # Visit a parse tree produced by BoardGameParser#player_statement.
    def visitPlayer_statement(self, ctx:BoardGameParser.Player_statementContext):
        print(ctx.getText())
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
    
    # Visit a parse tree produced by BoardGameParser#timer_statement.
    def visitTimer_statement(self, ctx:BoardGameParser.Timer_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#dice_statement.
    def visitDice_statement(self, ctx:BoardGameParser.Dice_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#if_statement.
    def visitIf_statement(self, ctx:BoardGameParser.If_statementContext):
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
