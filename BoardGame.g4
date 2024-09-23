/*
Grammar defining a Board Game Language
*/

grammar BoardGame;

GAME : 'GAME' ID; // match keyword game
PLAYERS : 'PLAYERS' INT; // match keyword players
PIECES : 'PIECES' __________; // match keyword pieces
PIECE : 'PIECE' ID; // match keyword piece
BOARD : 'BOARD' INT INT; // match keyword board
TURN : 'TURN' __________; // match keyword turn

OBSTACLES : 'OBSTACLES' ('none' | INT); // match keyword obstacles
BOOSTERS : 'BOOSTERS' ('none' | INT); // match keyword boosters

COUNT : 'COUNT' INT; // match keyword count
ACTION : 'ACTION' ___________; // match keyword action
SETUP : 'SETUP' ___________; // match keyword setup

MOVE : 'MOVE' ___________; // match keyword move
TO : 'TO' ___________; // match keyword to

START : 'START' ___________; // match keyword start
END : 'END' ___________; // match keyword end

ID : [a-zA-Z][a-zA-Z0-9_]*; // match identifiers
INT : '0' | [1-9] [0-9]*; // match integers