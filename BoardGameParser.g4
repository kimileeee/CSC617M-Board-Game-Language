parser grammar BoardGameParser;
options {
    tokenVocab=BoardGameLexer;
}

program : GAME IDENTIFIER define_block+ gameplay_block                          # Program
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
            | timer_statement
            | dice_statement
            | expression
            | if_statement
            | for_statement
            | while_statement
            | input_statement
            | print_statement
            | return_statement
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
        | object_access
        | list                                  # List
        | IDENTIFIER                            # Identifier
        | OPEN_PAR expression CLOSE_PAR
        | method_call
;

param_list : SCORE OPEN_PAR IDENTIFIER DOT CONDITIONS CLOSE_PAR
           | (ALL | ANY | NONE) COMMA param_list
           | IDENTIFIER ASSIGN_OPT (literal | objects | method_call) COMMA param_list
           | method_call ASSIGN_OPT (literal | objects | method_call) COMMA param_list
           | IDENTIFIER COMMA param_list
           | literal COMMA param_list
           | object_access COMMA param_list
           | list COMMA param_list
           | (ALL | ANY | NONE | IDENTIFIER | literal | object_access | list)
           ;

list : OPEN_BRACKET param_list CLOSE_BRACKET
     ;

object_access : IDENTIFIER DOT game_entities (DOT game_entities | IDENTIFIER)* //do we allow something like BOARD.PIECES.OBSTACLES??
              | game_entities DOT IDENTIFIER (DOT game_entities | IDENTIFIER)* //should it be DOT identifier 
              | IDENTIFIER DOT IDENTIFIER (DOT game_entities | IDENTIFIER)*
              ;
        
//BOARD DOT IDENTIFIER can also be handled by object access thanks to game_entities DOT IDENTIFIER?
//solution is to either remove BOARD from game entities and let it purely be handled by board_pos?
board_pos : BOARD DOT IDENTIFIER
          | BOARD DOT (ROW | COLUMN) DOT (int_literal)
          | board_pos ELIPSIS board_pos
          ;

conditional_opt : EQUAL_OPT 
             | LESS_THAN_OPT 
             | LESS_EQUAL_OPT 
             | GREATER_THAN_OPT 
             | GREATER_EQUAL_OPT
             ;

expression : base_expression logical_opt expression
           | base_expression
           ;

base_expression
    : assignment_expression
    | math_expression
    | in_expression
    | at_expression
    | conditional_expression
    | move_statement
    | any_expression expression
    | primary
    | NOT_OPT expression
    ;

objects : IDENTIFIER
        | object_access
        | board_pos
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

in_expression : primary IN primary
              ;

at_expression : (IDENTIFIER | object_access) AT board_pos
              ;

any_expression : ANY (IDENTIFIER | object_access | list | game_entities)
               ;

assignment_expression : (IDENTIFIER | IDENTIFIER OPEN_PAR IDENTIFIER CLOSE_PAR) ASSIGN_OPT expression
                      | (IDENTIFIER | IDENTIFIER OPEN_PAR IDENTIFIER CLOSE_PAR) ASSIGN_OPT input_statement
                     ;

exponent : primary (EXP_OPT primary)*
         ;

multiplicative : multiplicative (MUL_OPT | DIV_OPT) exponent
               | exponent
               ;

additive : additive (ADD_OPT | SUB_OPT) multiplicative
         | multiplicative
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

rule_statement : RULE IDENTIFIER OPEN_PAR expression CLOSE_PAR
               ;

piece_statement : PIECE (IDENTIFIER | object_access | ALL | OPEN_PAR param_list CLOSE_PAR) COUNT int_literal 
                | PIECE (IDENTIFIER | object_access | ALL | OPEN_PAR param_list CLOSE_PAR) ACTION IDENTIFIER OPEN_PAR param_list CLOSE_PAR (COMMA IDENTIFIER OPEN_PAR param_list CLOSE_PAR)*
                | PIECE (IDENTIFIER | object_access | ALL | OPEN_PAR param_list CLOSE_PAR | ANY | NONE) ACTION IDENTIFIER OPEN_PAR expression CLOSE_PAR (COMMA IDENTIFIER OPEN_PAR expression CLOSE_PAR)*
                | PIECE assignment_expression
                ;

board_statement : (PLAYER IDENTIFIER)* PIECE (IDENTIFIER | object_access | ALL) SETUP OPEN_PAR (param_list | board_pos) CLOSE_PAR
                | (PLAYER IDENTIFIER)* OBSTACLE (IDENTIFIER | object_access | ALL) SETUP OPEN_PAR (param_list | board_pos) CLOSE_PAR
                | (PLAYER IDENTIFIER)* BOOSTER (IDENTIFIER | object_access | ALL) SETUP OPEN_PAR (param_list | board_pos) CLOSE_PAR
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

if_statement : IF expression COLON code_block  ELSE COLON code_block
             | IF expression COLON code_block
             ;

for_statement : FOR IDENTIFIER IN list COLON code_block END
              ;

while_statement : WHILE expression COLON code_block END
                ;

input_statement : INPUT OPEN_PAR STRING_LITERAL* CLOSE_PAR
                ;

print_statement : PRINT OPEN_PAR (param_list) CLOSE_PAR
                ;

return_statement : RETURN expression
                 ;

timer_statement : TIMER OPEN_PAR POSITIVE_INT_LITERAL CLOSE_PAR //i set this as positive_int_literal since timer cannot be negative
                ;

dice_statement  : DICE OPEN_PAR int_literal COMMA int_literal CLOSE_PAR //i imagine it as DICE(1,6) where it rolls the possible numbers
                ; //currently its set as this in case of games that allow negative numbers since some games allow those type of dice rolls

