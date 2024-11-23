from antlr_files.BoardGameLexer import BoardGameLexer
from antlr_files.BoardGameParser import BoardGameParser
from antlr_files.BoardGameParserVisitor import BoardGameParserVisitor
# from game.Controller import Controler
from game.models.BoardGameModel import BoardGame

class BoardGameInterpreter(BoardGameParserVisitor):

    def __init__(self) -> None:
        super(BoardGameParserVisitor, self).__init__()
        self.res = {}
        self.game = None
        self.order = []
        self.players = {}
        self.temp = None
        self.temp_command = None

    def visitProgram(self, ctx:BoardGameParser.ProgramContext):
        # GAME IDENTIFIER define_block+ gameplay_block
        GAME_NAME = ctx.IDENTIFIER()
        print("Creating a new board game...")
        self.game = BoardGame(GAME_NAME)
        print(f"Game name: {self.game.name}")

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

    # Visit a parse tree produced by BoardGameParser#Integer.
    def visitInteger(self, ctx:BoardGameParser.IntegerContext):
        return int(ctx.getText())

    # Visit a parse tree produced by BoardGameParser#Float.
    def visitFloat(self, ctx:BoardGameParser.FloatContext):
        return float(ctx.getText())

    # Visit a parse tree produced by BoardGameParser#String.
    def visitString(self, ctx:BoardGameParser.StringContext):
        return str(ctx.getText().strip('"'))

    # Visit a parse tree produced by BoardGameParser#Boolean.
    def visitBoolean(self, ctx:BoardGameParser.BooleanContext):
        return bool(ctx.getText())

    # Visit a parse tree produced by BoardGameParser#primary.
    def visitPrimary(self, ctx:BoardGameParser.PrimaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BoardGameParser#ScoreParam.
    def visitScoreParam(self, ctx:BoardGameParser.ScoreParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#AllAnyNoneParam.
    def visitAllAnyNoneParam(self, ctx:BoardGameParser.AllAnyNoneParamContext):
        val = None
        if ctx.ALL():
            val = "ALL"
        elif ctx.ANY():
            val = "ANY"
        elif ctx.NONE():
            val = "NONE"

        params_list = []
        params_list.append(val)

        others = self.visit(ctx.param_list())
        
        return params_list + others


    # Visit a parse tree produced by BoardGameParser#AssignmentParam.
    def visitAssignmentParam(self, ctx:BoardGameParser.AssignmentParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#VariableParam.
    def visitVariableParam(self, ctx:BoardGameParser.VariableParamContext):
        val = ctx.IDENTIFIER().getText() # TODO: how to make it a variable/access the variable
        print(val)
        params_list = []
        params_list.append(val)

        others = self.visit(ctx.param_list())
        #if temp command was order, it gets the parameters from the param list
        #depending on how it was processed in node, that is the order
        #since DFS, left to right is the order of players
        if self.temp_command == "ORDER":
            self.game.set_turn_order(params_list + others)
            self.temp_command = None
        
        return params_list + others


    # Visit a parse tree produced by BoardGameParser#LiteralParam.
    def visitLiteralParam(self, ctx:BoardGameParser.LiteralParamContext):
        val = self.visit(ctx.literal())
        params_list = []
        params_list.append(val)

        others = self.visit(ctx.param_list())
        
        return params_list + others


    # Visit a parse tree produced by BoardGameParser#ObjectAccessParam.
    def visitObjectAccessParam(self, ctx:BoardGameParser.ObjectAccessParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#ListLiteralParam.
    def visitListLiteralParam(self, ctx:BoardGameParser.ListLiteralParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#SingleParam.
    def visitSingleParam(self, ctx:BoardGameParser.SingleParamContext):
        params_list = []
        
        if ctx.ALL():
            params_list.append("ALL") #TODO: Implement this
        elif ctx.ANY():
            params_list.append("ANY") #TODO: Implement this
        elif ctx.NONE():
            params_list.append("NONE") #TODO: Implement this
        elif ctx.IDENTIFIER():
            params_list.append(ctx.IDENTIFIER().getText()) #TODO: Implement this
        elif ctx.literal():
            params_list.append(self.visit(ctx.literal()))
        elif ctx.object_access():
            params_list.append(self.visit(ctx.object_access())) #TODO: Implement this
        elif ctx.list_():
            params_list.append(self.visit(ctx.list_())) #TODO: Implement this

        return params_list


    # Visit a parse tree produced by BoardGameParser#list.
    def visitList(self, ctx:BoardGameParser.ListContext):
        parent = ctx.parentCtx
        #check parent type and see if its players
        print(type(parent))
        #checks if previous called was actually a player statement
        #if player statement, it does this
        #check if it can be generalized or should be kept like this
        if type(parent) == BoardGameParser.Player_statementContext:
            #check contents of children
            print(ctx.getChild(1))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#object_access.
    def visitObject_access(self, ctx:BoardGameParser.Object_accessContext):
        #check object access and then check which was the parent node above??
        parent = ctx.parentCtx
        #check parent type and see if its players
        print(type(parent))
        if type(parent) == BoardGameParser.Player_statementContext:
            #if player parent content
            #always get terminal node
            #gets the child count and then uses the terminal node to assign as input for player
            value = ctx.getChild(ctx.getChildCount() - 1)
            self.players[self.temp] = value
            #self.temp is player and value refers to color but is it always color here??

            self.game.set_player_colors(self.temp, value)
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
        # l = self.visit(ctx.base_expression())
        print("-0", ctx.getChild(0).getText())
        
        l = self.visit(ctx.getChild(0))

        if ctx.logical_opt():
            print("-", ctx.logical_opt().getText(), ctx.getChild(2).getText())
            r = self.visit(ctx.getChild(2))

            if ctx.logical_opt().getText() == BoardGameLexer.symbolicNames[BoardGameLexer.AND_OPT]:
                return l and r
            else:
                return l or r

        # else:
        #     print("-1", ctx.getChild(1).getText())
        #     r = self.visit(ctx.getChild(1))

    # Visit a parse tree produced by BoardGameParser#conditional_expression.
    def visitConditional_expression(self, ctx:BoardGameParser.Conditional_expressionContext):
        print(ctx.getText())
        print(len(ctx.children))

        l = self.visit(ctx.getChild(0))
        r = self.visit(ctx.getChild(2))

        if ctx.conditional_opt().getText() == BoardGameLexer.symbolicNames[BoardGameLexer.EQUAL_OPT]:
            return l == r
        elif ctx.conditional_opt().getText() == BoardGameLexer.symbolicNames[BoardGameLexer.LESS_THAN_OPT]:
            return l < r
        elif ctx.conditional_opt().getText() == BoardGameLexer.symbolicNames[BoardGameLexer.LESS_EQUAL_OPT]:
            return l <= r
        elif ctx.conditional_opt().getText() == BoardGameLexer.symbolicNames[BoardGameLexer.GREATER_THAN_OPT]:
            return l > r
        elif ctx.conditional_opt().getText() == BoardGameLexer.symbolicNames[BoardGameLexer.GREATER_EQUAL_OPT]:
            return l >= r
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#in_expression.
    def visitIn_expression(self, ctx:BoardGameParser.In_expressionContext):
        l = self.visit(ctx.getChild(0))
        r = self.visit(ctx.getChild(2))

        for item in r:
            if item == l:
                return True
        
        return False


    # Visit a parse tree produced by BoardGameParser#at_expression.
    def visitAt_expression(self, ctx:BoardGameParser.At_expressionContext):
        l = self.visit(ctx.getChild(0))
        r = self.visit(ctx.getChild(2))
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#any_expression.
    def visitAny_expression(self, ctx:BoardGameParser.Any_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#assignment_expression.
    def visitAssignment_expression(self, ctx:BoardGameParser.Assignment_expressionContext):
        l = self.visit(ctx.getChild(0))
        r = self.visit(ctx.getChild(2))
        
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
        l = self.visit(ctx.getChild(0))
        r = self.visit(ctx.getChild(2))

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
        params_list = self.visit(ctx.param_list())

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.GAME]:
            print("\nSetting up game")
        
        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.BOARD]:
            print("\nSetting up board")
            
            print("Params list:")
            for param in params_list:
                print(param, type(param))

            if len(params_list) == 2:
                self.game.set_board(params_list[0], params_list[1])
            else:
                self.game.set_board(params_list[0], params_list[1], params_list[2])
            self.game.display_board()

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.PLAYERS]:
            print("\nSetting up players")

            print("Params list:")
            for param in params_list:
                print(param, type(param))
                self.game.add_player(param)

            self.game.display_all_players()

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.CONDITIONS]:
            print("\nSetting up conditions")

            print("Params list:")
            for param in params_list:
                print(param, type(param))
            
            self.game.set_win_condition(params_list[0])

            self.game.display_win_condition()

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.RULES]:
            print("\nSetting up rules")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.PIECES]:
            print("\nSetting up pieces")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.OBSTACLES]:
            print("\nSetting up obstacles")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.BOOSTERS]:
            print("\nSetting up boosters")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.COLOR]:
            print("\nSetting up color")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.SCORE]:
            print("\nSetting up score")


    # Visit a parse tree produced by BoardGameParser#player_statement.
    def visitPlayer_statement(self, ctx:BoardGameParser.Player_statementContext):
        #get identifier, object access and add it to board setup
        #take note of order and set that as turn???
        #initialize initially as none then contents will be handled later
        #first step is to check whether beginning word is PLAYER or ORDER
        if ctx.PLAYER(): 
            self.temp = ctx.IDENTIFIER() #temp is used to take note of which player gets assigned which value
            self.players[ctx.IDENTIFIER()] = None
        elif ctx.ORDER():
            self.temp_command = "ORDER"
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
