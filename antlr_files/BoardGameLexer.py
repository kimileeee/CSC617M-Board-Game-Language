# Generated from BoardGameLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,77,569,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,
        1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,
        1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,
        1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,
        1,31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,34,
        1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,
        1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,
        1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,44,1,44,
        1,44,1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,48,1,48,
        1,49,1,49,1,50,1,50,1,50,1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,54,
        1,54,1,55,1,55,1,56,1,56,1,57,1,57,1,58,1,58,1,59,1,59,1,60,1,60,
        1,61,1,61,1,62,1,62,1,63,1,63,1,64,1,64,1,65,1,65,1,66,1,66,1,67,
        1,67,1,67,1,67,1,68,1,68,1,69,4,69,489,8,69,11,69,12,69,490,1,70,
        3,70,494,8,70,1,70,1,70,1,71,1,71,1,72,1,72,1,72,1,73,1,73,1,73,
        1,73,1,74,1,74,5,74,509,8,74,10,74,12,74,512,9,74,1,74,1,74,1,75,
        1,75,1,75,1,75,1,75,1,75,1,75,1,75,1,75,3,75,525,8,75,1,76,1,76,
        5,76,529,8,76,10,76,12,76,532,9,76,1,77,1,77,1,77,1,77,5,77,538,
        8,77,10,77,12,77,541,9,77,1,77,1,77,1,78,1,78,1,79,4,79,548,8,79,
        11,79,12,79,549,1,79,1,79,1,80,1,80,1,80,1,80,1,80,3,80,559,8,80,
        1,80,1,80,5,80,563,8,80,10,80,12,80,566,9,80,1,80,1,80,0,0,81,1,
        1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,
        14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,
        25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,
        36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,
        47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,56,113,
        57,115,58,117,59,119,60,121,61,123,62,125,63,127,64,129,65,131,66,
        133,67,135,68,137,0,139,0,141,0,143,69,145,70,147,71,149,72,151,
        73,153,74,155,75,157,0,159,76,161,77,1,0,7,1,0,48,57,1,0,34,34,2,
        0,65,90,97,122,4,0,48,57,65,90,95,95,97,122,2,0,10,10,13,13,3,0,
        9,10,13,13,32,32,3,0,65,90,95,95,97,122,576,0,1,1,0,0,0,0,3,1,0,
        0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,
        0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,
        0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,
        0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,
        0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,
        0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,
        0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,
        0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,
        0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,
        0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,
        0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,
        1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,
        0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,
        0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,
        147,1,0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,0,153,1,0,0,0,0,155,1,0,
        0,0,0,159,1,0,0,0,0,161,1,0,0,0,1,163,1,0,0,0,3,168,1,0,0,0,5,175,
        1,0,0,0,7,181,1,0,0,0,9,189,1,0,0,0,11,200,1,0,0,0,13,206,1,0,0,
        0,15,212,1,0,0,0,17,217,1,0,0,0,19,223,1,0,0,0,21,230,1,0,0,0,23,
        240,1,0,0,0,25,249,1,0,0,0,27,256,1,0,0,0,29,262,1,0,0,0,31,268,
        1,0,0,0,33,278,1,0,0,0,35,283,1,0,0,0,37,289,1,0,0,0,39,295,1,0,
        0,0,41,302,1,0,0,0,43,308,1,0,0,0,45,317,1,0,0,0,47,325,1,0,0,0,
        49,331,1,0,0,0,51,335,1,0,0,0,53,340,1,0,0,0,55,343,1,0,0,0,57,348,
        1,0,0,0,59,352,1,0,0,0,61,359,1,0,0,0,63,362,1,0,0,0,65,367,1,0,
        0,0,67,371,1,0,0,0,69,377,1,0,0,0,71,383,1,0,0,0,73,389,1,0,0,0,
        75,396,1,0,0,0,77,402,1,0,0,0,79,408,1,0,0,0,81,412,1,0,0,0,83,416,
        1,0,0,0,85,421,1,0,0,0,87,424,1,0,0,0,89,427,1,0,0,0,91,431,1,0,
        0,0,93,434,1,0,0,0,95,438,1,0,0,0,97,441,1,0,0,0,99,443,1,0,0,0,
        101,445,1,0,0,0,103,448,1,0,0,0,105,450,1,0,0,0,107,453,1,0,0,0,
        109,455,1,0,0,0,111,457,1,0,0,0,113,459,1,0,0,0,115,461,1,0,0,0,
        117,463,1,0,0,0,119,465,1,0,0,0,121,467,1,0,0,0,123,469,1,0,0,0,
        125,471,1,0,0,0,127,473,1,0,0,0,129,475,1,0,0,0,131,477,1,0,0,0,
        133,479,1,0,0,0,135,481,1,0,0,0,137,485,1,0,0,0,139,488,1,0,0,0,
        141,493,1,0,0,0,143,497,1,0,0,0,145,499,1,0,0,0,147,502,1,0,0,0,
        149,506,1,0,0,0,151,524,1,0,0,0,153,526,1,0,0,0,155,533,1,0,0,0,
        157,544,1,0,0,0,159,547,1,0,0,0,161,558,1,0,0,0,163,164,5,71,0,0,
        164,165,5,65,0,0,165,166,5,77,0,0,166,167,5,69,0,0,167,2,1,0,0,0,
        168,169,5,68,0,0,169,170,5,69,0,0,170,171,5,70,0,0,171,172,5,73,
        0,0,172,173,5,78,0,0,173,174,5,69,0,0,174,4,1,0,0,0,175,176,5,66,
        0,0,176,177,5,79,0,0,177,178,5,65,0,0,178,179,5,82,0,0,179,180,5,
        68,0,0,180,6,1,0,0,0,181,182,5,80,0,0,182,183,5,76,0,0,183,184,5,
        65,0,0,184,185,5,89,0,0,185,186,5,69,0,0,186,187,5,82,0,0,187,188,
        5,83,0,0,188,8,1,0,0,0,189,190,5,67,0,0,190,191,5,79,0,0,191,192,
        5,78,0,0,192,193,5,68,0,0,193,194,5,73,0,0,194,195,5,84,0,0,195,
        196,5,73,0,0,196,197,5,79,0,0,197,198,5,78,0,0,198,199,5,83,0,0,
        199,10,1,0,0,0,200,201,5,84,0,0,201,202,5,73,0,0,202,203,5,77,0,
        0,203,204,5,69,0,0,204,205,5,82,0,0,205,12,1,0,0,0,206,207,5,83,
        0,0,207,208,5,67,0,0,208,209,5,79,0,0,209,210,5,82,0,0,210,211,5,
        69,0,0,211,14,1,0,0,0,212,213,5,68,0,0,213,214,5,73,0,0,214,215,
        5,67,0,0,215,216,5,69,0,0,216,16,1,0,0,0,217,218,5,82,0,0,218,219,
        5,85,0,0,219,220,5,76,0,0,220,221,5,69,0,0,221,222,5,83,0,0,222,
        18,1,0,0,0,223,224,5,80,0,0,224,225,5,73,0,0,225,226,5,69,0,0,226,
        227,5,67,0,0,227,228,5,69,0,0,228,229,5,83,0,0,229,20,1,0,0,0,230,
        231,5,79,0,0,231,232,5,66,0,0,232,233,5,83,0,0,233,234,5,84,0,0,
        234,235,5,65,0,0,235,236,5,67,0,0,236,237,5,76,0,0,237,238,5,69,
        0,0,238,239,5,83,0,0,239,22,1,0,0,0,240,241,5,66,0,0,241,242,5,79,
        0,0,242,243,5,79,0,0,243,244,5,83,0,0,244,245,5,84,0,0,245,246,5,
        69,0,0,246,247,5,82,0,0,247,248,5,83,0,0,248,24,1,0,0,0,249,250,
        5,80,0,0,250,251,5,76,0,0,251,252,5,65,0,0,252,253,5,89,0,0,253,
        254,5,69,0,0,254,255,5,82,0,0,255,26,1,0,0,0,256,257,5,67,0,0,257,
        258,5,79,0,0,258,259,5,76,0,0,259,260,5,79,0,0,260,261,5,82,0,0,
        261,28,1,0,0,0,262,263,5,79,0,0,263,264,5,82,0,0,264,265,5,68,0,
        0,265,266,5,69,0,0,266,267,5,82,0,0,267,30,1,0,0,0,268,269,5,67,
        0,0,269,270,5,79,0,0,270,271,5,78,0,0,271,272,5,68,0,0,272,273,5,
        73,0,0,273,274,5,84,0,0,274,275,5,73,0,0,275,276,5,79,0,0,276,277,
        5,78,0,0,277,32,1,0,0,0,278,279,5,82,0,0,279,280,5,85,0,0,280,281,
        5,76,0,0,281,282,5,69,0,0,282,34,1,0,0,0,283,284,5,80,0,0,284,285,
        5,73,0,0,285,286,5,69,0,0,286,287,5,67,0,0,287,288,5,69,0,0,288,
        36,1,0,0,0,289,290,5,67,0,0,290,291,5,79,0,0,291,292,5,85,0,0,292,
        293,5,78,0,0,293,294,5,84,0,0,294,38,1,0,0,0,295,296,5,65,0,0,296,
        297,5,67,0,0,297,298,5,84,0,0,298,299,5,73,0,0,299,300,5,79,0,0,
        300,301,5,78,0,0,301,40,1,0,0,0,302,303,5,83,0,0,303,304,5,69,0,
        0,304,305,5,84,0,0,305,306,5,85,0,0,306,307,5,80,0,0,307,42,1,0,
        0,0,308,309,5,79,0,0,309,310,5,66,0,0,310,311,5,83,0,0,311,312,5,
        84,0,0,312,313,5,65,0,0,313,314,5,67,0,0,314,315,5,76,0,0,315,316,
        5,69,0,0,316,44,1,0,0,0,317,318,5,66,0,0,318,319,5,79,0,0,319,320,
        5,79,0,0,320,321,5,83,0,0,321,322,5,84,0,0,322,323,5,69,0,0,323,
        324,5,82,0,0,324,46,1,0,0,0,325,326,5,83,0,0,326,327,5,84,0,0,327,
        328,5,65,0,0,328,329,5,82,0,0,329,330,5,84,0,0,330,48,1,0,0,0,331,
        332,5,69,0,0,332,333,5,78,0,0,333,334,5,68,0,0,334,50,1,0,0,0,335,
        336,5,77,0,0,336,337,5,79,0,0,337,338,5,86,0,0,338,339,5,69,0,0,
        339,52,1,0,0,0,340,341,5,84,0,0,341,342,5,79,0,0,342,54,1,0,0,0,
        343,344,5,84,0,0,344,345,5,85,0,0,345,346,5,82,0,0,346,347,5,78,
        0,0,347,56,1,0,0,0,348,349,5,82,0,0,349,350,5,79,0,0,350,351,5,87,
        0,0,351,58,1,0,0,0,352,353,5,67,0,0,353,354,5,79,0,0,354,355,5,76,
        0,0,355,356,5,85,0,0,356,357,5,77,0,0,357,358,5,78,0,0,358,60,1,
        0,0,0,359,360,5,73,0,0,360,361,5,70,0,0,361,62,1,0,0,0,362,363,5,
        69,0,0,363,364,5,76,0,0,364,365,5,83,0,0,365,366,5,69,0,0,366,64,
        1,0,0,0,367,368,5,70,0,0,368,369,5,79,0,0,369,370,5,82,0,0,370,66,
        1,0,0,0,371,372,5,87,0,0,372,373,5,72,0,0,373,374,5,73,0,0,374,375,
        5,76,0,0,375,376,5,69,0,0,376,68,1,0,0,0,377,378,5,73,0,0,378,379,
        5,78,0,0,379,380,5,80,0,0,380,381,5,85,0,0,381,382,5,84,0,0,382,
        70,1,0,0,0,383,384,5,80,0,0,384,385,5,82,0,0,385,386,5,73,0,0,386,
        387,5,78,0,0,387,388,5,84,0,0,388,72,1,0,0,0,389,390,5,82,0,0,390,
        391,5,69,0,0,391,392,5,84,0,0,392,393,5,85,0,0,393,394,5,82,0,0,
        394,395,5,78,0,0,395,74,1,0,0,0,396,397,5,66,0,0,397,398,5,82,0,
        0,398,399,5,69,0,0,399,400,5,65,0,0,400,401,5,75,0,0,401,76,1,0,
        0,0,402,403,5,69,0,0,403,404,5,82,0,0,404,405,5,82,0,0,405,406,5,
        79,0,0,406,407,5,82,0,0,407,78,1,0,0,0,408,409,5,65,0,0,409,410,
        5,76,0,0,410,411,5,76,0,0,411,80,1,0,0,0,412,413,5,65,0,0,413,414,
        5,78,0,0,414,415,5,89,0,0,415,82,1,0,0,0,416,417,5,78,0,0,417,418,
        5,79,0,0,418,419,5,78,0,0,419,420,5,69,0,0,420,84,1,0,0,0,421,422,
        5,73,0,0,422,423,5,78,0,0,423,86,1,0,0,0,424,425,5,65,0,0,425,426,
        5,84,0,0,426,88,1,0,0,0,427,428,5,65,0,0,428,429,5,78,0,0,429,430,
        5,68,0,0,430,90,1,0,0,0,431,432,5,79,0,0,432,433,5,82,0,0,433,92,
        1,0,0,0,434,435,5,78,0,0,435,436,5,79,0,0,436,437,5,84,0,0,437,94,
        1,0,0,0,438,439,5,61,0,0,439,440,5,61,0,0,440,96,1,0,0,0,441,442,
        5,61,0,0,442,98,1,0,0,0,443,444,5,60,0,0,444,100,1,0,0,0,445,446,
        5,60,0,0,446,447,5,61,0,0,447,102,1,0,0,0,448,449,5,62,0,0,449,104,
        1,0,0,0,450,451,5,62,0,0,451,452,5,61,0,0,452,106,1,0,0,0,453,454,
        5,43,0,0,454,108,1,0,0,0,455,456,5,45,0,0,456,110,1,0,0,0,457,458,
        5,42,0,0,458,112,1,0,0,0,459,460,5,47,0,0,460,114,1,0,0,0,461,462,
        5,94,0,0,462,116,1,0,0,0,463,464,5,58,0,0,464,118,1,0,0,0,465,466,
        5,46,0,0,466,120,1,0,0,0,467,468,5,44,0,0,468,122,1,0,0,0,469,470,
        5,40,0,0,470,124,1,0,0,0,471,472,5,41,0,0,472,126,1,0,0,0,473,474,
        5,91,0,0,474,128,1,0,0,0,475,476,5,93,0,0,476,130,1,0,0,0,477,478,
        5,123,0,0,478,132,1,0,0,0,479,480,5,125,0,0,480,134,1,0,0,0,481,
        482,5,46,0,0,482,483,5,46,0,0,483,484,5,46,0,0,484,136,1,0,0,0,485,
        486,7,0,0,0,486,138,1,0,0,0,487,489,3,137,68,0,488,487,1,0,0,0,489,
        490,1,0,0,0,490,488,1,0,0,0,490,491,1,0,0,0,491,140,1,0,0,0,492,
        494,5,45,0,0,493,492,1,0,0,0,493,494,1,0,0,0,494,495,1,0,0,0,495,
        496,3,139,69,0,496,142,1,0,0,0,497,498,3,139,69,0,498,144,1,0,0,
        0,499,500,5,45,0,0,500,501,3,139,69,0,501,146,1,0,0,0,502,503,3,
        141,70,0,503,504,5,46,0,0,504,505,3,139,69,0,505,148,1,0,0,0,506,
        510,5,34,0,0,507,509,8,1,0,0,508,507,1,0,0,0,509,512,1,0,0,0,510,
        508,1,0,0,0,510,511,1,0,0,0,511,513,1,0,0,0,512,510,1,0,0,0,513,
        514,5,34,0,0,514,150,1,0,0,0,515,516,5,116,0,0,516,517,5,114,0,0,
        517,518,5,117,0,0,518,525,5,101,0,0,519,520,5,102,0,0,520,521,5,
        97,0,0,521,522,5,108,0,0,522,523,5,115,0,0,523,525,5,101,0,0,524,
        515,1,0,0,0,524,519,1,0,0,0,525,152,1,0,0,0,526,530,7,2,0,0,527,
        529,7,3,0,0,528,527,1,0,0,0,529,532,1,0,0,0,530,528,1,0,0,0,530,
        531,1,0,0,0,531,154,1,0,0,0,532,530,1,0,0,0,533,534,5,47,0,0,534,
        535,5,47,0,0,535,539,1,0,0,0,536,538,8,4,0,0,537,536,1,0,0,0,538,
        541,1,0,0,0,539,537,1,0,0,0,539,540,1,0,0,0,540,542,1,0,0,0,541,
        539,1,0,0,0,542,543,6,77,0,0,543,156,1,0,0,0,544,545,5,32,0,0,545,
        158,1,0,0,0,546,548,7,5,0,0,547,546,1,0,0,0,548,549,1,0,0,0,549,
        547,1,0,0,0,549,550,1,0,0,0,550,551,1,0,0,0,551,552,6,79,1,0,552,
        160,1,0,0,0,553,559,3,143,71,0,554,559,3,145,72,0,555,559,3,149,
        74,0,556,559,3,147,73,0,557,559,3,117,58,0,558,553,1,0,0,0,558,554,
        1,0,0,0,558,555,1,0,0,0,558,556,1,0,0,0,558,557,1,0,0,0,559,560,
        1,0,0,0,560,564,7,6,0,0,561,563,7,3,0,0,562,561,1,0,0,0,563,566,
        1,0,0,0,564,562,1,0,0,0,564,565,1,0,0,0,565,567,1,0,0,0,566,564,
        1,0,0,0,567,568,6,80,2,0,568,162,1,0,0,0,10,0,490,493,510,524,530,
        539,549,558,564,3,0,2,0,0,1,0,0,3,0
    ]

class BoardGameLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENTS = 2
    ERRORS = 3

    GAME = 1
    DEFINE = 2
    BOARD = 3
    PLAYERS = 4
    CONDITIONS = 5
    TIMER = 6
    SCORE = 7
    DICE = 8
    RULES = 9
    PIECES = 10
    OBSTACLES = 11
    BOOSTERS = 12
    PLAYER = 13
    COLOR = 14
    ORDER = 15
    CONDITION = 16
    RULE = 17
    PIECE = 18
    COUNT = 19
    ACTION = 20
    SETUP = 21
    OBSTACLE = 22
    BOOSTER = 23
    START = 24
    END = 25
    MOVE = 26
    TO = 27
    TURN = 28
    ROW = 29
    COLUMN = 30
    IF = 31
    ELSE = 32
    FOR = 33
    WHILE = 34
    INPUT = 35
    PRINT = 36
    RETURN = 37
    BREAK = 38
    ERROR = 39
    ALL = 40
    ANY = 41
    NONE = 42
    IN = 43
    AT = 44
    AND_OPT = 45
    OR_OPT = 46
    NOT_OPT = 47
    EQUAL_OPT = 48
    ASSIGN_OPT = 49
    LESS_THAN_OPT = 50
    LESS_EQUAL_OPT = 51
    GREATER_THAN_OPT = 52
    GREATER_EQUAL_OPT = 53
    ADD_OPT = 54
    SUB_OPT = 55
    MUL_OPT = 56
    DIV_OPT = 57
    EXP_OPT = 58
    COLON = 59
    DOT = 60
    COMMA = 61
    OPEN_PAR = 62
    CLOSE_PAR = 63
    OPEN_BRACKET = 64
    CLOSE_BRACKET = 65
    OPEN_BRACE = 66
    CLOSE_BRACE = 67
    ELIPSIS = 68
    POSITIVE_INT_LITERAL = 69
    NEGATIVE_INT_LITERAL = 70
    FLOAT_LITERAL = 71
    STRING_LITERAL = 72
    BOOLEAN_LITERAL = 73
    IDENTIFIER = 74
    COMMENT = 75
    WS = 76
    INVALID_IDENTIFIER = 77

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"COMMENTS", u"ERRORS" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'GAME'", "'DEFINE'", "'BOARD'", "'PLAYERS'", "'CONDITIONS'", 
            "'TIMER'", "'SCORE'", "'DICE'", "'RULES'", "'PIECES'", "'OBSTACLES'", 
            "'BOOSTERS'", "'PLAYER'", "'COLOR'", "'ORDER'", "'CONDITION'", 
            "'RULE'", "'PIECE'", "'COUNT'", "'ACTION'", "'SETUP'", "'OBSTACLE'", 
            "'BOOSTER'", "'START'", "'END'", "'MOVE'", "'TO'", "'TURN'", 
            "'ROW'", "'COLUMN'", "'IF'", "'ELSE'", "'FOR'", "'WHILE'", "'INPUT'", 
            "'PRINT'", "'RETURN'", "'BREAK'", "'ERROR'", "'ALL'", "'ANY'", 
            "'NONE'", "'IN'", "'AT'", "'AND'", "'OR'", "'NOT'", "'=='", 
            "'='", "'<'", "'<='", "'>'", "'>='", "'+'", "'-'", "'*'", "'/'", 
            "'^'", "':'", "'.'", "','", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "'...'" ]

    symbolicNames = [ "<INVALID>",
            "GAME", "DEFINE", "BOARD", "PLAYERS", "CONDITIONS", "TIMER", 
            "SCORE", "DICE", "RULES", "PIECES", "OBSTACLES", "BOOSTERS", 
            "PLAYER", "COLOR", "ORDER", "CONDITION", "RULE", "PIECE", "COUNT", 
            "ACTION", "SETUP", "OBSTACLE", "BOOSTER", "START", "END", "MOVE", 
            "TO", "TURN", "ROW", "COLUMN", "IF", "ELSE", "FOR", "WHILE", 
            "INPUT", "PRINT", "RETURN", "BREAK", "ERROR", "ALL", "ANY", 
            "NONE", "IN", "AT", "AND_OPT", "OR_OPT", "NOT_OPT", "EQUAL_OPT", 
            "ASSIGN_OPT", "LESS_THAN_OPT", "LESS_EQUAL_OPT", "GREATER_THAN_OPT", 
            "GREATER_EQUAL_OPT", "ADD_OPT", "SUB_OPT", "MUL_OPT", "DIV_OPT", 
            "EXP_OPT", "COLON", "DOT", "COMMA", "OPEN_PAR", "CLOSE_PAR", 
            "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
            "ELIPSIS", "POSITIVE_INT_LITERAL", "NEGATIVE_INT_LITERAL", "FLOAT_LITERAL", 
            "STRING_LITERAL", "BOOLEAN_LITERAL", "IDENTIFIER", "COMMENT", 
            "WS", "INVALID_IDENTIFIER" ]

    ruleNames = [ "GAME", "DEFINE", "BOARD", "PLAYERS", "CONDITIONS", "TIMER", 
                  "SCORE", "DICE", "RULES", "PIECES", "OBSTACLES", "BOOSTERS", 
                  "PLAYER", "COLOR", "ORDER", "CONDITION", "RULE", "PIECE", 
                  "COUNT", "ACTION", "SETUP", "OBSTACLE", "BOOSTER", "START", 
                  "END", "MOVE", "TO", "TURN", "ROW", "COLUMN", "IF", "ELSE", 
                  "FOR", "WHILE", "INPUT", "PRINT", "RETURN", "BREAK", "ERROR", 
                  "ALL", "ANY", "NONE", "IN", "AT", "AND_OPT", "OR_OPT", 
                  "NOT_OPT", "EQUAL_OPT", "ASSIGN_OPT", "LESS_THAN_OPT", 
                  "LESS_EQUAL_OPT", "GREATER_THAN_OPT", "GREATER_EQUAL_OPT", 
                  "ADD_OPT", "SUB_OPT", "MUL_OPT", "DIV_OPT", "EXP_OPT", 
                  "COLON", "DOT", "COMMA", "OPEN_PAR", "CLOSE_PAR", "OPEN_BRACKET", 
                  "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", "ELIPSIS", 
                  "DIGIT", "NUMBER", "INTEGER", "POSITIVE_INT_LITERAL", 
                  "NEGATIVE_INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                  "BOOLEAN_LITERAL", "IDENTIFIER", "COMMENT", "SPACE", "WS", 
                  "INVALID_IDENTIFIER" ]

    grammarFileName = "BoardGameLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


