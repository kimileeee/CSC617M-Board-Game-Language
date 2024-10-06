parser grammar BoardGameParser;
options {
    tokenVocab=BoardGameLexer;
}

program : GAME IDENTIFIER define_block+ gameplay_block
        ;

define_block : DEFINE IDENTIFIER COLON code_block END
             | DEFINE IDENTIFIER DOT IDENTIFIER COLON code_block END
             ;

gameplay_block : START COLON code_block END
               ;

code_block  : statement code_block
            | statement
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
            ;

game_entities : BOARD
              | PLAYERS
              | CONDITIONS
              | RULES
              | PIECES
              | OBSTACLES
              | BOOSTERS
              ;

literal : INT_LITERAL
        | FLOAT_LITERAL
        | STRING_LITERAL
        | BOOLEAN_LITERAL
        ;

literal_list : literal COMMA literal_list
             | literal
             ;

list_literal : OPEN_PAR literal_list CLOSE_PAR
             ;

param_list  : IDENTIFIER COMMA param_list
            | IDENTIFIER
            | NONE
            | ANY
            | ALL
            | literal COMMA param_list
            | literal
            ;

board_pos : BOARD DOT ROW DOT INT_LITERAL
          | BOARD DOT COLUMN DOT INT_LITERAL
          | BOARD DOT IDENTIFIER
          ;

conditional  : AND_OPT
             | OR_OPT
             | NOT_OPT
             | EQUAL_OPT
             | LESS_THAN_OPT
             | LESS_EQUAL_OPT
             | GREATER_THAN_OPT
             | GREATER_EQUAL_OPT
             ;

expression : IDENTIFIER
           | literal
           | IDENTIFIER DOT IDENTIFIER
           | expression ADD_OPT expression
           | expression SUB_OPT expression
           | expression MUL_OPT expression
           | expression DIV_OPT expression
           ;

conditional_expression : expression conditional conditional_expression
                       | expression
                       ;

game_entities_statement : game_entities OPEN_PAR param_list CLOSE_PAR
                        ;

player_statement : PLAYER IDENTIFIER COLOR IDENTIFIER AT board_pos
                 | ORDER OPEN_PAR list_literal CLOSE_PAR
                 ;

condition_statement : CONDITION OPEN_PAR conditional_expression CLOSE_PAR
                    ;

rule_statement : RULE IDENTIFIER OPEN_PAR conditional_expression CLOSE_PAR
               ;

piece_statement : PIECE IDENTIFIER COUNT INT_LITERAL 
                | PIECE IDENTIFIER ACTION IDENTIFIER OPEN_PAR param_list CLOSE_PAR
                ;

board_statement : PIECE IDENTIFIER SETUP OPEN_PAR (param_list | board_pos) CLOSE_PAR
                | OBSTACLE IDENTIFIER SETUP OPEN_PAR (param_list | board_pos) CLOSE_PAR
                | BOOSTER IDENTIFIER SETUP OPEN_PAR (param_list | board_pos) CLOSE_PAR
                ;

obstacle_statement : OBSTACLE IDENTIFIER COUNT INT_LITERAL
                   | OBSTACLE IDENTIFIER ACTION IDENTIFIER OPEN_PAR param_list CLOSE_PAR
                   ;

booster_statement : BOOSTER IDENTIFIER COUNT INT_LITERAL
                  | BOOSTER IDENTIFIER ACTION IDENTIFIER OPEN_PAR param_list CLOSE_PAR
                  ;

move_statement : MOVE IDENTIFIER TO board_pos
               ;

turn_statement : TURN IDENTIFIER move_statement
               ;