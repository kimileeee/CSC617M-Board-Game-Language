parser grammar BoardGameParser;
options {
    tokenVocab=BoardGameLexer;
}

program : GAME IDENTIFIER define_block+ gameplay_block
        ;

define_block : DEFINE (IDENTIFIER | object_access) COLON code_block END         # Define
             | method_declaration                                               # MethodDeclaration
             ;

gameplay_block : START COLON code_block END                                     # Gameplay
               ;

code_block  : (statement)+ //person should have at least one or more statements when creating code
            ;

statement   : game_entities_statement
            | board_statement
            | player_statement
            | condition_statement
            | rule_statement
            | piece_statement
            | obstacle_statement
            | booster_statement
            | turn_statement
            | move_statement
            | dice_statement
            | expression
            | if_statement
            | for_statement
            | while_statement
            | input_statement
            | print_statement
            | return_statement
            | break_statement
            ;

game_entities : BOARD
              | GAME
              | PLAYERS
              | CONDITIONS
              | RULES
              | PIECES
              | OBSTACLES
              | BOOSTERS
              | COLOR
              | SCORE //added this to indicate that it can be set
              | TIMER
              ;

int_literal : POSITIVE_INT_LITERAL
            | NEGATIVE_INT_LITERAL
            ;

literal : int_literal                           # Integer
        | FLOAT_LITERAL                         # Float
        | STRING_LITERAL                        # String
        | BOOLEAN_LITERAL                       # Boolean
        ;

primary : literal
        | list       
        | IDENTIFIER
        | object_access              
        | OPEN_PAR expression CLOSE_PAR
        | method_call
        | entity_count_expression
;

param_list : SCORE OPEN_PAR IDENTIFIER DOT CONDITIONS CLOSE_PAR                                 # ScoreParam
           | (ALL | ANY | NONE) COMMA param_list                                                # AllAnyNoneParam      
           | assignment_expression COMMA param_list                                             # AssignmentParam
           | literal COMMA param_list                                                           # LiteralParam
           | IDENTIFIER COMMA param_list                                                        # VariableParam
           | board_pos COMMA param_list                                                         # BoardPosParam
           | object_access COMMA param_list                                                     # ObjectAccessParam
           | list COMMA param_list                                                              # ListLiteralParam
           | (ALL | ANY | NONE | IDENTIFIER | literal | object_access | list | assignment_expression | board_pos)       # SingleParam
           ;

list : OPEN_BRACKET param_list CLOSE_BRACKET
     ;

object_access : IDENTIFIER DOT game_entities (DOT game_entities | IDENTIFIER)*                  # ObjectEntityAccess
              | game_entities DOT IDENTIFIER (DOT game_entities | IDENTIFIER)*                  # GameEntityAccess
              | IDENTIFIER DOT IDENTIFIER (DOT game_entities | IDENTIFIER)*                     # IdentifierAccess
              ;
        
//BOARD DOT IDENTIFIER can also be handled by object access thanks to game_entities DOT IDENTIFIER?
//solution is to either remove BOARD from game entities and let it purely be handled by board_pos?
board_pos : BOARD DOT IDENTIFIER                                # BoardPosIdentifier
          | BOARD DOT (ROW | COLUMN) DOT (int_literal)          # BoardPosRowCol
          | board_pos ELIPSIS board_pos                         # BoardPosRange
          ;

conditional_opt : EQUAL_OPT 
                | NOT_EQUAL_OPT
                | LESS_THAN_OPT 
                | LESS_EQUAL_OPT 
                | GREATER_THAN_OPT 
                | GREATER_EQUAL_OPT
                ;

expression : base_expression logical_opt expression
           | base_expression
           ;

entity_count_expression : game_entities DOT COUNT           # CountEntity
                        | IDENTIFIER DOT COUNT              # CountIdentifier
                        | object_access DOT COUNT           # CountObjectAccess
                        ;

base_expression
    : primary
    | assignment_expression
    | math_expression
    | in_expression
    | at_expression
    | conditional_expression
    | move_statement
    | any_expression expression
    | NOT_OPT expression
    | entity_count_expression
    ;

objects : IDENTIFIER
        | board_pos
        | object_access
        ;

method_declaration : DEFINE IDENTIFIER OPEN_PAR param_list CLOSE_PAR COLON code_block END
                   ;

method_call : objects DOT IDENTIFIER OPEN_PAR param_list* CLOSE_PAR
            ;

class_define_block : DEFINE IDENTIFIER COLON (class_statement)+ END
                   ;

class_statement : assignment_expression
                | method_declaration
                ;

conditional_expression : primary conditional_opt primary
                       ;

relational_expression : additive (conditional_opt additive)*                            # RelationalExpression
                      | STRING_LITERAL (EQUAL_OPT | NOT_EQUAL_OPT) STRING_LITERAL       # StringRelationalExpression
                      ;

in_expression : primary IN primary
              ;

at_expression : (IDENTIFIER | object_access) AT board_pos
              | ANY (IDENTIFIER | object_access) AT board_pos
              ;

any_expression : ANY (IDENTIFIER | object_access | list | game_entities)
               ;

assignment_expression : IDENTIFIER ASSIGN_OPT expression              # AssignExpression
                      | IDENTIFIER ASSIGN_OPT evaluate_statement        # AssignEvaluate
                      | IDENTIFIER ASSIGN_OPT method_call               # AssignMethodCall
                      | IDENTIFIER ASSIGN_OPT input_statement         # AssignInput
                      | IDENTIFIER ASSIGN_OPT object_access         # AssignObjectAccess
                      | IDENTIFIER ASSIGN_OPT list         # AssignObjectAccess
                     ;

eval_base_expressions   : relational_expression
                        | not_expression
                        | BOOLEAN_LITERAL
                        ;

eval_expression : eval_base_expressions logical_opt eval_expression
                | eval_base_expressions
                ;

not_expression : NOT_OPT relational_expression
               ;

evaluate_statement : EVALUATE OPEN_PAR eval_expression CLOSE_PAR
                   ;

primary_eval : OPEN_PAR eval_expression CLOSE_PAR
             | int_literal
             | FLOAT_LITERAL
             | BOOLEAN_LITERAL
             | IDENTIFIER
             | object_access
             ;

unary : (ADD_OPT | SUB_OPT)? primary_eval
      ;

exponent : unary (EXP_OPT unary)*
         ;

multiplicative : exponent ((MUL_OPT | DIV_OPT) exponent)*
               ;

additive : multiplicative ((ADD_OPT | SUB_OPT) multiplicative)*
         ;


math_expression : additive
                ;

logical_opt : AND_OPT 
            | OR_OPT
            ;

game_entities_statement : game_entities OPEN_PAR param_list CLOSE_PAR
                        ;

player_statement : PLAYER IDENTIFIER COLOR object_access AT board_pos
                 | ORDER OPEN_PAR list CLOSE_PAR
                 ;

condition_statement : CONDITION OPEN_PAR expression CLOSE_PAR
                    ;

rule_statement : RULE OPEN_PAR param_list CLOSE_PAR
               ;

piece_statement : PIECE (IDENTIFIER | object_access | ALL | OPEN_PAR param_list CLOSE_PAR) COUNT int_literal 
                | PIECE (IDENTIFIER | object_access | ALL | OPEN_PAR param_list CLOSE_PAR) ACTION OPEN_PAR param_list CLOSE_PAR (COMMA IDENTIFIER OPEN_PAR param_list CLOSE_PAR)*
                | PIECE (IDENTIFIER | object_access | ALL | OPEN_PAR param_list CLOSE_PAR | ANY | NONE) ACTION OPEN_PAR expression CLOSE_PAR (COMMA IDENTIFIER OPEN_PAR expression CLOSE_PAR)*
                | PIECE assignment_expression
                ;

board_statement : PLAYER IDENTIFIER PIECE (IDENTIFIER | object_access | ALL) SETUP OPEN_PAR (param_list | board_pos) CLOSE_PAR
                | PLAYER IDENTIFIER OBSTACLE (IDENTIFIER | object_access | ALL) SETUP OPEN_PAR (param_list | board_pos) CLOSE_PAR
                | PLAYER IDENTIFIER BOOSTER (IDENTIFIER | object_access | ALL) SETUP OPEN_PAR (param_list | board_pos) CLOSE_PAR
                ;

obstacle_statement : OBSTACLE (IDENTIFIER | object_access | ALL) COUNT int_literal
                   | OBSTACLE (IDENTIFIER | object_access | ALL) ACTION IDENTIFIER OPEN_PAR param_list CLOSE_PAR (COMMA IDENTIFIER OPEN_PAR param_list CLOSE_PAR)*
                   ;

booster_statement : BOOSTER (IDENTIFIER | object_access | ALL) COUNT int_literal
                  | BOOSTER (IDENTIFIER | object_access | ALL) ACTION IDENTIFIER OPEN_PAR param_list CLOSE_PAR (COMMA IDENTIFIER OPEN_PAR param_list CLOSE_PAR)*
                  ;

move_statement : MOVE (IDENTIFIER | object_access | ALL) TO board_pos
               ;

turn_statement : TURN IDENTIFIER move_statement
               ;

if_statement : IF expression THEN code_block ELSE code_block END                # IfElseExpression
             | IF expression THEN code_block END                                # IfExpression
             | IF evaluate_statement THEN code_block ELSE code_block END        # IfElseEvaluate
             | IF evaluate_statement THEN code_block END                        # IfEvaluate
             ;

for_statement : FOR IDENTIFIER IN list COLON code_block END             # ForList
              | FOR IDENTIFIER IN IDENTIFIER COLON code_block END       # ForIdentifier
              ;

while_statement : WHILE expression COLON code_block END
                ;

input_statement : IDENTIFIER ASSIGN_OPT INPUT OPEN_PAR STRING_LITERAL* CLOSE_PAR
                ;

print_statement : PRINT OPEN_PAR (param_list) CLOSE_PAR
                | PRINT OPEN_PAR  CLOSE_PAR
                ;

return_statement : RETURN expression
                 ;

// timer_statement : TIMER OPEN_PAR POSITIVE_INT_LITERAL CLOSE_PAR //i set this as positive_int_literal since timer cannot be negative
//                 ;

dice_statement  : DICE OPEN_PAR int_literal COMMA int_literal CLOSE_PAR //i imagine it as DICE(1,6) where it rolls the possible numbers
                ; //currently its set as this in case of games that allow negative numbers since some games allow those type of dice rolls

break_statement : BREAK
                ;