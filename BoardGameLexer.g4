/*
Grammar defining a Board Game Language
*/

lexer grammar BoardGameLexer;

channels {
	COMMENTS,
    ERRORS
}

// Keywords
GAME : 'GAME';
DEFINE : 'DEFINE';
BOARD : 'BOARD';
PLAYERS : 'PLAYERS';
CONDITIONS : 'CONDITIONS';
TIMER : 'TIMER';
SCORE : 'SCORE';
DICE : 'DICE';
RULES : 'RULES';
PIECES : 'PIECES';
OBSTACLES : 'OBSTACLES';
BOOSTERS : 'BOOSTERS';
PLAYER : 'PLAYER';
COLOR : 'COLOR';
ORDER : 'ORDER';
CONDITION : 'CONDITION';
RULE : 'RULE';
PIECE : 'PIECE';
COUNT : 'COUNT';
ACTION : 'ACTION';
SETUP : 'SETUP';
OBSTACLE : 'OBSTACLE';
BOOSTER : 'BOOSTER';
START : 'START';
END : 'END';
MOVE : 'MOVE';
TO : 'TO';
TURN : 'TURN';
ROW : 'ROW';
COLUMN : 'COLUMN';

IF : 'IF';
ELSE : 'ELSE';
FOR : 'FOR';
WHILE : 'WHILE';
INPUT : 'INPUT';
PRINT : 'PRINT';
RETURN : 'RETURN';
BREAK : 'BREAK';
ERROR : 'ERROR';

ALL : 'ALL';
ANY : 'ANY';
NONE : 'NONE';
// NEWLINE : '\r'? '\n';

// Operators
IN : 'IN';
AT : 'AT';
AND_OPT : 'AND';
OR_OPT : 'OR';
NOT_OPT : 'NOT';
EQUAL_OPT : '==';
ASSIGN_OPT : '=';
LESS_THAN_OPT : '<';
LESS_EQUAL_OPT : '<=';
GREATER_THAN_OPT : '>';
GREATER_EQUAL_OPT : '>=';
ADD_OPT : '+';
SUB_OPT : '-';
MUL_OPT : '*';
DIV_OPT : '/';

// Symbols
COLON : ':';
DOT : '.';
COMMA : ',';
OPEN_PAR : '(';
CLOSE_PAR : ')';
OPEN_BRACKET : '[';
CLOSE_BRACKET : ']';
OPEN_BRACE : '{';
CLOSE_BRACE : '}';
ELIPSIS : '...';

// Literals
fragment DIGIT : [0-9];
fragment NUMBER : DIGIT+;
fragment INTEGER : '-'? NUMBER;

//to handle the issue between the two a possible alternative would be to distinguish between positive and negative int literals?
INT_LITERAL : INTEGER;
POSITIVE_INT_LITERAL : NUMBER;
FLOAT_LITERAL : INTEGER '.' NUMBER;
STRING_LITERAL : '"' (~["])* '"';
BOOLEAN_LITERAL : 'true' | 'false';

// Identifiers
IDENTIFIER : [a-zA-Z][a-zA-Z0-9_]*;

// Comments
COMMENT : '//' ~[\r\n]* -> channel(COMMENTS);

// Whitespace
fragment SPACE : ' ';
WS : [ \t\r\n]+ -> channel(HIDDEN);

//checks for invalid inputs
INVALID_IDENTIFIER : ((INT_LITERAL | STRING_LITERAL | FLOAT_LITERAL) [a-zA-Z_][a-zA-Z0-9_]*) -> channel(ERRORS);

//how is the usage of special characters usually handled in a language?

