from antlr_files.BoardGameLexer import BoardGameLexer
from antlr_files.BoardGameParser import BoardGameParser
from antlr_files.BoardGameParserVisitor import BoardGameParserVisitor
import antlr_files.BoardGameExceptions as exceptions
from game.models.BoardGameModel import BoardGame
from game.models.PieceModel import Piece
from game.models.PlayerModel import Player
from game.models.BoardCellModel import Cell
from game.models.Colors import Colors
from antlr_files.utils import utils
import copy

class BoardGameInterpreter(BoardGameParserVisitor):

    def __init__(self) -> None:
        super(BoardGameParserVisitor, self).__init__()
        self.res = {}
        self.game = None
        self.order = []
        self.players = {}
        self.temp = None
        self.temp_command = None
        self.indent = ""
        self.symbol_table = [{}]
        self.entities = {}

    ####################
    ### SYMBOL TABLE ###
    ####################

    def enter_scope(self):
        """Enter a new scope."""
        self.symbol_table.append({})

    def exit_scope(self):
        """Exit the current scope."""
        self.symbol_table.pop()

    def declare_symbol(self, name, value=None):
        """Declare a new symbol in the current scope."""
        if name in self.symbol_table[-1]:
            raise Exception(f"Error: Symbol '{name}' is already declared in this scope.")
        self.symbol_table[-1][name] = value

    def assign_symbol(self, name, value):
        """Assign a value to an existing symbol or declare a new one in the current scope."""
        for scope in reversed(self.symbol_table):
            if name in scope:
                scope[name] = value
                return
        # If not found, declare it in the current scope
        self.declare_symbol(name, value)

    def lookup_symbol(self, name):
        """Look up a symbol in the current and enclosing scopes."""
        for scope in reversed(self.symbol_table):
            if name in scope:
                return scope[name]
        raise Exception(f"Error: Symbol '{name}' not found.")
    
    def print_symbol_table(self):
        """Print the current state of the symbol table."""
        print("\nSymbol Table:")
        for i, scope in enumerate(self.symbol_table):
            print(f"Scope {i}: {scope}")
        print()  # Add a blank line for better readability

    ###############
    ### VISITOR ###
    ###############

    # Visit a parse tree produced by BoardGameParser#program.
    def visitProgram(self, ctx:BoardGameParser.ProgramContext):
        # GAME IDENTIFIER define_block+ gameplay_block
        GAME_NAME = ctx.IDENTIFIER()

        print(f"Creating a new board game: {GAME_NAME}")
        self.game = BoardGame(GAME_NAME)
        self.declare_symbol("game", self.game)
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by BoardGameParser#Define.
    def visitDefine(self, ctx:BoardGameParser.DefineContext):
        # DEFINE (IDENTIFIER | object_access) COLON code_block END
        # self.enter_scope()

        if not ctx.END():
            raise exceptions.BoardGameSyntaxError("Syntax error: Missing 'END' keyword.")

        if(ctx.IDENTIFIER()):               # Initializing game settings
            # print(ctx.IDENTIFIER())
            identifier = ctx.IDENTIFIER().getText()
            # print(f"Defined identifier: {identifier}")

            self.visitChildren(ctx)

        else:                               # Specifying game conditions
            # print(ctx.object_access().getText())
            self.visitChildren(ctx)
        
        # self.exit_scope()
        print("\n")


    # Visit a parse tree produced by BoardGameParser#MethodDeclaration.
    def visitMethodDeclaration(self, ctx:BoardGameParser.MethodDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BoardGameParser#Gameplay.
    def visitGameplay(self, ctx:BoardGameParser.GameplayContext):
        # START COLON code_block END   
        if ctx.END() is None:
            raise exceptions.BoardGameSyntaxError("Syntax error: Missing 'END' keyword.")
        
        else:
            print("\n----------------------")
            print("Starting gameplay...")
            self.game.print_board()

        self.enter_scope()  # Enter a new scope for gameplay logic
        # self.game.start_game()
        self.visitChildren(ctx)
        self.exit_scope()


    # Visit a parse tree produced by BoardGameParser#code_block.
    def visitCode_block(self, ctx:BoardGameParser.Code_blockContext):
        # (statement)+
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#statement.
    def visitStatement(self, ctx:BoardGameParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#game_entities.
    def visitGame_entities(self, ctx:BoardGameParser.Game_entitiesContext):
        
        if self.game is None:
            return self.visitChildren(ctx)
        # else:
        #     if ctx.GAME():
        #         return self.game
        #     elif ctx.BOARD():
        #         return self.game.board
        #     elif ctx.PLAYERS():
        #         return self.game.players
        #     elif ctx.PIECES():
        #         return self.game.base_pieces
        #     elif ctx.OBSTACLES():
        #         return self.game.obstacles
        #     elif ctx.BOOSTERS():
        #         return self.game.boosters
        #     elif ctx.CONDITIONS():
        #         return self.game.conditions
        #     elif ctx.RULES():
        #         return self.game.rules

        else:
            if self.temp_command == "ANY":
                if ctx.GAME():
                    return "self"
                elif ctx.BOARD():
                    return "self.board"
                elif ctx.PLAYERS():
                    return "self.players"
                elif ctx.PIECES():
                    return "self.base_pieces"
                elif ctx.OBSTACLES():
                    return "self.obstacles"
                elif ctx.BOOSTERS():
                    return "self.boosters"
                elif ctx.CONDITIONS():
                    return "self.conditions"
                elif ctx.RULES():
                    return "self.rules"
            else:
                if ctx.GAME():
                    return "self"
                elif ctx.BOARD():
                    return "temp.board"
                elif ctx.PLAYERS():
                    return "temp.players"
                elif ctx.PIECES():
                    return "temp.pieces"


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
        if ctx.getText() == "True":
            return True
        else:
            return False

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
        # print(val)
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

    # Visit a parse tree produced by BoardGameParser#BoardPosParam.
    def visitBoardPosParam(self, ctx:BoardGameParser.BoardPosParamContext):
        
        val = self.visit(ctx.board_pos())
        params_list = []
        params_list.append(val)

        others = self.visit(ctx.param_list())
        
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
        return self.visit(ctx.list_())


    # Visit a parse tree produced by BoardGameParser#SingleParam.
    def visitSingleParam(self, ctx:BoardGameParser.SingleParamContext):
        params_list = []
        
        if ctx.ALL():
            params_list.append("ALL") #TODO: Implement this
        elif ctx.ANY():
            params_list.append("ANY") #TODO: Implement this
        elif ctx.NONE():
            params_list.append(None) #TODO: Implement this
        elif ctx.IDENTIFIER():
            params_list.append(ctx.IDENTIFIER().getText()) #TODO: Implement this
        elif ctx.literal():
            params_list.append(self.visit(ctx.literal()))
        elif ctx.board_pos():
            params_list.append(self.visit(ctx.board_pos()))
        elif ctx.object_access():
            params_list.append(self.visit(ctx.object_access())) #TODO: Implement this
        elif ctx.list_():
            params_list.append(self.visit(ctx.list_())) #TODO: Implement this

        return params_list


    # Visit a parse tree produced by BoardGameParser#list.
    def visitList(self, ctx:BoardGameParser.ListContext):
        return self.visit(ctx.param_list())
    

    #####################
    ### OBJECT ACCESS ###
    #####################
    
    # Visit a parse tree produced by BoardGameParser#ObjectEntityAccess.
    def visitObjectEntityAccess(self, ctx:BoardGameParser.ObjectEntityAccessContext):
        parent = ctx.parentCtx
        # print("parent", type(ctx.parentCtx))

        if type(parent) is BoardGameParser.Primary_evalContext:
            print("in primary eval, object entity access")
            for i in ctx.children:
                print(i.getText())

        elif type(parent) not in [BoardGameParser.DefineContext, BoardGameParser.Player_statementContext]:

            if "COLOR" in ctx.getText():
                return ctx.getChild(ctx.getChildCount() - 1).getText()
            
            objs = ctx.getText().split(".")
            script = f"self.game"

            for obj in objs:
                type_obj = type(self.lookup_symbol(obj))
                
                if type_obj == Piece:
                    script += f".get_pieces_by_name('{obj}')"
                elif type_obj == Player:
                    script += f".get_player('{obj}')"

            return script

        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#GameEntityAccess.
    def visitGameEntityAccess(self, ctx:BoardGameParser.GameEntityAccessContext):
        parent = ctx.parentCtx
        # print("parent", type(ctx.parentCtx))

        if type(parent) is BoardGameParser.Primary_evalContext:
            print("in primary eval, game entity access")
            for i in ctx.children:
                print(i.getText())

        elif type(parent) not in [BoardGameParser.DefineContext, BoardGameParser.Player_statementContext]:

            objs = ctx.getText().split(".")
            script = ""

            for obj in objs:
                if objs == BoardGameLexer.symbolicNames[BoardGameLexer.GAME]:
                    script += "self.game"

                elif objs == BoardGameLexer.symbolicNames[BoardGameLexer.BOARD]:
                    script += "self.game.board"

                elif objs == BoardGameLexer.symbolicNames[BoardGameLexer.PLAYERS]:
                    script += "self.game.players"

                elif objs == BoardGameLexer.symbolicNames[BoardGameLexer.PIECES]:
                    script += "self.game.base_pieces"

                elif objs == BoardGameLexer.symbolicNames[BoardGameLexer.OBSTACLES]:
                    script += "self.game.obstacles"

                elif objs == BoardGameLexer.symbolicNames[BoardGameLexer.BOOSTERS]:
                    script += "self.game.boosters"

                elif objs == BoardGameLexer.symbolicNames[BoardGameLexer.CONDITIONS]:
                    script += "self.game.conditions"

                elif objs == BoardGameLexer.symbolicNames[BoardGameLexer.RULES]:
                    script += "self.game.rules"

                elif objs == BoardGameLexer.symbolicNames[BoardGameLexer.TIMER]:
                    script += "self.game.timer"

                else:
                    script += f"{obj}"

                if obj != objs[-1]:
                    script += "."

            return script
        elif type(parent) == BoardGameParser.Player_statementContext:
            #if player parent content
            #always get terminal node
            #gets the child count and then uses the terminal node to assign as input for player
            value = ctx.getChild(ctx.getChildCount() - 1)
            self.players[self.temp] = value
            #self.temp is player and value refers to color but is it always color here??
            self.game.set_player_colors(self.temp, value)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#IdentifierAccess.
    def visitIdentifierAccess(self, ctx:BoardGameParser.IdentifierAccessContext):
        parent = ctx.parentCtx
        # print("parent", type(ctx.parentCtx))

        if type(parent) is BoardGameParser.Primary_evalContext:
            print("in primary eval, identifier access")
            for i in ctx.children:
                print(i.getText())
        return self.visitObjectEntityAccess(ctx)



    # Visit a parse tree produced by BoardGameParser#BoardPosIdentifier.
    def visitBoardPosIdentifier(self, ctx:BoardGameParser.BoardPosIdentifierContext):
        # BOARD DOT IDENTIFIER
        
        pos = ctx.IDENTIFIER().getText()  # Example: "A3"
        board_cell = self.game.board.get_cell_by_name(pos)

        return board_cell

    # Visit a parse tree produced by BoardGameParser#BoardPosRange.
    def visitBoardPosRange(self, ctx:BoardGameParser.BoardPosRangeContext):
        # board_pos ELIPSIS board_pos
        pos1 = self.visit(ctx.getChild(0)).name  # First position, e.g., "A1"
        pos2 = self.visit(ctx.getChild(2)).name  # Second position, e.g., "A5"

        # Extract row and column from positions
        start_row, start_col = ord(pos1[0]), int(pos1[1:])  # e.g., 'A' -> 65, '1' -> 1
        end_row, end_col = ord(pos2[0]), int(pos2[1:])  # e.g., 'A' -> 65, '5' -> 5

        # Check if the positions are in the same row or column
        if start_row != end_row and start_col != end_col:
            raise ValueError(f"Invalid range: {pos1} and {pos2} must be in the same row or column.")

        # Generate the list of positions in the range
        positions = []
        if start_row == end_row:  # Same row
            for col in range(start_col, end_col + 1 if start_col < end_col else end_col - 1, 1 if start_col < end_col else -1):
                positions.append(f"{chr(start_row)}{col}")
        elif start_col == end_col:  # Same column
            for row in range(start_row, end_row + 1 if start_row < end_row else end_row - 1, 1 if start_row < end_row else -1):
                positions.append(f"{chr(row)}{start_col}")

        # print("range", positions)
        board_cells = [self.game.board.get_cell_by_name(pos) for pos in positions]
        return board_cells


    # Visit a parse tree produced by BoardGameParser#BoardPosRowCol.
    def visitBoardPosRowCol(self, ctx:BoardGameParser.BoardPosRowColContext):
        # BOARD DOT (ROW | COLUMN) DOT (int_literal)
        dimension = ctx.getChild(2).getText()  # "ROW" or "COLUMN"
        index = int(ctx.getChild(4).getText())  # Extract the row or column index

        board = self.game.board
        num_rows, num_cols = board.rows, board.cols

        positions = []
        if dimension == "ROW":
            positions = [f"{chr(65 + index - 1)}{col}" for col in range(1, num_cols + 1)]
        elif dimension == "COLUMN":
            positions = [f"{chr(65 + row)}{index}" for row in range(0, num_rows)]

        # print("rowcol", positions)
        board_cells = [board.get_cell_by_name(pos) for pos in positions]
        return board_cells


    # Visit a parse tree produced by BoardGameParser#conditional_opt.
    def visitConditional_opt(self, ctx:BoardGameParser.Conditional_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#objects.
    def visitObjects(self, ctx:BoardGameParser.ObjectsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#method_declaration.
    def visitMethod_declaration(self, ctx:BoardGameParser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#method_call.
    def visitMethod_call(self, ctx:BoardGameParser.Method_callContext):
        objects = self.visit(ctx.objects())
        method = ctx.IDENTIFIER().getText() + "()"
        return f"{objects}.{method}"


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
        l = self.visit(ctx.base_expression())

        if ctx.logical_opt():
            # print("-", ctx.logical_opt().getText(), ctx.expression().getText())
            r = self.visit(ctx.expression())

            if ctx.logical_opt().getText() == BoardGameLexer.symbolicNames[BoardGameLexer.AND_OPT]:
                return l and r
            else:
                return l or r

        else:
            return l
        # else:
        #     print("-1", ctx.getChild(1).getText())
        #     r = self.visit(ctx.getChild(1))

    # Visit a parse tree produced by BoardGameParser#base_expression.
    def visitBase_expression(self, ctx:BoardGameParser.Base_expressionContext):
        l = self.visit(ctx.getChild(0))

        if ctx.getChildCount() > 1:
            r = self.visit(ctx.expression())
            if "temp" in r:
                r = r.replace("temp", "entity")
            return l + r
        elif ctx.getChildCount() == 1:
            return l
    
    # Visit a parse tree produced by BoardGameParser#CountEntity.
    def visitCountEntity(self, ctx:BoardGameParser.CountEntityContext):
        # game_entity = self.visit(ctx.game_entities())

        # return len(game_entity)
        game_entity = self.visit(ctx.game_entities())
        # return f"count_val = len(attr_val) if hasattr(attr_val, '__len__') else None\n"
        return "len(" + game_entity + ")"
    
    # Visit a parse tree produced by BoardGameParser#CountIdentifier.
    # def visitCountIdentifier(self, ctx:BoardGameParser.CountIdentifierContext):
    #     val = self.lookup_symbol(ctx.IDENTIFIER().getText())
    #     if type(val) == Piece:

    #     # return f"count_val = len(attr_val) if hasattr(attr_val, '__len__') else None\n"
    #     return "len(" + game_entity + ")"

    # Visit a parse tree produced by BoardGameParser#CountObjectAccess.
    def visitCountObjectAccess(self, ctx:BoardGameParser.CountObjectAccessContext):
        object_access = self.visit(ctx.object_access())
        # print(object_access)
        script = f"len({object_access})"
        return script
        # return "len(" + object_access + ")"

    # Visit a parse tree produced by BoardGameParser#in_expression.
    def visitIn_expression(self, ctx:BoardGameParser.In_expressionContext):
        l = str(self.visit(ctx.getChild(0)))
        r = str(self.visit(ctx.getChild(2)))

        # for item in r:
        #     if item == l:
        #         return True
        
        return False


    # Visit a parse tree produced by BoardGameParser#at_expression.
    def visitAt_expression(self, ctx:BoardGameParser.At_expressionContext):
        object = self.visit(ctx.getChild(0))
        board_pos = self.visit(ctx.getChild(2))

        print(f"Object: {object}, Position: {board_pos}")
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#any_expression.
    def visitAny_expression(self, ctx:BoardGameParser.Any_expressionContext):
        # print("Depth:", ctx.depth())
        self.temp_command = ctx.ANY().getText()
        py_script = f"{self.indent}for entity in "

        # print("in any expression", ctx.getText())
        if ctx.IDENTIFIER():
            pass
        elif ctx.object_access():
            pass
        elif ctx.list_():
            pass
        elif ctx.game_entities():
            game_entity = self.visit(ctx.game_entities())

            py_script += game_entity
            py_script += ":\n"
            self.indent += "\t"
            # py_script += f"{self.indent}attr_val = getattr(entity, <attr>)\n"

            # print("in any expression\n", py_script)
            self.temp_command = None
            return py_script

        # return self.visitChildren(ctx).getText()

    # Visit a parse tree produced by BoardGameParser#AssignExpression.
    def visitAssignExpression(self, ctx:BoardGameParser.AssignExpressionContext):
        variable_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        self.assign_symbol(variable_name, value)
        print(f"Assigned {variable_name} = {value}")


    # Visit a parse tree produced by BoardGameParser#AssignMethodCall.
    def visitAssignMethodCall(self, ctx:BoardGameParser.AssignMethodCallContext):
        variable_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.method_call())
        self.assign_symbol(variable_name, value)
        print(f"Assigned {variable_name} = {value}")


    # Visit a parse tree produced by BoardGameParser#AssignInput.
    def visitAssignInput(self, ctx:BoardGameParser.AssignInputContext):
        variable_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.input_statement())
        self.assign_symbol(variable_name, value)
        print(f"Assigned {variable_name} = {value}")

    # Visit a parse tree produced by BoardGameParser#AssignEvaluate.
    def visitAssignEvaluate(self, ctx:BoardGameParser.AssignEvaluateContext):
        # print("in assign evaluate")
        variable_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.evaluate_statement())
        self.assign_symbol(variable_name, value)
        print(f"Assigned {variable_name} = {value}")

    # Visit a parse tree produced by BoardGameParser#primary_eval.
    def visitPrimary_eval(self, ctx:BoardGameParser.Primary_evalContext):
        if ctx.int_literal():
            return self.visitInt_literal(ctx.int_literal())
        elif ctx.FLOAT_LITERAL():
            return self.visitFloat(ctx.FLOAT_LITERAL())
        elif ctx.BOOLEAN_LITERAL():
            return self.visitBoolean(ctx.BOOLEAN_LITERAL())
        elif ctx.IDENTIFIER():
            # You can define a variable lookup here.
            try:
                return self.lookup_symbol(ctx.IDENTIFIER().getText())
            except Exception as e:
                raise ValueError(f"Unknown identifier: {ctx.IDENTIFIER().getText()}")
        elif ctx.object_access():
            return self.visit(ctx.object_access())
        else:
            return self.visit(ctx.eval_expression())
    
    # Visit a parse tree produced by BoardGameParser#unary.
    def visitUnary(self, ctx:BoardGameParser.UnaryContext):
        # print("primary_eval", self.visit(ctx.primary_eval()), type(self.visit(ctx.primary_eval())))   
        if ctx.ADD_OPT():
            return self.visit(ctx.primary_eval())
        elif ctx.SUB_OPT():
            return -self.visit(ctx.primary_eval())
        else:
            return self.visit(ctx.primary_eval())

    # Visit a parse tree produced by BoardGameParser#exponent.
    def visitExponent(self, ctx:BoardGameParser.ExponentContext):
        n = len(ctx.unary())
        # Start from the rightmost operand
        res = self.visit(ctx.unary(n - 1))
        for i in range(n - 2, -1, -1):  # Iterate right-to-left
            operator = ctx.getChild(2 * i + 1).getText()  # Operator is at odd indices
            if operator == '^':
                l = self.visit(ctx.unary(i))
                res = l ** res  # Right-to-left exponentiation
        return res

    # Visit a parse tree produced by BoardGameParser#multiplicative.
    def visitMultiplicative(self, ctx:BoardGameParser.MultiplicativeContext):
        l = self.visit(ctx.exponent(0))
        for i in range(1, len(ctx.exponent())):
            operator = ctx.getChild(2 * i - 1).getText()
            r = self.visit(ctx.exponent(i))
            if operator == utils.get_literal_name(BoardGameLexer.MUL_OPT):
                l = l * r
            elif operator == utils.get_literal_name(BoardGameLexer.DIV_OPT):
                if r == 0:
                    raise ZeroDivisionError()
                l = l / r
        # print("multiplicative", l)
        return l

    # Visit a parse tree produced by BoardGameParser#additive.
    def visitAdditive(self, ctx:BoardGameParser.AdditiveContext):
        l = self.visit(ctx.multiplicative(0))
        for i in range(1, len(ctx.multiplicative())):
            operator = ctx.getChild(2 * i - 1).getText()
            r = self.visit(ctx.multiplicative(i))

            if operator == utils.get_literal_name(BoardGameLexer.ADD_OPT):
                l = l + r
            elif operator == utils.get_literal_name(BoardGameLexer.SUB_OPT):
                l = l - r
        # print("additive", l)
        return l

    # Visit a parse tree produced by BoardGameParser#math_expression.
    def visitMath_expression(self, ctx:BoardGameParser.Math_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BoardGameParser#conditional_expression.
    def visitConditional_expression(self, ctx:BoardGameParser.Conditional_expressionContext):
        # print(ctx.getText())
        # print(len(ctx.children))
        # print(type(ctx.parentCtx))
        if type(ctx.parentCtx) not in [BoardGameParser.Eval_base_expressionsContext, BoardGameParser.Not_expressionContext]:
            l = str(self.visit(ctx.getChild(0)))
            # print(l)
            r = str(self.visit(ctx.getChild(2)))
            # print(r, type(r), "\n")
            print(ctx.getText())
            cond_opt = ctx.conditional_opt().getText()

            # if type(ctx.getChild(0)) == BoardGameParser.Entity_count_expressionContext:
            #     return f"{self.indent}return count_val {cond_opt} {r}\n"

            exp = f"{self.indent}return {l} {cond_opt} {r}\n"
            # print(exp)
            return exp
        
    # Visit a parse tree produced by BoardGameParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:BoardGameParser.RelationalExpressionContext):
        l = self.visit(ctx.additive(0))
        for i in range(1, len(ctx.additive())):
            cond_opt = ctx.getChild(2 * i - 1).getText()
            r = self.visit(ctx.additive(i))
            if cond_opt == utils.get_literal_name(BoardGameLexer.EQUAL_OPT):
                l = l == r
            elif cond_opt == utils.get_literal_name(BoardGameLexer.NOT_EQUAL_OPT):
                l = l != r
            elif cond_opt == utils.get_literal_name(BoardGameLexer.GREATER_THAN_OPT):
                l = l > r
            elif cond_opt == utils.get_literal_name(BoardGameLexer.GREATER_EQUAL_OPT):
                l = l >= r
            elif cond_opt == utils.get_literal_name(BoardGameLexer.LESS_THAN_OPT):
                l = l < r
            elif cond_opt == utils.get_literal_name(BoardGameLexer.LESS_EQUAL_OPT):
                l = l <= r
        
        # print("conditional_expression", l)
        return l


    # Visit a parse tree produced by BoardGameParser#StringRelationalExpression.
    def visitStringRelationalExpression(self, ctx:BoardGameParser.StringRelationalExpressionContext):
        l = self.visitString(ctx.STRING_LITERAL(0))
        r = self.visitString(ctx.STRING_LITERAL(1))

        if ctx.EQUAL_OPT():
            return l == r
        elif ctx.NOT_EQUAL_OPT():
            return l != r
        
    # Visit a parse tree produced by BoardGameParser#not_expression.
    def visitNot_expression(self, ctx:BoardGameParser.Not_expressionContext):
        val = self.visit(ctx.relational_expression())
        return (not val)
        
    # Visit a parse tree produced by BoardGameParser#logical_opt.
    def visitLogical_opt(self, ctx:BoardGameParser.Logical_optContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by BoardGameParser#eval_base_expressions.
    def visitEval_base_expressions(self, ctx:BoardGameParser.Eval_base_expressionsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BoardGameParser#eval_expression.
    def visitEval_expression(self, ctx:BoardGameParser.Eval_expressionContext):
        l = self.visit(ctx.eval_base_expressions())

        if ctx.getChildCount() > 1:
            r = self.visit(ctx.eval_expression())
            operator = ctx.getChild(1).getText()
            if operator == utils.get_literal_name(BoardGameLexer.AND_OPT):
                l = l and r
            elif operator == utils.get_literal_name(BoardGameLexer.OR_OPT):
                l = l or r
        # print("eval_expression", l)
        return l
    
    
    ##########################
    ###     STATEMENTS     ###
    ##########################

    # Visit a parse tree produced by BoardGameParser#game_entities_statement.
    def visitGame_entities_statement(self, ctx:BoardGameParser.Game_entities_statementContext):
        # game_entities OPEN_PAR param_list CLOSE_PAR
        game_entity = ctx.game_entities().getText()
        params_list = self.visit(ctx.param_list())

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.GAME]:
            print("\nSetting up game")
        
        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.BOARD]:
            print("\nSetting up board")

            if len(params_list) == 2:
                self.game.set_board(params_list[0], params_list[1])
            else:
                self.game.set_board(params_list[0], params_list[1], params_list[2])
            self.game.display_board()
            self.declare_symbol("board", self.game.board)

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.PLAYERS]:
            print("\nSetting up players")

            for param in params_list:
                player = self.game.add_player(param)
                self.declare_symbol(param, player)

            self.game.display_all_players()

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.PIECES]:
            print("\nSetting up pieces")

            if None in params_list:
                params_list.remove(None)

            for param in params_list:
                base_piece = self.game.create_piece(param)
                self.declare_symbol(param, base_piece)

            self.game.display_base_pieces()

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.OBSTACLES]:
            print("\nSetting up obstacles")

            if None in params_list:
                params_list.remove(None)

            for param in params_list:
                obstacle = self.game.create_obstacle(param)
                self.declare_symbol(param, obstacle)

            self.game.display_obstacles()

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.BOOSTERS]:
            print("\nSetting up boosters")

            if None in params_list:
                params_list.remove(None)

            for param in params_list:
                booster = self.game.create_booster(param)
                self.declare_symbol(param, booster)

            self.game.display_boosters()

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.CONDITIONS]:
            print("\nSetting up conditions")

            if None in params_list:
                params_list.remove(None)

            for param in params_list:
                self.game.set_win_condition(param)
                self.declare_symbol(param)

            self.game.display_win_condition()

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.RULES]:
            print("\nSetting up rules")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.COLOR]:
            print("\nSetting up color")

        if game_entity == BoardGameLexer.symbolicNames[BoardGameLexer.TIMER]:
            print("\nSetting up timer\n")
            self.game.set_timer(params_list[0])
            self.game.display_timer()


    # Visit a parse tree produced by BoardGameParser#player_statement.
    def visitPlayer_statement(self, ctx:BoardGameParser.Player_statementContext):
        #get identifier, object access and add it to board setup
        #take note of order and set that as turn???
        #initialize initially as none then contents will be handled later
        #first step is to check whether beginning word is PLAYER or ORDER
        if ctx.PLAYER(): 
            self.temp = ctx.IDENTIFIER() #temp is used to take note of which player gets assigned which value
            self.players[ctx.IDENTIFIER()] = None

            player_name = ctx.IDENTIFIER().getText()
            player = self.game.get_player(player_name)
            color = self.visit(ctx.object_access())
            # self.assig

        elif ctx.ORDER():
            self.temp_command = "ORDER"
        # print(ctx.getText())
        self.visitChildren(ctx)
        self.game.display_all_players()
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#condition_statement.
    def visitCondition_statement(self, ctx:BoardGameParser.Condition_statementContext):
        # print("\nDefining CONDITIONs")

        func_name = f"check_condition_{len(self.game.conditions)}"
        func_script = f"def {func_name}(self):\n"
        self.indent += "\t"

        # print("disecting expression\n")
        func_script += str(self.visit(ctx.expression()))

        # print("--Symbol Table--")
        # self.print_symbol_table()

        print("\n--Final Script--")
        print(func_script)

        try:
            self.game.add_condition(func_name, func_script)
            self.game.display_conditions()
            self.indent = ""
        except Exception as e:
            raise exceptions.InvalidConditionException() from e


    # Visit a parse tree produced by BoardGameParser#rule_statement.
    def visitRule_statement(self, ctx:BoardGameParser.Rule_statementContext):
        print("\nDefining RULEs")
        print(self.print_symbol_table())
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by BoardGameParser#piece_statement.
    def visitPiece_statement(self, ctx:BoardGameParser.Piece_statementContext):
        print("\nDefining PIECEs")
        
        if ctx.COUNT():
            print("\nSetting count")
            identifier_nodes = ctx.IDENTIFIER()
            count = int(ctx.int_literal().getText())

            for node in identifier_nodes:
                name = node.getText()

                for player in self.game.get_players():
                    
                    for i in range(count):
                        piece = copy.deepcopy(self.game.get_base_pieces(name))
                        piece.set_color(player.color)
                        piece.set_ID(i + 1)
                        player.add_piece(piece)
        else:
            print("\nSetting move")
            param_nodes = ctx.param_list()
            identifier_nodes = ctx.IDENTIFIER()

            for param_list in param_nodes:
                params = param_list.getText()
                params = params.split(",")

                param_dict = {}

                for param in params:
                    key, value = param.split("=")

                    if value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    elif value.isdigit():
                        value = int(value)
                    else:
                        value = value.strip()

                    param_dict[key.strip()] = value

            for node in identifier_nodes:
                name = node.getText()

                print(name)

                for player in self.game.get_players():
                    pieces = player.get_pieces_by_name(name)

                    if pieces:
                        for piece in pieces:
                            print("ENTER HERE")
                            piece.set_move(**param_dict)
                    else:
                        piece = self.game.get_base_pieces(name)
                        piece.set_move(**param_dict)

        # return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#board_statement.
    def visitBoard_statement(self, ctx:BoardGameParser.Board_statementContext):
        print("\nDefining BOARD")

        cells = self.visit(ctx.param_list())
        temp = []

        for c in cells:
            if isinstance(c, str):
                value = c.split('BOARD.')[-1]
                cell = self.game.board.get_cell_by_name(value)
                temp.append(cell)
            elif isinstance(c, list):
                for t in c:
                    if isinstance(t, str):
                        value = t.split('BOARD.')[-1]
                        cell = self.game.board.get_cell_by_name(value)
                        temp.append(cell)
                    else:
                        temp.append(t)
            else:
                temp.append(c)
        
        count=1
        for cell in temp:
            if cell.name[0].isalpha():
                row = (ord(cell.name[0].upper()) % 65)
                col = int(cell.name[1]) - 1
            else:
                row = int(cell.name)
                col = None
            
            # if its a piece 
            if ctx.PIECE():
                self.game.add_piece(ctx.IDENTIFIER()[0].getText().strip(), ctx.IDENTIFIER()[1].getText().strip(), row, col, None, count)
                count+=1
            
            # if its an obstacle
            if ctx.OBSTACLE():
                self.game.place_obstacle(ctx.IDENTIFIER().getText().strip(), row, col)

            # if its a booster
            if ctx.BOOSTER():
                 self.game.place_booster(ctx.IDENTIFIER().getText().strip(), row, col)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#obstacle_statement.
    def visitObstacle_statement(self, ctx:BoardGameParser.Obstacle_statementContext):
        # print("\nDefining OBSTACLEs")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#booster_statement.
    def visitBooster_statement(self, ctx:BoardGameParser.Booster_statementContext):
        # print("\nDefining BOOSTERs")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#move_statement.
    def visitMove_statement(self, ctx:BoardGameParser.Move_statementContext):
        # print("\nMoving PIECEs")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#turn_statement.
    def visitTurn_statement(self, ctx:BoardGameParser.Turn_statementContext):
        # print("\nTaking TURN")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BoardGameParser#dice_statement.
    def visitDice_statement(self, ctx:BoardGameParser.Dice_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#if_statement.
    # Visit a parse tree produced by BoardGameParser#IfElseExpression.
    def visitIfElseExpression(self, ctx:BoardGameParser.IfElseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#IfExpression.
    def visitIfExpression(self, ctx:BoardGameParser.IfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#IfElseEvaluate.
    def visitIfElseEvaluate(self, ctx:BoardGameParser.IfElseEvaluateContext):
        if self.visit(ctx.evaluate_statement()):
            self.visit(ctx.code_block(0))
        else:
            self.visit(ctx.code_block(1))


    # Visit a parse tree produced by BoardGameParser#IfEvaluate.
    def visitIfEvaluate(self, ctx:BoardGameParser.IfEvaluateContext):
        if self.visit(ctx.evaluate_statement()):
            self.visit(ctx.code_block())

    # Visit a parse tree produced by BoardGameParser#evaluate_statement.
    def visitEvaluate_statement(self, ctx:BoardGameParser.Evaluate_statementContext):
        return self.visit(ctx.eval_expression())

    # Visit a parse tree produced by BoardGameParser#for_statement.
    def visitForList(self, ctx:BoardGameParser.ForListContext):
        loop_var = ctx.IDENTIFIER().getText()

        loop_list = self.visit(ctx.list_())
        if not isinstance(loop_list, list):
            raise ValueError(f"Expected a list in 'FOR' statement, but got {type(loop_list)}")

        self.enter_scope()
        try:
            for value in loop_list:
                self.assign_symbol(loop_var, value)
                self.visit(ctx.code_block())
        except exceptions.BreakException:
            pass
        finally:
            self.exit_scope()

    # Visit a parse tree produced by BoardGameParser#ForIdentifier.
    def visitForIdentifier(self, ctx:BoardGameParser.ForIdentifierContext):
        loop_var = ctx.IDENTIFIER(0).getText()

        var_loop_list = ctx.IDENTIFIER(1).getText()
        loop_list = self.lookup_symbol(var_loop_list)
        if not isinstance(loop_list, list):
            raise ValueError(f"Expected a list in 'FOR' statement, but got {type(loop_list)}")

        self.enter_scope()
        try:
            for value in loop_list:
                self.assign_symbol(loop_var, value)
                self.visit(ctx.code_block())
        except exceptions.BreakException:
            pass
        finally:
            self.exit_scope()


    # Visit a parse tree produced by BoardGameParser#while_statement.
    def visitWhile_statement(self, ctx:BoardGameParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#input_statement.
    def visitInput_statement(self, ctx:BoardGameParser.Input_statementContext):
        input_prompt = ""
        if ctx.STRING_LITERAL():
            input_prompt = self.visitString(ctx.STRING_LITERAL()[0])

        identifier = ctx.IDENTIFIER().getText()
        input_val = input(input_prompt)
        self.assign_symbol(identifier, input_val)

    # Visit a parse tree produced by BoardGameParser#print_statement.
    def visitPrint_statement(self, ctx:BoardGameParser.Print_statementContext):
        to_print = self.visit(ctx.param_list())

        for item in to_print:
            item = self.lookup_symbol(item) if item in self.symbol_table[-1] else item
            print(item, end=" ")
        print()


    # Visit a parse tree produced by BoardGameParser#return_statement.
    def visitReturn_statement(self, ctx:BoardGameParser.Return_statementContext):
        return self.visit(ctx.expression())
    
    # Visit a parse tree produced by BoardGameParser#break_statement.
    def visitBreak_statement(self, ctx:BoardGameParser.Break_statementContext):
        raise exceptions.BreakException()
    
