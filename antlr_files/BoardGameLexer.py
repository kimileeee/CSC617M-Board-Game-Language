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
        4,0,68,499,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,
        16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,
        21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,
        24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,
        27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,30,1,
        30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,
        33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,
        37,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,
        40,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,
        45,1,45,1,46,1,46,1,47,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,
        51,1,51,1,52,1,52,1,53,1,53,1,54,1,54,1,55,1,55,1,56,1,56,1,57,1,
        57,1,58,1,58,1,59,1,59,1,60,1,60,1,61,4,61,427,8,61,11,61,12,61,
        428,1,62,4,62,432,8,62,11,62,12,62,433,1,62,1,62,4,62,438,8,62,11,
        62,12,62,439,1,63,1,63,5,63,444,8,63,10,63,12,63,447,9,63,1,63,1,
        63,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,3,64,460,8,64,1,
        65,1,65,5,65,464,8,65,10,65,12,65,467,9,65,1,65,1,65,1,65,5,65,472,
        8,65,10,65,12,65,475,9,65,5,65,477,8,65,10,65,12,65,480,9,65,1,66,
        1,66,1,66,1,66,5,66,486,8,66,10,66,12,66,489,9,66,1,66,1,66,1,67,
        4,67,494,8,67,11,67,12,67,495,1,67,1,67,0,0,68,1,1,3,2,5,3,7,4,9,
        5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,
        33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,
        55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,
        77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,
        99,50,101,51,103,52,105,53,107,54,109,55,111,56,113,57,115,58,117,
        59,119,60,121,61,123,62,125,63,127,64,129,65,131,66,133,67,135,68,
        1,0,6,1,0,48,57,1,0,34,34,2,0,65,90,97,122,4,0,48,57,65,90,95,95,
        97,122,2,0,10,10,13,13,3,0,9,10,13,13,32,32,508,0,1,1,0,0,0,0,3,
        1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,
        0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,
        0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,
        0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,
        0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,
        0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,
        0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,
        0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,
        0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,
        0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,
        1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,
        0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,
        0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,
        131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,1,137,1,0,0,0,3,142,1,0,
        0,0,5,149,1,0,0,0,7,155,1,0,0,0,9,163,1,0,0,0,11,174,1,0,0,0,13,
        180,1,0,0,0,15,187,1,0,0,0,17,197,1,0,0,0,19,206,1,0,0,0,21,213,
        1,0,0,0,23,219,1,0,0,0,25,222,1,0,0,0,27,228,1,0,0,0,29,238,1,0,
        0,0,31,243,1,0,0,0,33,249,1,0,0,0,35,255,1,0,0,0,37,262,1,0,0,0,
        39,268,1,0,0,0,41,277,1,0,0,0,43,285,1,0,0,0,45,291,1,0,0,0,47,295,
        1,0,0,0,49,300,1,0,0,0,51,303,1,0,0,0,53,308,1,0,0,0,55,312,1,0,
        0,0,57,316,1,0,0,0,59,321,1,0,0,0,61,324,1,0,0,0,63,329,1,0,0,0,
        65,333,1,0,0,0,67,339,1,0,0,0,69,345,1,0,0,0,71,351,1,0,0,0,73,358,
        1,0,0,0,75,361,1,0,0,0,77,367,1,0,0,0,79,373,1,0,0,0,81,377,1,0,
        0,0,83,380,1,0,0,0,85,384,1,0,0,0,87,387,1,0,0,0,89,389,1,0,0,0,
        91,391,1,0,0,0,93,394,1,0,0,0,95,396,1,0,0,0,97,399,1,0,0,0,99,401,
        1,0,0,0,101,403,1,0,0,0,103,405,1,0,0,0,105,407,1,0,0,0,107,409,
        1,0,0,0,109,411,1,0,0,0,111,413,1,0,0,0,113,415,1,0,0,0,115,417,
        1,0,0,0,117,419,1,0,0,0,119,421,1,0,0,0,121,423,1,0,0,0,123,426,
        1,0,0,0,125,431,1,0,0,0,127,441,1,0,0,0,129,459,1,0,0,0,131,461,
        1,0,0,0,133,481,1,0,0,0,135,493,1,0,0,0,137,138,5,71,0,0,138,139,
        5,65,0,0,139,140,5,77,0,0,140,141,5,69,0,0,141,2,1,0,0,0,142,143,
        5,68,0,0,143,144,5,69,0,0,144,145,5,70,0,0,145,146,5,73,0,0,146,
        147,5,78,0,0,147,148,5,69,0,0,148,4,1,0,0,0,149,150,5,66,0,0,150,
        151,5,79,0,0,151,152,5,65,0,0,152,153,5,82,0,0,153,154,5,68,0,0,
        154,6,1,0,0,0,155,156,5,80,0,0,156,157,5,76,0,0,157,158,5,65,0,0,
        158,159,5,89,0,0,159,160,5,69,0,0,160,161,5,82,0,0,161,162,5,83,
        0,0,162,8,1,0,0,0,163,164,5,67,0,0,164,165,5,79,0,0,165,166,5,78,
        0,0,166,167,5,68,0,0,167,168,5,73,0,0,168,169,5,84,0,0,169,170,5,
        73,0,0,170,171,5,79,0,0,171,172,5,78,0,0,172,173,5,83,0,0,173,10,
        1,0,0,0,174,175,5,82,0,0,175,176,5,85,0,0,176,177,5,76,0,0,177,178,
        5,69,0,0,178,179,5,83,0,0,179,12,1,0,0,0,180,181,5,80,0,0,181,182,
        5,73,0,0,182,183,5,69,0,0,183,184,5,67,0,0,184,185,5,69,0,0,185,
        186,5,83,0,0,186,14,1,0,0,0,187,188,5,79,0,0,188,189,5,66,0,0,189,
        190,5,83,0,0,190,191,5,84,0,0,191,192,5,65,0,0,192,193,5,67,0,0,
        193,194,5,76,0,0,194,195,5,69,0,0,195,196,5,83,0,0,196,16,1,0,0,
        0,197,198,5,66,0,0,198,199,5,79,0,0,199,200,5,79,0,0,200,201,5,83,
        0,0,201,202,5,84,0,0,202,203,5,69,0,0,203,204,5,82,0,0,204,205,5,
        83,0,0,205,18,1,0,0,0,206,207,5,80,0,0,207,208,5,76,0,0,208,209,
        5,65,0,0,209,210,5,89,0,0,210,211,5,69,0,0,211,212,5,82,0,0,212,
        20,1,0,0,0,213,214,5,67,0,0,214,215,5,79,0,0,215,216,5,76,0,0,216,
        217,5,79,0,0,217,218,5,82,0,0,218,22,1,0,0,0,219,220,5,65,0,0,220,
        221,5,84,0,0,221,24,1,0,0,0,222,223,5,79,0,0,223,224,5,82,0,0,224,
        225,5,68,0,0,225,226,5,69,0,0,226,227,5,82,0,0,227,26,1,0,0,0,228,
        229,5,67,0,0,229,230,5,79,0,0,230,231,5,78,0,0,231,232,5,68,0,0,
        232,233,5,73,0,0,233,234,5,84,0,0,234,235,5,73,0,0,235,236,5,79,
        0,0,236,237,5,78,0,0,237,28,1,0,0,0,238,239,5,82,0,0,239,240,5,85,
        0,0,240,241,5,76,0,0,241,242,5,69,0,0,242,30,1,0,0,0,243,244,5,80,
        0,0,244,245,5,73,0,0,245,246,5,69,0,0,246,247,5,67,0,0,247,248,5,
        69,0,0,248,32,1,0,0,0,249,250,5,67,0,0,250,251,5,79,0,0,251,252,
        5,85,0,0,252,253,5,78,0,0,253,254,5,84,0,0,254,34,1,0,0,0,255,256,
        5,65,0,0,256,257,5,67,0,0,257,258,5,84,0,0,258,259,5,73,0,0,259,
        260,5,79,0,0,260,261,5,78,0,0,261,36,1,0,0,0,262,263,5,83,0,0,263,
        264,5,69,0,0,264,265,5,84,0,0,265,266,5,85,0,0,266,267,5,80,0,0,
        267,38,1,0,0,0,268,269,5,79,0,0,269,270,5,66,0,0,270,271,5,83,0,
        0,271,272,5,84,0,0,272,273,5,65,0,0,273,274,5,67,0,0,274,275,5,76,
        0,0,275,276,5,69,0,0,276,40,1,0,0,0,277,278,5,66,0,0,278,279,5,79,
        0,0,279,280,5,79,0,0,280,281,5,83,0,0,281,282,5,84,0,0,282,283,5,
        69,0,0,283,284,5,82,0,0,284,42,1,0,0,0,285,286,5,83,0,0,286,287,
        5,84,0,0,287,288,5,65,0,0,288,289,5,82,0,0,289,290,5,84,0,0,290,
        44,1,0,0,0,291,292,5,69,0,0,292,293,5,78,0,0,293,294,5,68,0,0,294,
        46,1,0,0,0,295,296,5,77,0,0,296,297,5,79,0,0,297,298,5,86,0,0,298,
        299,5,69,0,0,299,48,1,0,0,0,300,301,5,84,0,0,301,302,5,79,0,0,302,
        50,1,0,0,0,303,304,5,84,0,0,304,305,5,85,0,0,305,306,5,82,0,0,306,
        307,5,78,0,0,307,52,1,0,0,0,308,309,5,65,0,0,309,310,5,76,0,0,310,
        311,5,76,0,0,311,54,1,0,0,0,312,313,5,65,0,0,313,314,5,78,0,0,314,
        315,5,89,0,0,315,56,1,0,0,0,316,317,5,78,0,0,317,318,5,79,0,0,318,
        319,5,78,0,0,319,320,5,69,0,0,320,58,1,0,0,0,321,322,5,73,0,0,322,
        323,5,70,0,0,323,60,1,0,0,0,324,325,5,69,0,0,325,326,5,76,0,0,326,
        327,5,83,0,0,327,328,5,69,0,0,328,62,1,0,0,0,329,330,5,70,0,0,330,
        331,5,79,0,0,331,332,5,82,0,0,332,64,1,0,0,0,333,334,5,87,0,0,334,
        335,5,72,0,0,335,336,5,73,0,0,336,337,5,76,0,0,337,338,5,69,0,0,
        338,66,1,0,0,0,339,340,5,73,0,0,340,341,5,78,0,0,341,342,5,80,0,
        0,342,343,5,85,0,0,343,344,5,84,0,0,344,68,1,0,0,0,345,346,5,80,
        0,0,346,347,5,82,0,0,347,348,5,73,0,0,348,349,5,78,0,0,349,350,5,
        84,0,0,350,70,1,0,0,0,351,352,5,82,0,0,352,353,5,69,0,0,353,354,
        5,84,0,0,354,355,5,85,0,0,355,356,5,82,0,0,356,357,5,78,0,0,357,
        72,1,0,0,0,358,359,5,73,0,0,359,360,5,78,0,0,360,74,1,0,0,0,361,
        362,5,66,0,0,362,363,5,82,0,0,363,364,5,69,0,0,364,365,5,65,0,0,
        365,366,5,75,0,0,366,76,1,0,0,0,367,368,5,69,0,0,368,369,5,82,0,
        0,369,370,5,82,0,0,370,371,5,79,0,0,371,372,5,82,0,0,372,78,1,0,
        0,0,373,374,5,65,0,0,374,375,5,78,0,0,375,376,5,68,0,0,376,80,1,
        0,0,0,377,378,5,79,0,0,378,379,5,82,0,0,379,82,1,0,0,0,380,381,5,
        78,0,0,381,382,5,79,0,0,382,383,5,84,0,0,383,84,1,0,0,0,384,385,
        5,61,0,0,385,386,5,61,0,0,386,86,1,0,0,0,387,388,5,61,0,0,388,88,
        1,0,0,0,389,390,5,60,0,0,390,90,1,0,0,0,391,392,5,60,0,0,392,393,
        5,61,0,0,393,92,1,0,0,0,394,395,5,62,0,0,395,94,1,0,0,0,396,397,
        5,62,0,0,397,398,5,61,0,0,398,96,1,0,0,0,399,400,5,43,0,0,400,98,
        1,0,0,0,401,402,5,45,0,0,402,100,1,0,0,0,403,404,5,42,0,0,404,102,
        1,0,0,0,405,406,5,47,0,0,406,104,1,0,0,0,407,408,5,58,0,0,408,106,
        1,0,0,0,409,410,5,46,0,0,410,108,1,0,0,0,411,412,5,44,0,0,412,110,
        1,0,0,0,413,414,5,40,0,0,414,112,1,0,0,0,415,416,5,41,0,0,416,114,
        1,0,0,0,417,418,5,91,0,0,418,116,1,0,0,0,419,420,5,93,0,0,420,118,
        1,0,0,0,421,422,5,123,0,0,422,120,1,0,0,0,423,424,5,125,0,0,424,
        122,1,0,0,0,425,427,7,0,0,0,426,425,1,0,0,0,427,428,1,0,0,0,428,
        426,1,0,0,0,428,429,1,0,0,0,429,124,1,0,0,0,430,432,7,0,0,0,431,
        430,1,0,0,0,432,433,1,0,0,0,433,431,1,0,0,0,433,434,1,0,0,0,434,
        435,1,0,0,0,435,437,5,46,0,0,436,438,7,0,0,0,437,436,1,0,0,0,438,
        439,1,0,0,0,439,437,1,0,0,0,439,440,1,0,0,0,440,126,1,0,0,0,441,
        445,5,34,0,0,442,444,8,1,0,0,443,442,1,0,0,0,444,447,1,0,0,0,445,
        443,1,0,0,0,445,446,1,0,0,0,446,448,1,0,0,0,447,445,1,0,0,0,448,
        449,5,34,0,0,449,128,1,0,0,0,450,451,5,116,0,0,451,452,5,114,0,0,
        452,453,5,117,0,0,453,460,5,101,0,0,454,455,5,102,0,0,455,456,5,
        97,0,0,456,457,5,108,0,0,457,458,5,115,0,0,458,460,5,101,0,0,459,
        450,1,0,0,0,459,454,1,0,0,0,460,130,1,0,0,0,461,465,7,2,0,0,462,
        464,7,3,0,0,463,462,1,0,0,0,464,467,1,0,0,0,465,463,1,0,0,0,465,
        466,1,0,0,0,466,478,1,0,0,0,467,465,1,0,0,0,468,469,5,46,0,0,469,
        473,7,2,0,0,470,472,7,3,0,0,471,470,1,0,0,0,472,475,1,0,0,0,473,
        471,1,0,0,0,473,474,1,0,0,0,474,477,1,0,0,0,475,473,1,0,0,0,476,
        468,1,0,0,0,477,480,1,0,0,0,478,476,1,0,0,0,478,479,1,0,0,0,479,
        132,1,0,0,0,480,478,1,0,0,0,481,482,5,47,0,0,482,483,5,47,0,0,483,
        487,1,0,0,0,484,486,8,4,0,0,485,484,1,0,0,0,486,489,1,0,0,0,487,
        485,1,0,0,0,487,488,1,0,0,0,488,490,1,0,0,0,489,487,1,0,0,0,490,
        491,6,66,0,0,491,134,1,0,0,0,492,494,7,5,0,0,493,492,1,0,0,0,494,
        495,1,0,0,0,495,493,1,0,0,0,495,496,1,0,0,0,496,497,1,0,0,0,497,
        498,6,67,0,0,498,136,1,0,0,0,11,0,428,433,439,445,459,465,473,478,
        487,495,1,6,0,0
    ]

class BoardGameLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    GAME = 1
    DEFINE = 2
    BOARD = 3
    PLAYERS = 4
    CONDITIONS = 5
    RULES = 6
    PIECES = 7
    OBSTACLES = 8
    BOOSTERS = 9
    PLAYER = 10
    COLOR = 11
    AT = 12
    ORDER = 13
    CONDITION = 14
    RULE = 15
    PIECE = 16
    COUNT = 17
    ACTION = 18
    SETUP = 19
    OBSTACLE = 20
    BOOSTER = 21
    START = 22
    END = 23
    MOVE = 24
    TO = 25
    TURN = 26
    ALL = 27
    ANY = 28
    NONE = 29
    IF = 30
    ELSE = 31
    FOR = 32
    WHILE = 33
    INPUT = 34
    PRINT = 35
    RETURN = 36
    IN = 37
    BREAK = 38
    ERROR = 39
    AND_OPT = 40
    OR_OPT = 41
    NOT_OPT = 42
    EQUAL_OPT = 43
    ASSIGN_OPT = 44
    LESS_THAN_OPT = 45
    LESS_EQUAL_OPT = 46
    GREATER_THAN_OPT = 47
    GREATER_EQUAL_OPT = 48
    ADD_OPT = 49
    SUB_OPT = 50
    MUL_OPT = 51
    DIV_OPT = 52
    COLON = 53
    DOT = 54
    COMMA = 55
    OPEN_PAR = 56
    CLOSE_PAR = 57
    OPEN_BRACKET = 58
    CLOSE_BRACKET = 59
    OPEN_BRACE = 60
    CLOSE_BRACE = 61
    INT_LITERAL = 62
    FLOAT_LITERAL = 63
    STRING_LITERAL = 64
    BOOLEAN_LITERAL = 65
    IDENTIFIER = 66
    COMMENT = 67
    WS = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'GAME'", "'DEFINE'", "'BOARD'", "'PLAYERS'", "'CONDITIONS'", 
            "'RULES'", "'PIECES'", "'OBSTACLES'", "'BOOSTERS'", "'PLAYER'", 
            "'COLOR'", "'AT'", "'ORDER'", "'CONDITION'", "'RULE'", "'PIECE'", 
            "'COUNT'", "'ACTION'", "'SETUP'", "'OBSTACLE'", "'BOOSTER'", 
            "'START'", "'END'", "'MOVE'", "'TO'", "'TURN'", "'ALL'", "'ANY'", 
            "'NONE'", "'IF'", "'ELSE'", "'FOR'", "'WHILE'", "'INPUT'", "'PRINT'", 
            "'RETURN'", "'IN'", "'BREAK'", "'ERROR'", "'AND'", "'OR'", "'NOT'", 
            "'=='", "'='", "'<'", "'<='", "'>'", "'>='", "'+'", "'-'", "'*'", 
            "'/'", "':'", "'.'", "','", "'('", "')'", "'['", "']'", "'{'", 
            "'}'" ]

    symbolicNames = [ "<INVALID>",
            "GAME", "DEFINE", "BOARD", "PLAYERS", "CONDITIONS", "RULES", 
            "PIECES", "OBSTACLES", "BOOSTERS", "PLAYER", "COLOR", "AT", 
            "ORDER", "CONDITION", "RULE", "PIECE", "COUNT", "ACTION", "SETUP", 
            "OBSTACLE", "BOOSTER", "START", "END", "MOVE", "TO", "TURN", 
            "ALL", "ANY", "NONE", "IF", "ELSE", "FOR", "WHILE", "INPUT", 
            "PRINT", "RETURN", "IN", "BREAK", "ERROR", "AND_OPT", "OR_OPT", 
            "NOT_OPT", "EQUAL_OPT", "ASSIGN_OPT", "LESS_THAN_OPT", "LESS_EQUAL_OPT", 
            "GREATER_THAN_OPT", "GREATER_EQUAL_OPT", "ADD_OPT", "SUB_OPT", 
            "MUL_OPT", "DIV_OPT", "COLON", "DOT", "COMMA", "OPEN_PAR", "CLOSE_PAR", 
            "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
            "INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
            "IDENTIFIER", "COMMENT", "WS" ]

    ruleNames = [ "GAME", "DEFINE", "BOARD", "PLAYERS", "CONDITIONS", "RULES", 
                  "PIECES", "OBSTACLES", "BOOSTERS", "PLAYER", "COLOR", 
                  "AT", "ORDER", "CONDITION", "RULE", "PIECE", "COUNT", 
                  "ACTION", "SETUP", "OBSTACLE", "BOOSTER", "START", "END", 
                  "MOVE", "TO", "TURN", "ALL", "ANY", "NONE", "IF", "ELSE", 
                  "FOR", "WHILE", "INPUT", "PRINT", "RETURN", "IN", "BREAK", 
                  "ERROR", "AND_OPT", "OR_OPT", "NOT_OPT", "EQUAL_OPT", 
                  "ASSIGN_OPT", "LESS_THAN_OPT", "LESS_EQUAL_OPT", "GREATER_THAN_OPT", 
                  "GREATER_EQUAL_OPT", "ADD_OPT", "SUB_OPT", "MUL_OPT", 
                  "DIV_OPT", "COLON", "DOT", "COMMA", "OPEN_PAR", "CLOSE_PAR", 
                  "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
                  "INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                  "IDENTIFIER", "COMMENT", "WS" ]

    grammarFileName = "BoardGameLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


