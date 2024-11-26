from antlr_files.BoardGameLexer import BoardGameLexer
from antlr_files.BoardGameParser import BoardGameParser
from antlr_files.BoardGameParserVisitor import BoardGameParserVisitor
# from game.Controller import Controler
from game.models.BoardGameModel import BoardGame
from game.models.PieceModel import Piece
from game.models.PlayerModel import Player
from game.models.Colors import Colors
from antlr_files.utils import utils

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
    
    # Visit a parse tree produced by BoardGameParser#define_block.
    def visitDefine_block(self, ctx:BoardGameParser.Define_blockContext):
        # DEFINE (IDENTIFIER | object_access) COLON code_block END
        # self.enter_scope()

        if(ctx.IDENTIFIER()):               # Initializing game settings
            # print(ctx.IDENTIFIER())
            identifier = ctx.IDENTIFIER().getText()
            self.declare_symbol(identifier)
            # print(f"Defined identifier: {identifier}")

            self.visitChildren(ctx)

        else:                               # Specifying game conditions
            # print(ctx.object_access().getText())
            self.visitChildren(ctx)
        
        # self.exit_scope()
        print("\n")

    # Visit a parse tree produced by BoardGameParser#Gameplay.
    def visitGameplay(self, ctx:BoardGameParser.GameplayContext):
        # START COLON code_block END   
        print("\n----------------------")
        print("Starting gameplay...")

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
        return self.visitChildren(ctx)

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
        parent = ctx.parentCtx
        #check parent type and see if its players
        # print(type(parent))
        #checks if previous called was actually a player statement
        #if player statement, it does this
        #check if it can be generalized or should be kept like this
        # if type(parent) == BoardGameParser.Player_statementContext:
        #     #check contents of children
        #     print(ctx.getChild(1))
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by BoardGameParser#ObjectEntityAccess.
    def visitObjectEntityAccess(self, ctx:BoardGameParser.ObjectEntityAccessContext):
        parent = ctx.parentCtx

        if type(parent) not in [BoardGameParser.DefineContext, BoardGameParser.Player_statementContext]:

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

        if type(parent) not in [BoardGameParser.DefineContext, BoardGameParser.Player_statementContext]:

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
        return self.visitObjectEntityAccess(ctx)



    # Visit a parse tree produced by BoardGameParser#BoardPosIdentifier.
    def visitBoardPosIdentifier(self, ctx:BoardGameParser.BoardPosIdentifierContext):
        # BOARD DOT IDENTIFIER
        
        pos = ctx.IDENTIFIER().getText()  # Example: "A3"
        board_cell = self.game.board.get_cell_by_name(pos)

        return [board_cell]

    # Visit a parse tree produced by BoardGameParser#BoardPosRange.
    def visitBoardPosRange(self, ctx:BoardGameParser.BoardPosRangeContext):
        # board_pos ELIPSIS board_pos
        pos1 = self.visit(ctx.getChild(0))[0].name  # First position, e.g., "A1"
        pos2 = self.visit(ctx.getChild(2))[0].name  # Second position, e.g., "A5"

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
    
    # Visit a parse tree produced by BoardGameParser#conditional_expression.
    def visitConditional_expression(self, ctx:BoardGameParser.Conditional_expressionContext):
        # print(ctx.getText())
        # print(len(ctx.children))

        l = str(self.visit(ctx.getChild(0)))
        # print(l)
        r = str(self.visit(ctx.getChild(2)))
        # print(r, type(r), "\n")

        cond_opt = ctx.conditional_opt().getText()

        # if type(ctx.getChild(0)) == BoardGameParser.Entity_count_expressionContext:
        #     return f"{self.indent}return count_val {cond_opt} {r}\n"

        exp = f"{self.indent}return {l} {cond_opt} {r}\n"
        # print(exp)
        return exp

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
        l = self.visit(ctx.getChild(0))
        r = self.visit(ctx.getChild(2))
        
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
        self.declare_symbol(variable_name, value)
        print(f"Assigned {variable_name} = {value}")


    # Visit a parse tree produced by BoardGameParser#AssignMethodCall.
    def visitAssignMethodCall(self, ctx:BoardGameParser.AssignMethodCallContext):
        variable_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.method_call())
        self.declare_symbol(variable_name, value)
        print(f"Assigned {variable_name} = {value}")


    # Visit a parse tree produced by BoardGameParser#AssignInput.
    def visitAssignInput(self, ctx:BoardGameParser.AssignInputContext):
        variable_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.input_statement())
        self.declare_symbol(variable_name, value)
        print(f"Assigned {variable_name} = {value}")


    # Visit a parse tree produced by BoardGameParser#exponent.
    def visitExponent(self, ctx:BoardGameParser.ExponentContext):
        l = self.visit(ctx.getChild(0))
        r = self.visit(ctx.getChild(2))

        if ctx.EXP_OPT().getText():
            return l ** r

    # Visit a parse tree produced by BoardGameParser#multiplicative.
    def visitMultiplicative(self, ctx:BoardGameParser.MultiplicativeContext):
        l = self.visit(ctx.getChild(0))
        r = self.visit(ctx.getChild(2))

        if ctx.MUL_OPT().getText():
            return l * r
        elif ctx.DIV_OPT.text:
            if r == 0:
                raise ZeroDivisionError
            return l / r

    # Visit a parse tree produced by BoardGameParser#additive.
    def visitAdditive(self, ctx:BoardGameParser.AdditiveContext):
        l = self.visit(ctx.getChild(0))
        r = self.visit(ctx.getChild(2))

        if ctx.ADD_OPT().getText():
            return l + r
        elif ctx.SUB_OPT().getText():
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

        self.game.add_condition(func_name, func_script)
        self.game.display_conditions()
        self.indent = ""


    # Visit a parse tree produced by BoardGameParser#rule_statement.
    def visitRule_statement(self, ctx:BoardGameParser.Rule_statementContext):
        # print("\nDefining RULEs")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BoardGameParser#piece_statement.
    def visitPiece_statement(self, ctx:BoardGameParser.Piece_statementContext):
        print("\nDefining PIECEs")
        if ctx.COUNT():
            print("\nSetting count")
            identifier_nodes = ctx.IDENTIFIER()
            count = int(ctx.int_literal().getText())
            for node in identifier_nodes:
                name = node.getText()
                piece = self.game.get_base_pieces(name)
                piece.set_count(count)
                print(piece.__repr__())
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
                piece = self.game.get_base_pieces(name)
                piece.set_move(**param_dict)
                print(piece.__repr__())
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#board_statement.
    def visitBoard_statement(self, ctx:BoardGameParser.Board_statementContext):
        print("\nDefining BOARD")

        print(ctx.param_list().getText())

        # positions = ctx.param_list().getText().split(',')

        # list_positions = []
        # for pos in positions:
        #     # Get the part after 'BOARD.'
        #     value = pos.split('BOARD.')[-1]
        #     row_part = value[0]  # 'C'
        #     col_part = value[1]  # '1'

        #     # check if row_part is a character
        #     if row_part.isalpha():  
        #         # convert to uppercase and mod 65 (if row starts at 0)
        #         row_value = (ord(row_part.upper()) % 64)  
                
        #     else:
        #         row_value = int(row_part)  # if already a number, just use it

        #     # check if char_part is a character
        #     if col_part.isalpha():  
        #         # convert to uppercase and mod 65 (if row starts at 0)
        #         col_part = (ord(col_part.upper()) % 64)  

        #     else:
        #         col_value = int(col_part)  # if already a number, just use it

        #     # Append processed values as tuple
        #     list_positions.append((row_value, col_value))
        

        # # if its a piece 
        # if ctx.PIECE():
        #     print("Piece:", ctx.PIECE().getText())
        #     if len(ctx.IDENTIFIER()) > 1:
                
        #         for position in list_positions:
        #             self.game.add_piece(ctx.IDENTIFIER()[0].getText().strip(), ctx.IDENTIFIER()[1].getText().strip(), position[0], position[1], None)
        #     else:
        #         for position in list_positions:
        #             self.game.add_piece(None, ctx.IDENTIFIER()[0].getText().strip(), position[0], position[1], None) 

        # # if its an obstacle
        # if ctx.OBSTACLE():
        #     print("Obstacle:", ctx.OBSTACLE().getText())
        #     for position in list_positions:
        #         self.game.place_obstacle(ctx.IDENTIFIER().getText().strip(), position[0], position[1])

        # # if its a booster
        # if ctx.BOOSTER():
        #     print("Booster:", ctx.BOOSTER().getText())
        #     for position in list_positions:
        #         self.game.place_booster(ctx.IDENTIFIER().getText().strip(), position[0], position[1])
        

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
        if ctx.STRING_LITERAL():
            print(ctx.STRING_LITERAL().getText(), end="")

        input_val = input()
        
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by BoardGameParser#print_statement.
    def visitPrint_statement(self, ctx:BoardGameParser.Print_statementContext):
        to_print = self.visit(ctx.param_list())

        for item in to_print:
            print(item, end=" ")


    # Visit a parse tree produced by BoardGameParser#return_statement.
    def visitReturn_statement(self, ctx:BoardGameParser.Return_statementContext):
        return self.visitChildren(ctx)
