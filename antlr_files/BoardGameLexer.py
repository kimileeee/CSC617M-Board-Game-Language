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
        4,0,79,585,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
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
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,1,0,1,0,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,
        1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,32,
        1,32,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,
        1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,
        1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,
        1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,42,
        1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,45,1,45,
        1,45,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,48,1,48,1,48,1,48,1,49,
        1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,54,1,54,
        1,54,1,55,1,55,1,56,1,56,1,57,1,57,1,58,1,58,1,59,1,59,1,60,1,60,
        1,61,1,61,1,62,1,62,1,63,1,63,1,64,1,64,1,65,1,65,1,66,1,66,1,67,
        1,67,1,68,1,68,1,69,1,69,1,69,1,69,1,70,1,70,1,71,4,71,506,8,71,
        11,71,12,71,507,1,72,3,72,511,8,72,1,72,1,72,1,73,1,73,1,74,1,74,
        1,74,1,75,1,75,1,75,1,75,1,76,1,76,5,76,526,8,76,10,76,12,76,529,
        9,76,1,76,1,76,1,77,1,77,1,77,1,77,1,77,1,77,1,77,1,77,1,77,3,77,
        542,8,77,1,78,1,78,5,78,546,8,78,10,78,12,78,549,9,78,1,79,1,79,
        1,79,1,79,5,79,555,8,79,10,79,12,79,558,9,79,1,79,1,79,1,80,1,80,
        1,81,4,81,565,8,81,11,81,12,81,566,1,81,1,81,1,82,1,82,1,82,1,82,
        3,82,575,8,82,1,82,1,82,5,82,579,8,82,10,82,12,82,582,9,82,1,82,
        1,82,0,0,83,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,
        23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,
        45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,
        67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,
        89,45,91,46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,
        109,55,111,56,113,57,115,58,117,59,119,60,121,61,123,62,125,63,127,
        64,129,65,131,66,133,67,135,68,137,69,139,70,141,0,143,0,145,0,147,
        71,149,72,151,73,153,74,155,75,157,76,159,77,161,0,163,78,165,79,
        1,0,7,1,0,48,57,1,0,34,34,2,0,65,90,97,122,4,0,48,57,65,90,95,95,
        97,122,2,0,10,10,13,13,3,0,9,10,13,13,32,32,3,0,65,90,95,95,97,122,
        591,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,
        0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,
        0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,
        0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,
        0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,
        0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,
        0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,
        0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,
        0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,
        0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,
        0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,
        0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,
        119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,
        0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,
        1,0,0,0,0,139,1,0,0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,
        0,153,1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,1,0,0,0,0,163,1,
        0,0,0,0,165,1,0,0,0,1,167,1,0,0,0,3,172,1,0,0,0,5,179,1,0,0,0,7,
        185,1,0,0,0,9,193,1,0,0,0,11,204,1,0,0,0,13,210,1,0,0,0,15,216,1,
        0,0,0,17,221,1,0,0,0,19,227,1,0,0,0,21,234,1,0,0,0,23,244,1,0,0,
        0,25,253,1,0,0,0,27,260,1,0,0,0,29,266,1,0,0,0,31,272,1,0,0,0,33,
        282,1,0,0,0,35,287,1,0,0,0,37,293,1,0,0,0,39,299,1,0,0,0,41,306,
        1,0,0,0,43,312,1,0,0,0,45,321,1,0,0,0,47,329,1,0,0,0,49,335,1,0,
        0,0,51,339,1,0,0,0,53,344,1,0,0,0,55,347,1,0,0,0,57,355,1,0,0,0,
        59,360,1,0,0,0,61,364,1,0,0,0,63,371,1,0,0,0,65,374,1,0,0,0,67,379,
        1,0,0,0,69,384,1,0,0,0,71,388,1,0,0,0,73,394,1,0,0,0,75,400,1,0,
        0,0,77,406,1,0,0,0,79,413,1,0,0,0,81,419,1,0,0,0,83,425,1,0,0,0,
        85,429,1,0,0,0,87,433,1,0,0,0,89,438,1,0,0,0,91,441,1,0,0,0,93,444,
        1,0,0,0,95,448,1,0,0,0,97,451,1,0,0,0,99,455,1,0,0,0,101,458,1,0,
        0,0,103,460,1,0,0,0,105,462,1,0,0,0,107,465,1,0,0,0,109,467,1,0,
        0,0,111,470,1,0,0,0,113,472,1,0,0,0,115,474,1,0,0,0,117,476,1,0,
        0,0,119,478,1,0,0,0,121,480,1,0,0,0,123,482,1,0,0,0,125,484,1,0,
        0,0,127,486,1,0,0,0,129,488,1,0,0,0,131,490,1,0,0,0,133,492,1,0,
        0,0,135,494,1,0,0,0,137,496,1,0,0,0,139,498,1,0,0,0,141,502,1,0,
        0,0,143,505,1,0,0,0,145,510,1,0,0,0,147,514,1,0,0,0,149,516,1,0,
        0,0,151,519,1,0,0,0,153,523,1,0,0,0,155,541,1,0,0,0,157,543,1,0,
        0,0,159,550,1,0,0,0,161,561,1,0,0,0,163,564,1,0,0,0,165,574,1,0,
        0,0,167,168,5,71,0,0,168,169,5,65,0,0,169,170,5,77,0,0,170,171,5,
        69,0,0,171,2,1,0,0,0,172,173,5,68,0,0,173,174,5,69,0,0,174,175,5,
        70,0,0,175,176,5,73,0,0,176,177,5,78,0,0,177,178,5,69,0,0,178,4,
        1,0,0,0,179,180,5,66,0,0,180,181,5,79,0,0,181,182,5,65,0,0,182,183,
        5,82,0,0,183,184,5,68,0,0,184,6,1,0,0,0,185,186,5,80,0,0,186,187,
        5,76,0,0,187,188,5,65,0,0,188,189,5,89,0,0,189,190,5,69,0,0,190,
        191,5,82,0,0,191,192,5,83,0,0,192,8,1,0,0,0,193,194,5,67,0,0,194,
        195,5,79,0,0,195,196,5,78,0,0,196,197,5,68,0,0,197,198,5,73,0,0,
        198,199,5,84,0,0,199,200,5,73,0,0,200,201,5,79,0,0,201,202,5,78,
        0,0,202,203,5,83,0,0,203,10,1,0,0,0,204,205,5,84,0,0,205,206,5,73,
        0,0,206,207,5,77,0,0,207,208,5,69,0,0,208,209,5,82,0,0,209,12,1,
        0,0,0,210,211,5,83,0,0,211,212,5,67,0,0,212,213,5,79,0,0,213,214,
        5,82,0,0,214,215,5,69,0,0,215,14,1,0,0,0,216,217,5,68,0,0,217,218,
        5,73,0,0,218,219,5,67,0,0,219,220,5,69,0,0,220,16,1,0,0,0,221,222,
        5,82,0,0,222,223,5,85,0,0,223,224,5,76,0,0,224,225,5,69,0,0,225,
        226,5,83,0,0,226,18,1,0,0,0,227,228,5,80,0,0,228,229,5,73,0,0,229,
        230,5,69,0,0,230,231,5,67,0,0,231,232,5,69,0,0,232,233,5,83,0,0,
        233,20,1,0,0,0,234,235,5,79,0,0,235,236,5,66,0,0,236,237,5,83,0,
        0,237,238,5,84,0,0,238,239,5,65,0,0,239,240,5,67,0,0,240,241,5,76,
        0,0,241,242,5,69,0,0,242,243,5,83,0,0,243,22,1,0,0,0,244,245,5,66,
        0,0,245,246,5,79,0,0,246,247,5,79,0,0,247,248,5,83,0,0,248,249,5,
        84,0,0,249,250,5,69,0,0,250,251,5,82,0,0,251,252,5,83,0,0,252,24,
        1,0,0,0,253,254,5,80,0,0,254,255,5,76,0,0,255,256,5,65,0,0,256,257,
        5,89,0,0,257,258,5,69,0,0,258,259,5,82,0,0,259,26,1,0,0,0,260,261,
        5,67,0,0,261,262,5,79,0,0,262,263,5,76,0,0,263,264,5,79,0,0,264,
        265,5,82,0,0,265,28,1,0,0,0,266,267,5,79,0,0,267,268,5,82,0,0,268,
        269,5,68,0,0,269,270,5,69,0,0,270,271,5,82,0,0,271,30,1,0,0,0,272,
        273,5,67,0,0,273,274,5,79,0,0,274,275,5,78,0,0,275,276,5,68,0,0,
        276,277,5,73,0,0,277,278,5,84,0,0,278,279,5,73,0,0,279,280,5,79,
        0,0,280,281,5,78,0,0,281,32,1,0,0,0,282,283,5,82,0,0,283,284,5,85,
        0,0,284,285,5,76,0,0,285,286,5,69,0,0,286,34,1,0,0,0,287,288,5,80,
        0,0,288,289,5,73,0,0,289,290,5,69,0,0,290,291,5,67,0,0,291,292,5,
        69,0,0,292,36,1,0,0,0,293,294,5,67,0,0,294,295,5,79,0,0,295,296,
        5,85,0,0,296,297,5,78,0,0,297,298,5,84,0,0,298,38,1,0,0,0,299,300,
        5,65,0,0,300,301,5,67,0,0,301,302,5,84,0,0,302,303,5,73,0,0,303,
        304,5,79,0,0,304,305,5,78,0,0,305,40,1,0,0,0,306,307,5,83,0,0,307,
        308,5,69,0,0,308,309,5,84,0,0,309,310,5,85,0,0,310,311,5,80,0,0,
        311,42,1,0,0,0,312,313,5,79,0,0,313,314,5,66,0,0,314,315,5,83,0,
        0,315,316,5,84,0,0,316,317,5,65,0,0,317,318,5,67,0,0,318,319,5,76,
        0,0,319,320,5,69,0,0,320,44,1,0,0,0,321,322,5,66,0,0,322,323,5,79,
        0,0,323,324,5,79,0,0,324,325,5,83,0,0,325,326,5,84,0,0,326,327,5,
        69,0,0,327,328,5,82,0,0,328,46,1,0,0,0,329,330,5,83,0,0,330,331,
        5,84,0,0,331,332,5,65,0,0,332,333,5,82,0,0,333,334,5,84,0,0,334,
        48,1,0,0,0,335,336,5,69,0,0,336,337,5,78,0,0,337,338,5,68,0,0,338,
        50,1,0,0,0,339,340,5,77,0,0,340,341,5,79,0,0,341,342,5,86,0,0,342,
        343,5,69,0,0,343,52,1,0,0,0,344,345,5,84,0,0,345,346,5,79,0,0,346,
        54,1,0,0,0,347,348,5,67,0,0,348,349,5,79,0,0,349,350,5,78,0,0,350,
        351,5,86,0,0,351,352,5,69,0,0,352,353,5,82,0,0,353,354,5,84,0,0,
        354,56,1,0,0,0,355,356,5,84,0,0,356,357,5,85,0,0,357,358,5,82,0,
        0,358,359,5,78,0,0,359,58,1,0,0,0,360,361,5,82,0,0,361,362,5,79,
        0,0,362,363,5,87,0,0,363,60,1,0,0,0,364,365,5,67,0,0,365,366,5,79,
        0,0,366,367,5,76,0,0,367,368,5,85,0,0,368,369,5,77,0,0,369,370,5,
        78,0,0,370,62,1,0,0,0,371,372,5,73,0,0,372,373,5,70,0,0,373,64,1,
        0,0,0,374,375,5,69,0,0,375,376,5,76,0,0,376,377,5,83,0,0,377,378,
        5,69,0,0,378,66,1,0,0,0,379,380,5,84,0,0,380,381,5,72,0,0,381,382,
        5,69,0,0,382,383,5,78,0,0,383,68,1,0,0,0,384,385,5,70,0,0,385,386,
        5,79,0,0,386,387,5,82,0,0,387,70,1,0,0,0,388,389,5,87,0,0,389,390,
        5,72,0,0,390,391,5,73,0,0,391,392,5,76,0,0,392,393,5,69,0,0,393,
        72,1,0,0,0,394,395,5,73,0,0,395,396,5,78,0,0,396,397,5,80,0,0,397,
        398,5,85,0,0,398,399,5,84,0,0,399,74,1,0,0,0,400,401,5,80,0,0,401,
        402,5,82,0,0,402,403,5,73,0,0,403,404,5,78,0,0,404,405,5,84,0,0,
        405,76,1,0,0,0,406,407,5,82,0,0,407,408,5,69,0,0,408,409,5,84,0,
        0,409,410,5,85,0,0,410,411,5,82,0,0,411,412,5,78,0,0,412,78,1,0,
        0,0,413,414,5,66,0,0,414,415,5,82,0,0,415,416,5,69,0,0,416,417,5,
        65,0,0,417,418,5,75,0,0,418,80,1,0,0,0,419,420,5,69,0,0,420,421,
        5,82,0,0,421,422,5,82,0,0,422,423,5,79,0,0,423,424,5,82,0,0,424,
        82,1,0,0,0,425,426,5,65,0,0,426,427,5,76,0,0,427,428,5,76,0,0,428,
        84,1,0,0,0,429,430,5,65,0,0,430,431,5,78,0,0,431,432,5,89,0,0,432,
        86,1,0,0,0,433,434,5,78,0,0,434,435,5,79,0,0,435,436,5,78,0,0,436,
        437,5,69,0,0,437,88,1,0,0,0,438,439,5,73,0,0,439,440,5,78,0,0,440,
        90,1,0,0,0,441,442,5,65,0,0,442,443,5,84,0,0,443,92,1,0,0,0,444,
        445,5,65,0,0,445,446,5,78,0,0,446,447,5,68,0,0,447,94,1,0,0,0,448,
        449,5,79,0,0,449,450,5,82,0,0,450,96,1,0,0,0,451,452,5,78,0,0,452,
        453,5,79,0,0,453,454,5,84,0,0,454,98,1,0,0,0,455,456,5,61,0,0,456,
        457,5,61,0,0,457,100,1,0,0,0,458,459,5,61,0,0,459,102,1,0,0,0,460,
        461,5,60,0,0,461,104,1,0,0,0,462,463,5,60,0,0,463,464,5,61,0,0,464,
        106,1,0,0,0,465,466,5,62,0,0,466,108,1,0,0,0,467,468,5,62,0,0,468,
        469,5,61,0,0,469,110,1,0,0,0,470,471,5,43,0,0,471,112,1,0,0,0,472,
        473,5,45,0,0,473,114,1,0,0,0,474,475,5,42,0,0,475,116,1,0,0,0,476,
        477,5,47,0,0,477,118,1,0,0,0,478,479,5,94,0,0,479,120,1,0,0,0,480,
        481,5,58,0,0,481,122,1,0,0,0,482,483,5,46,0,0,483,124,1,0,0,0,484,
        485,5,44,0,0,485,126,1,0,0,0,486,487,5,40,0,0,487,128,1,0,0,0,488,
        489,5,41,0,0,489,130,1,0,0,0,490,491,5,91,0,0,491,132,1,0,0,0,492,
        493,5,93,0,0,493,134,1,0,0,0,494,495,5,123,0,0,495,136,1,0,0,0,496,
        497,5,125,0,0,497,138,1,0,0,0,498,499,5,46,0,0,499,500,5,46,0,0,
        500,501,5,46,0,0,501,140,1,0,0,0,502,503,7,0,0,0,503,142,1,0,0,0,
        504,506,3,141,70,0,505,504,1,0,0,0,506,507,1,0,0,0,507,505,1,0,0,
        0,507,508,1,0,0,0,508,144,1,0,0,0,509,511,5,45,0,0,510,509,1,0,0,
        0,510,511,1,0,0,0,511,512,1,0,0,0,512,513,3,143,71,0,513,146,1,0,
        0,0,514,515,3,143,71,0,515,148,1,0,0,0,516,517,5,45,0,0,517,518,
        3,143,71,0,518,150,1,0,0,0,519,520,3,145,72,0,520,521,5,46,0,0,521,
        522,3,143,71,0,522,152,1,0,0,0,523,527,5,34,0,0,524,526,8,1,0,0,
        525,524,1,0,0,0,526,529,1,0,0,0,527,525,1,0,0,0,527,528,1,0,0,0,
        528,530,1,0,0,0,529,527,1,0,0,0,530,531,5,34,0,0,531,154,1,0,0,0,
        532,533,5,84,0,0,533,534,5,114,0,0,534,535,5,117,0,0,535,542,5,101,
        0,0,536,537,5,70,0,0,537,538,5,97,0,0,538,539,5,108,0,0,539,540,
        5,115,0,0,540,542,5,101,0,0,541,532,1,0,0,0,541,536,1,0,0,0,542,
        156,1,0,0,0,543,547,7,2,0,0,544,546,7,3,0,0,545,544,1,0,0,0,546,
        549,1,0,0,0,547,545,1,0,0,0,547,548,1,0,0,0,548,158,1,0,0,0,549,
        547,1,0,0,0,550,551,5,47,0,0,551,552,5,47,0,0,552,556,1,0,0,0,553,
        555,8,4,0,0,554,553,1,0,0,0,555,558,1,0,0,0,556,554,1,0,0,0,556,
        557,1,0,0,0,557,559,1,0,0,0,558,556,1,0,0,0,559,560,6,79,0,0,560,
        160,1,0,0,0,561,562,5,32,0,0,562,162,1,0,0,0,563,565,7,5,0,0,564,
        563,1,0,0,0,565,566,1,0,0,0,566,564,1,0,0,0,566,567,1,0,0,0,567,
        568,1,0,0,0,568,569,6,81,1,0,569,164,1,0,0,0,570,575,3,147,73,0,
        571,575,3,149,74,0,572,575,3,153,76,0,573,575,3,151,75,0,574,570,
        1,0,0,0,574,571,1,0,0,0,574,572,1,0,0,0,574,573,1,0,0,0,575,576,
        1,0,0,0,576,580,7,6,0,0,577,579,7,3,0,0,578,577,1,0,0,0,579,582,
        1,0,0,0,580,578,1,0,0,0,580,581,1,0,0,0,581,583,1,0,0,0,582,580,
        1,0,0,0,583,584,6,82,2,0,584,166,1,0,0,0,10,0,507,510,527,541,547,
        556,566,574,580,3,0,2,0,0,1,0,0,3,0
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
    CONVERT = 28
    TURN = 29
    ROW = 30
    COLUMN = 31
    IF = 32
    ELSE = 33
    THEN = 34
    FOR = 35
    WHILE = 36
    INPUT = 37
    PRINT = 38
    RETURN = 39
    BREAK = 40
    ERROR = 41
    ALL = 42
    ANY = 43
    NONE = 44
    IN = 45
    AT = 46
    AND_OPT = 47
    OR_OPT = 48
    NOT_OPT = 49
    EQUAL_OPT = 50
    ASSIGN_OPT = 51
    LESS_THAN_OPT = 52
    LESS_EQUAL_OPT = 53
    GREATER_THAN_OPT = 54
    GREATER_EQUAL_OPT = 55
    ADD_OPT = 56
    SUB_OPT = 57
    MUL_OPT = 58
    DIV_OPT = 59
    EXP_OPT = 60
    COLON = 61
    DOT = 62
    COMMA = 63
    OPEN_PAR = 64
    CLOSE_PAR = 65
    OPEN_BRACKET = 66
    CLOSE_BRACKET = 67
    OPEN_BRACE = 68
    CLOSE_BRACE = 69
    ELIPSIS = 70
    POSITIVE_INT_LITERAL = 71
    NEGATIVE_INT_LITERAL = 72
    FLOAT_LITERAL = 73
    STRING_LITERAL = 74
    BOOLEAN_LITERAL = 75
    IDENTIFIER = 76
    COMMENT = 77
    WS = 78
    INVALID_IDENTIFIER = 79

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"COMMENTS", u"ERRORS" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'GAME'", "'DEFINE'", "'BOARD'", "'PLAYERS'", "'CONDITIONS'", 
            "'TIMER'", "'SCORE'", "'DICE'", "'RULES'", "'PIECES'", "'OBSTACLES'", 
            "'BOOSTERS'", "'PLAYER'", "'COLOR'", "'ORDER'", "'CONDITION'", 
            "'RULE'", "'PIECE'", "'COUNT'", "'ACTION'", "'SETUP'", "'OBSTACLE'", 
            "'BOOSTER'", "'START'", "'END'", "'MOVE'", "'TO'", "'CONVERT'", 
            "'TURN'", "'ROW'", "'COLUMN'", "'IF'", "'ELSE'", "'THEN'", "'FOR'", 
            "'WHILE'", "'INPUT'", "'PRINT'", "'RETURN'", "'BREAK'", "'ERROR'", 
            "'ALL'", "'ANY'", "'NONE'", "'IN'", "'AT'", "'AND'", "'OR'", 
            "'NOT'", "'=='", "'='", "'<'", "'<='", "'>'", "'>='", "'+'", 
            "'-'", "'*'", "'/'", "'^'", "':'", "'.'", "','", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "'...'" ]

    symbolicNames = [ "<INVALID>",
            "GAME", "DEFINE", "BOARD", "PLAYERS", "CONDITIONS", "TIMER", 
            "SCORE", "DICE", "RULES", "PIECES", "OBSTACLES", "BOOSTERS", 
            "PLAYER", "COLOR", "ORDER", "CONDITION", "RULE", "PIECE", "COUNT", 
            "ACTION", "SETUP", "OBSTACLE", "BOOSTER", "START", "END", "MOVE", 
            "TO", "CONVERT", "TURN", "ROW", "COLUMN", "IF", "ELSE", "THEN", 
            "FOR", "WHILE", "INPUT", "PRINT", "RETURN", "BREAK", "ERROR", 
            "ALL", "ANY", "NONE", "IN", "AT", "AND_OPT", "OR_OPT", "NOT_OPT", 
            "EQUAL_OPT", "ASSIGN_OPT", "LESS_THAN_OPT", "LESS_EQUAL_OPT", 
            "GREATER_THAN_OPT", "GREATER_EQUAL_OPT", "ADD_OPT", "SUB_OPT", 
            "MUL_OPT", "DIV_OPT", "EXP_OPT", "COLON", "DOT", "COMMA", "OPEN_PAR", 
            "CLOSE_PAR", "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", 
            "CLOSE_BRACE", "ELIPSIS", "POSITIVE_INT_LITERAL", "NEGATIVE_INT_LITERAL", 
            "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", "IDENTIFIER", 
            "COMMENT", "WS", "INVALID_IDENTIFIER" ]

    ruleNames = [ "GAME", "DEFINE", "BOARD", "PLAYERS", "CONDITIONS", "TIMER", 
                  "SCORE", "DICE", "RULES", "PIECES", "OBSTACLES", "BOOSTERS", 
                  "PLAYER", "COLOR", "ORDER", "CONDITION", "RULE", "PIECE", 
                  "COUNT", "ACTION", "SETUP", "OBSTACLE", "BOOSTER", "START", 
                  "END", "MOVE", "TO", "CONVERT", "TURN", "ROW", "COLUMN", 
                  "IF", "ELSE", "THEN", "FOR", "WHILE", "INPUT", "PRINT", 
                  "RETURN", "BREAK", "ERROR", "ALL", "ANY", "NONE", "IN", 
                  "AT", "AND_OPT", "OR_OPT", "NOT_OPT", "EQUAL_OPT", "ASSIGN_OPT", 
                  "LESS_THAN_OPT", "LESS_EQUAL_OPT", "GREATER_THAN_OPT", 
                  "GREATER_EQUAL_OPT", "ADD_OPT", "SUB_OPT", "MUL_OPT", 
                  "DIV_OPT", "EXP_OPT", "COLON", "DOT", "COMMA", "OPEN_PAR", 
                  "CLOSE_PAR", "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", 
                  "CLOSE_BRACE", "ELIPSIS", "DIGIT", "NUMBER", "INTEGER", 
                  "POSITIVE_INT_LITERAL", "NEGATIVE_INT_LITERAL", "FLOAT_LITERAL", 
                  "STRING_LITERAL", "BOOLEAN_LITERAL", "IDENTIFIER", "COMMENT", 
                  "SPACE", "WS", "INVALID_IDENTIFIER" ]

    grammarFileName = "BoardGameLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


