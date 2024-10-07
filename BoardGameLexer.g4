/*
Grammar defining a Board Game Language
*/

lexer grammar BoardGameLexer;

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
AT : 'AT';
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

ALL : 'ALL';
ANY : 'ANY';
NONE : 'NONE';
// NEWLINE : '\r'? '\n';

IF : 'IF';
ELSE : 'ELSE';
FOR : 'FOR';
WHILE : 'WHILE';
INPUT : 'INPUT';
PRINT : 'PRINT';
RETURN : 'RETURN';
IN : 'IN';
BREAK : 'BREAK';
ERROR : 'ERROR';

// Operators
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

// Literals
INT_LITERAL : [0-9]+;
FLOAT_LITERAL : [0-9]+ '.' [0-9]+;
STRING_LITERAL : '"' (~["])* '"';
BOOLEAN_LITERAL : 'true' | 'false';

// Identifiers
IDENTIFIER : [a-zA-Z][a-zA-Z0-9_]*('.'[a-zA-Z][a-zA-Z0-9_]*)*;

// Comments
COMMENT : '//' ~[\r\n]* -> skip;

// Whitespace
WS : [ \t\r\n]+ -> skip;

