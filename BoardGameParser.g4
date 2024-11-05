parser grammar BoardGameParser;
options {
    tokenVocab=BoardGameLexer;
}

program : GAME IDENTIFIER define_block+ gameplay_block
        ;

define_block : DEFINE (IDENTIFIER | object_access) COLON code_block END
             ;

gameplay_block : START COLON code_block END
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

literal : int_literal
        | FLOAT_LITERAL
        | STRING_LITERAL
        | BOOLEAN_LITERAL
        ;

primary : literal
        | object_access
        | list
        | IDENTIFIER
        | OPEN_PAR expression CLOSE_PAR
        | method_call
        ;

param_list      : SCORE OPEN_PAR IDENTIFIER DOT CONDITIONS CLOSE_PAR
                | ALL (COMMA param_list)*
                | ANY (COMMA param_list)*
                | NONE (COMMA param_list)*
                | IDENTIFIER ASSIGN_OPT literal (COMMA param_list)* //in what situations would a literal have 0 comma param list extra after it?
                | IDENTIFIER ASSIGN_OPT objects (COMMA param_list)*
                | IDENTIFIER (COMMA param_list)*
                | literal (COMMA param_list)* //removes redundancy of literal COMMA param_list and literal
                | object_access (COMMA param_list)*
                | list (COMMA param_list)*
                ;

list : OPEN_BRACKET param_list CLOSE_BRACKET
     ;

object_access : IDENTIFIER DOT game_entities (DOT game_entities | IDENTIFIER)* //do we allow something like BOARD.PIECES.OBSTACLES??
              | game_entities DOT IDENTIFIER (DOT game_entities | IDENTIFIER)* //should it be DOT identifier 
              | IDENTIFIER DOT IDENTIFIER (DOT game_entities | IDENTIFIER)*
              ;
        

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

expression : assignment_expression (logical_opt expression)*
           | math_expression (logical_opt expression)*
           | in_expression (logical_opt expression)*
           | at_expression (logical_opt expression)*
           | any_expression expression (logical_opt expression)*
           | primary (logical_opt expression)*
           | NOT_OPT expression (logical_opt expression)*
           | conditional_expression (logical_opt expression)*
           | move_statement (logical_opt expression)*
           ;

objects : IDENTIFIER
        | object_access
        | board_pos
        ;

method_call : objects DOT IDENTIFIER OPEN_PAR param_list* CLOSE_PAR
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

