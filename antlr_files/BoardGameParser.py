# Generated from BoardGameParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,77,761,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        1,0,1,0,4,0,96,8,0,11,0,12,0,97,1,0,1,0,1,1,1,1,1,1,3,1,105,8,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,4,3,117,8,3,11,3,12,3,118,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,141,8,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,3,7,
        151,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,162,8,8,1,9,1,9,
        1,9,1,9,1,9,5,9,169,8,9,10,9,12,9,172,9,9,1,9,1,9,1,9,1,9,1,9,5,
        9,179,8,9,10,9,12,9,182,9,9,1,9,1,9,1,9,5,9,187,8,9,10,9,12,9,190,
        9,9,1,9,1,9,1,9,5,9,195,8,9,10,9,12,9,198,9,9,1,9,1,9,1,9,5,9,203,
        8,9,10,9,12,9,206,9,9,1,9,1,9,1,9,5,9,211,8,9,10,9,12,9,214,9,9,
        1,9,1,9,1,9,5,9,219,8,9,10,9,12,9,222,9,9,1,9,1,9,1,9,5,9,227,8,
        9,10,9,12,9,230,9,9,1,9,1,9,1,9,5,9,235,8,9,10,9,12,9,238,9,9,3,
        9,240,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,
        252,8,11,10,11,12,11,255,9,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,
        263,8,11,10,11,12,11,266,9,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,
        274,8,11,10,11,12,11,277,9,11,3,11,279,8,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,3,12,290,8,12,1,12,1,12,1,12,5,12,295,8,
        12,10,12,12,12,298,9,12,1,13,1,13,1,14,1,14,1,14,1,14,5,14,306,8,
        14,10,14,12,14,309,9,14,1,14,1,14,1,14,1,14,5,14,315,8,14,10,14,
        12,14,318,9,14,1,14,1,14,1,14,1,14,5,14,324,8,14,10,14,12,14,327,
        9,14,1,14,1,14,1,14,1,14,5,14,333,8,14,10,14,12,14,336,9,14,1,14,
        1,14,1,14,1,14,1,14,5,14,343,8,14,10,14,12,14,346,9,14,1,14,1,14,
        1,14,1,14,5,14,352,8,14,10,14,12,14,355,9,14,1,14,1,14,1,14,1,14,
        1,14,5,14,362,8,14,10,14,12,14,365,9,14,1,14,1,14,1,14,1,14,5,14,
        371,8,14,10,14,12,14,374,9,14,1,14,1,14,1,14,1,14,5,14,380,8,14,
        10,14,12,14,383,9,14,3,14,385,8,14,1,15,1,15,1,15,3,15,390,8,15,
        1,16,1,16,1,16,1,16,1,16,5,16,397,8,16,10,16,12,16,400,9,16,1,16,
        1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,3,19,414,
        8,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,3,20,424,8,20,1,21,
        1,21,1,21,1,21,1,21,3,21,431,8,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,3,21,440,8,21,1,21,1,21,3,21,444,8,21,1,22,1,22,1,22,5,22,449,
        8,22,10,22,12,22,452,9,22,1,23,1,23,1,23,1,23,1,23,1,23,5,23,460,
        8,23,10,23,12,23,463,9,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,471,
        8,24,10,24,12,24,474,9,24,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,27,
        1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        3,28,497,8,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,
        1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,518,8,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,530,8,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,543,8,31,
        10,31,12,31,546,9,31,1,31,1,31,3,31,550,8,31,1,32,1,32,5,32,554,
        8,32,10,32,12,32,557,9,32,1,32,1,32,1,32,1,32,3,32,563,8,32,1,32,
        1,32,1,32,1,32,3,32,569,8,32,1,32,1,32,1,32,1,32,5,32,575,8,32,10,
        32,12,32,578,9,32,1,32,1,32,1,32,1,32,3,32,584,8,32,1,32,1,32,1,
        32,1,32,3,32,590,8,32,1,32,1,32,1,32,1,32,5,32,596,8,32,10,32,12,
        32,599,9,32,1,32,1,32,1,32,1,32,3,32,605,8,32,1,32,1,32,1,32,1,32,
        3,32,611,8,32,1,32,1,32,3,32,615,8,32,1,33,1,33,1,33,1,33,3,33,621,
        8,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,629,8,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,5,33,642,8,33,10,33,12,33,
        645,9,33,3,33,647,8,33,1,34,1,34,1,34,1,34,3,34,653,8,34,1,34,1,
        34,1,34,1,34,1,34,1,34,3,34,661,8,34,1,34,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,5,34,674,8,34,10,34,12,34,677,9,34,3,
        34,679,8,34,1,35,1,35,1,35,1,35,3,35,685,8,35,1,35,1,35,1,35,1,36,
        1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
        1,37,1,37,1,37,3,37,707,8,37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,
        1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,5,40,726,8,40,
        10,40,12,40,729,9,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,42,1,42,
        1,42,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,
        1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,0,3,24,46,48,46,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,0,
        7,4,0,3,5,7,7,9,12,14,14,1,0,69,70,1,0,29,30,2,0,48,48,50,53,1,0,
        56,57,1,0,54,55,1,0,45,46,841,0,92,1,0,0,0,2,101,1,0,0,0,4,110,1,
        0,0,0,6,116,1,0,0,0,8,140,1,0,0,0,10,142,1,0,0,0,12,144,1,0,0,0,
        14,150,1,0,0,0,16,161,1,0,0,0,18,239,1,0,0,0,20,241,1,0,0,0,22,278,
        1,0,0,0,24,289,1,0,0,0,26,299,1,0,0,0,28,384,1,0,0,0,30,389,1,0,
        0,0,32,391,1,0,0,0,34,403,1,0,0,0,36,407,1,0,0,0,38,413,1,0,0,0,
        40,418,1,0,0,0,42,443,1,0,0,0,44,445,1,0,0,0,46,453,1,0,0,0,48,464,
        1,0,0,0,50,475,1,0,0,0,52,477,1,0,0,0,54,479,1,0,0,0,56,496,1,0,
        0,0,58,498,1,0,0,0,60,503,1,0,0,0,62,549,1,0,0,0,64,614,1,0,0,0,
        66,646,1,0,0,0,68,678,1,0,0,0,70,680,1,0,0,0,72,689,1,0,0,0,74,706,
        1,0,0,0,76,708,1,0,0,0,78,716,1,0,0,0,80,722,1,0,0,0,82,732,1,0,
        0,0,84,737,1,0,0,0,86,740,1,0,0,0,88,745,1,0,0,0,90,752,1,0,0,0,
        92,93,5,1,0,0,93,95,5,74,0,0,94,96,3,2,1,0,95,94,1,0,0,0,96,97,1,
        0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,3,4,2,0,100,
        1,1,0,0,0,101,104,5,2,0,0,102,105,5,74,0,0,103,105,3,22,11,0,104,
        102,1,0,0,0,104,103,1,0,0,0,105,106,1,0,0,0,106,107,5,59,0,0,107,
        108,3,6,3,0,108,109,5,25,0,0,109,3,1,0,0,0,110,111,5,24,0,0,111,
        112,5,59,0,0,112,113,3,6,3,0,113,114,5,25,0,0,114,5,1,0,0,0,115,
        117,3,8,4,0,116,115,1,0,0,0,117,118,1,0,0,0,118,116,1,0,0,0,118,
        119,1,0,0,0,119,7,1,0,0,0,120,141,3,54,27,0,121,141,3,64,32,0,122,
        141,3,56,28,0,123,141,3,58,29,0,124,141,3,60,30,0,125,141,3,62,31,
        0,126,141,3,66,33,0,127,141,3,68,34,0,128,141,3,72,36,0,129,141,
        3,70,35,0,130,141,3,86,43,0,131,141,3,88,44,0,132,141,3,90,45,0,
        133,141,3,28,14,0,134,141,3,74,37,0,135,141,3,76,38,0,136,141,3,
        78,39,0,137,141,3,80,40,0,138,141,3,82,41,0,139,141,3,84,42,0,140,
        120,1,0,0,0,140,121,1,0,0,0,140,122,1,0,0,0,140,123,1,0,0,0,140,
        124,1,0,0,0,140,125,1,0,0,0,140,126,1,0,0,0,140,127,1,0,0,0,140,
        128,1,0,0,0,140,129,1,0,0,0,140,130,1,0,0,0,140,131,1,0,0,0,140,
        132,1,0,0,0,140,133,1,0,0,0,140,134,1,0,0,0,140,135,1,0,0,0,140,
        136,1,0,0,0,140,137,1,0,0,0,140,138,1,0,0,0,140,139,1,0,0,0,141,
        9,1,0,0,0,142,143,7,0,0,0,143,11,1,0,0,0,144,145,7,1,0,0,145,13,
        1,0,0,0,146,151,3,12,6,0,147,151,5,71,0,0,148,151,5,72,0,0,149,151,
        5,73,0,0,150,146,1,0,0,0,150,147,1,0,0,0,150,148,1,0,0,0,150,149,
        1,0,0,0,151,15,1,0,0,0,152,162,3,14,7,0,153,162,3,22,11,0,154,162,
        3,20,10,0,155,162,5,74,0,0,156,157,5,62,0,0,157,158,3,28,14,0,158,
        159,5,63,0,0,159,162,1,0,0,0,160,162,3,32,16,0,161,152,1,0,0,0,161,
        153,1,0,0,0,161,154,1,0,0,0,161,155,1,0,0,0,161,156,1,0,0,0,161,
        160,1,0,0,0,162,17,1,0,0,0,163,164,5,74,0,0,164,165,5,49,0,0,165,
        170,3,14,7,0,166,167,5,61,0,0,167,169,3,18,9,0,168,166,1,0,0,0,169,
        172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,240,1,0,0,0,172,
        170,1,0,0,0,173,174,5,74,0,0,174,175,5,49,0,0,175,180,3,30,15,0,
        176,177,5,61,0,0,177,179,3,18,9,0,178,176,1,0,0,0,179,182,1,0,0,
        0,180,178,1,0,0,0,180,181,1,0,0,0,181,240,1,0,0,0,182,180,1,0,0,
        0,183,188,5,74,0,0,184,185,5,61,0,0,185,187,3,18,9,0,186,184,1,0,
        0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,240,1,0,
        0,0,190,188,1,0,0,0,191,196,3,14,7,0,192,193,5,61,0,0,193,195,3,
        18,9,0,194,192,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,
        0,0,0,197,240,1,0,0,0,198,196,1,0,0,0,199,204,3,22,11,0,200,201,
        5,61,0,0,201,203,3,18,9,0,202,200,1,0,0,0,203,206,1,0,0,0,204,202,
        1,0,0,0,204,205,1,0,0,0,205,240,1,0,0,0,206,204,1,0,0,0,207,212,
        5,42,0,0,208,209,5,61,0,0,209,211,3,18,9,0,210,208,1,0,0,0,211,214,
        1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,240,1,0,0,0,214,212,
        1,0,0,0,215,220,5,41,0,0,216,217,5,61,0,0,217,219,3,18,9,0,218,216,
        1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,240,
        1,0,0,0,222,220,1,0,0,0,223,228,5,40,0,0,224,225,5,61,0,0,225,227,
        3,18,9,0,226,224,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,
        1,0,0,0,229,240,1,0,0,0,230,228,1,0,0,0,231,236,3,20,10,0,232,233,
        5,61,0,0,233,235,3,18,9,0,234,232,1,0,0,0,235,238,1,0,0,0,236,234,
        1,0,0,0,236,237,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,239,163,
        1,0,0,0,239,173,1,0,0,0,239,183,1,0,0,0,239,191,1,0,0,0,239,199,
        1,0,0,0,239,207,1,0,0,0,239,215,1,0,0,0,239,223,1,0,0,0,239,231,
        1,0,0,0,240,19,1,0,0,0,241,242,5,64,0,0,242,243,3,18,9,0,243,244,
        5,65,0,0,244,21,1,0,0,0,245,246,5,74,0,0,246,247,5,60,0,0,247,253,
        3,10,5,0,248,249,5,60,0,0,249,252,3,10,5,0,250,252,5,74,0,0,251,
        248,1,0,0,0,251,250,1,0,0,0,252,255,1,0,0,0,253,251,1,0,0,0,253,
        254,1,0,0,0,254,279,1,0,0,0,255,253,1,0,0,0,256,257,3,10,5,0,257,
        258,5,60,0,0,258,264,5,74,0,0,259,260,5,60,0,0,260,263,3,10,5,0,
        261,263,5,74,0,0,262,259,1,0,0,0,262,261,1,0,0,0,263,266,1,0,0,0,
        264,262,1,0,0,0,264,265,1,0,0,0,265,279,1,0,0,0,266,264,1,0,0,0,
        267,268,5,74,0,0,268,269,5,60,0,0,269,275,5,74,0,0,270,271,5,60,
        0,0,271,274,3,10,5,0,272,274,5,74,0,0,273,270,1,0,0,0,273,272,1,
        0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,279,1,
        0,0,0,277,275,1,0,0,0,278,245,1,0,0,0,278,256,1,0,0,0,278,267,1,
        0,0,0,279,23,1,0,0,0,280,281,6,12,-1,0,281,282,5,3,0,0,282,283,5,
        60,0,0,283,290,5,74,0,0,284,285,5,3,0,0,285,286,5,60,0,0,286,287,
        7,2,0,0,287,288,5,60,0,0,288,290,3,12,6,0,289,280,1,0,0,0,289,284,
        1,0,0,0,290,296,1,0,0,0,291,292,10,1,0,0,292,293,5,68,0,0,293,295,
        3,24,12,2,294,291,1,0,0,0,295,298,1,0,0,0,296,294,1,0,0,0,296,297,
        1,0,0,0,297,25,1,0,0,0,298,296,1,0,0,0,299,300,7,3,0,0,300,27,1,
        0,0,0,301,307,3,42,21,0,302,303,3,52,26,0,303,304,3,28,14,0,304,
        306,1,0,0,0,305,302,1,0,0,0,306,309,1,0,0,0,307,305,1,0,0,0,307,
        308,1,0,0,0,308,385,1,0,0,0,309,307,1,0,0,0,310,316,3,50,25,0,311,
        312,3,52,26,0,312,313,3,28,14,0,313,315,1,0,0,0,314,311,1,0,0,0,
        315,318,1,0,0,0,316,314,1,0,0,0,316,317,1,0,0,0,317,385,1,0,0,0,
        318,316,1,0,0,0,319,325,3,36,18,0,320,321,3,52,26,0,321,322,3,28,
        14,0,322,324,1,0,0,0,323,320,1,0,0,0,324,327,1,0,0,0,325,323,1,0,
        0,0,325,326,1,0,0,0,326,385,1,0,0,0,327,325,1,0,0,0,328,334,3,38,
        19,0,329,330,3,52,26,0,330,331,3,28,14,0,331,333,1,0,0,0,332,329,
        1,0,0,0,333,336,1,0,0,0,334,332,1,0,0,0,334,335,1,0,0,0,335,385,
        1,0,0,0,336,334,1,0,0,0,337,338,3,40,20,0,338,344,3,28,14,0,339,
        340,3,52,26,0,340,341,3,28,14,0,341,343,1,0,0,0,342,339,1,0,0,0,
        343,346,1,0,0,0,344,342,1,0,0,0,344,345,1,0,0,0,345,385,1,0,0,0,
        346,344,1,0,0,0,347,353,3,16,8,0,348,349,3,52,26,0,349,350,3,28,
        14,0,350,352,1,0,0,0,351,348,1,0,0,0,352,355,1,0,0,0,353,351,1,0,
        0,0,353,354,1,0,0,0,354,385,1,0,0,0,355,353,1,0,0,0,356,357,5,47,
        0,0,357,363,3,28,14,0,358,359,3,52,26,0,359,360,3,28,14,0,360,362,
        1,0,0,0,361,358,1,0,0,0,362,365,1,0,0,0,363,361,1,0,0,0,363,364,
        1,0,0,0,364,385,1,0,0,0,365,363,1,0,0,0,366,372,3,34,17,0,367,368,
        3,52,26,0,368,369,3,28,14,0,369,371,1,0,0,0,370,367,1,0,0,0,371,
        374,1,0,0,0,372,370,1,0,0,0,372,373,1,0,0,0,373,385,1,0,0,0,374,
        372,1,0,0,0,375,381,3,70,35,0,376,377,3,52,26,0,377,378,3,28,14,
        0,378,380,1,0,0,0,379,376,1,0,0,0,380,383,1,0,0,0,381,379,1,0,0,
        0,381,382,1,0,0,0,382,385,1,0,0,0,383,381,1,0,0,0,384,301,1,0,0,
        0,384,310,1,0,0,0,384,319,1,0,0,0,384,328,1,0,0,0,384,337,1,0,0,
        0,384,347,1,0,0,0,384,356,1,0,0,0,384,366,1,0,0,0,384,375,1,0,0,
        0,385,29,1,0,0,0,386,390,5,74,0,0,387,390,3,22,11,0,388,390,3,24,
        12,0,389,386,1,0,0,0,389,387,1,0,0,0,389,388,1,0,0,0,390,31,1,0,
        0,0,391,392,3,30,15,0,392,393,5,60,0,0,393,394,5,74,0,0,394,398,
        5,62,0,0,395,397,3,18,9,0,396,395,1,0,0,0,397,400,1,0,0,0,398,396,
        1,0,0,0,398,399,1,0,0,0,399,401,1,0,0,0,400,398,1,0,0,0,401,402,
        5,63,0,0,402,33,1,0,0,0,403,404,3,16,8,0,404,405,3,26,13,0,405,406,
        3,16,8,0,406,35,1,0,0,0,407,408,3,16,8,0,408,409,5,43,0,0,409,410,
        3,16,8,0,410,37,1,0,0,0,411,414,5,74,0,0,412,414,3,22,11,0,413,411,
        1,0,0,0,413,412,1,0,0,0,414,415,1,0,0,0,415,416,5,44,0,0,416,417,
        3,24,12,0,417,39,1,0,0,0,418,423,5,41,0,0,419,424,5,74,0,0,420,424,
        3,22,11,0,421,424,3,20,10,0,422,424,3,10,5,0,423,419,1,0,0,0,423,
        420,1,0,0,0,423,421,1,0,0,0,423,422,1,0,0,0,424,41,1,0,0,0,425,431,
        5,74,0,0,426,427,5,74,0,0,427,428,5,62,0,0,428,429,5,74,0,0,429,
        431,5,63,0,0,430,425,1,0,0,0,430,426,1,0,0,0,431,432,1,0,0,0,432,
        433,5,49,0,0,433,444,3,28,14,0,434,440,5,74,0,0,435,436,5,74,0,0,
        436,437,5,62,0,0,437,438,5,74,0,0,438,440,5,63,0,0,439,434,1,0,0,
        0,439,435,1,0,0,0,440,441,1,0,0,0,441,442,5,49,0,0,442,444,3,80,
        40,0,443,430,1,0,0,0,443,439,1,0,0,0,444,43,1,0,0,0,445,450,3,16,
        8,0,446,447,5,58,0,0,447,449,3,16,8,0,448,446,1,0,0,0,449,452,1,
        0,0,0,450,448,1,0,0,0,450,451,1,0,0,0,451,45,1,0,0,0,452,450,1,0,
        0,0,453,454,6,23,-1,0,454,455,3,44,22,0,455,461,1,0,0,0,456,457,
        10,2,0,0,457,458,7,4,0,0,458,460,3,44,22,0,459,456,1,0,0,0,460,463,
        1,0,0,0,461,459,1,0,0,0,461,462,1,0,0,0,462,47,1,0,0,0,463,461,1,
        0,0,0,464,465,6,24,-1,0,465,466,3,46,23,0,466,472,1,0,0,0,467,468,
        10,2,0,0,468,469,7,5,0,0,469,471,3,46,23,0,470,467,1,0,0,0,471,474,
        1,0,0,0,472,470,1,0,0,0,472,473,1,0,0,0,473,49,1,0,0,0,474,472,1,
        0,0,0,475,476,3,48,24,0,476,51,1,0,0,0,477,478,7,6,0,0,478,53,1,
        0,0,0,479,480,3,10,5,0,480,481,5,62,0,0,481,482,3,18,9,0,482,483,
        5,63,0,0,483,55,1,0,0,0,484,485,5,13,0,0,485,486,5,74,0,0,486,487,
        5,14,0,0,487,488,3,22,11,0,488,489,5,44,0,0,489,490,3,24,12,0,490,
        497,1,0,0,0,491,492,5,15,0,0,492,493,5,62,0,0,493,494,3,20,10,0,
        494,495,5,63,0,0,495,497,1,0,0,0,496,484,1,0,0,0,496,491,1,0,0,0,
        497,57,1,0,0,0,498,499,5,16,0,0,499,500,5,62,0,0,500,501,3,28,14,
        0,501,502,5,63,0,0,502,59,1,0,0,0,503,504,5,17,0,0,504,505,5,74,
        0,0,505,506,5,62,0,0,506,507,3,28,14,0,507,508,5,63,0,0,508,61,1,
        0,0,0,509,517,5,18,0,0,510,518,5,74,0,0,511,518,3,22,11,0,512,518,
        5,40,0,0,513,514,5,62,0,0,514,515,3,18,9,0,515,516,5,63,0,0,516,
        518,1,0,0,0,517,510,1,0,0,0,517,511,1,0,0,0,517,512,1,0,0,0,517,
        513,1,0,0,0,518,519,1,0,0,0,519,520,5,19,0,0,520,550,3,12,6,0,521,
        529,5,18,0,0,522,530,5,74,0,0,523,530,3,22,11,0,524,530,5,40,0,0,
        525,526,5,62,0,0,526,527,3,18,9,0,527,528,5,63,0,0,528,530,1,0,0,
        0,529,522,1,0,0,0,529,523,1,0,0,0,529,524,1,0,0,0,529,525,1,0,0,
        0,530,531,1,0,0,0,531,532,5,20,0,0,532,533,5,74,0,0,533,534,5,62,
        0,0,534,535,3,18,9,0,535,544,5,63,0,0,536,537,5,61,0,0,537,538,5,
        74,0,0,538,539,5,62,0,0,539,540,3,18,9,0,540,541,5,63,0,0,541,543,
        1,0,0,0,542,536,1,0,0,0,543,546,1,0,0,0,544,542,1,0,0,0,544,545,
        1,0,0,0,545,550,1,0,0,0,546,544,1,0,0,0,547,548,5,18,0,0,548,550,
        3,42,21,0,549,509,1,0,0,0,549,521,1,0,0,0,549,547,1,0,0,0,550,63,
        1,0,0,0,551,552,5,13,0,0,552,554,5,74,0,0,553,551,1,0,0,0,554,557,
        1,0,0,0,555,553,1,0,0,0,555,556,1,0,0,0,556,558,1,0,0,0,557,555,
        1,0,0,0,558,562,5,18,0,0,559,563,5,74,0,0,560,563,3,22,11,0,561,
        563,5,40,0,0,562,559,1,0,0,0,562,560,1,0,0,0,562,561,1,0,0,0,563,
        564,1,0,0,0,564,565,5,21,0,0,565,568,5,62,0,0,566,569,3,18,9,0,567,
        569,3,24,12,0,568,566,1,0,0,0,568,567,1,0,0,0,569,570,1,0,0,0,570,
        571,5,63,0,0,571,615,1,0,0,0,572,573,5,13,0,0,573,575,5,74,0,0,574,
        572,1,0,0,0,575,578,1,0,0,0,576,574,1,0,0,0,576,577,1,0,0,0,577,
        579,1,0,0,0,578,576,1,0,0,0,579,583,5,22,0,0,580,584,5,74,0,0,581,
        584,3,22,11,0,582,584,5,40,0,0,583,580,1,0,0,0,583,581,1,0,0,0,583,
        582,1,0,0,0,584,585,1,0,0,0,585,586,5,21,0,0,586,589,5,62,0,0,587,
        590,3,18,9,0,588,590,3,24,12,0,589,587,1,0,0,0,589,588,1,0,0,0,590,
        591,1,0,0,0,591,592,5,63,0,0,592,615,1,0,0,0,593,594,5,13,0,0,594,
        596,5,74,0,0,595,593,1,0,0,0,596,599,1,0,0,0,597,595,1,0,0,0,597,
        598,1,0,0,0,598,600,1,0,0,0,599,597,1,0,0,0,600,604,5,23,0,0,601,
        605,5,74,0,0,602,605,3,22,11,0,603,605,5,40,0,0,604,601,1,0,0,0,
        604,602,1,0,0,0,604,603,1,0,0,0,605,606,1,0,0,0,606,607,5,21,0,0,
        607,610,5,62,0,0,608,611,3,18,9,0,609,611,3,24,12,0,610,608,1,0,
        0,0,610,609,1,0,0,0,611,612,1,0,0,0,612,613,5,63,0,0,613,615,1,0,
        0,0,614,555,1,0,0,0,614,576,1,0,0,0,614,597,1,0,0,0,615,65,1,0,0,
        0,616,620,5,22,0,0,617,621,5,74,0,0,618,621,3,22,11,0,619,621,5,
        40,0,0,620,617,1,0,0,0,620,618,1,0,0,0,620,619,1,0,0,0,621,622,1,
        0,0,0,622,623,5,19,0,0,623,647,3,12,6,0,624,628,5,22,0,0,625,629,
        5,74,0,0,626,629,3,22,11,0,627,629,5,40,0,0,628,625,1,0,0,0,628,
        626,1,0,0,0,628,627,1,0,0,0,629,630,1,0,0,0,630,631,5,20,0,0,631,
        632,5,74,0,0,632,633,5,62,0,0,633,634,3,18,9,0,634,643,5,63,0,0,
        635,636,5,61,0,0,636,637,5,74,0,0,637,638,5,62,0,0,638,639,3,18,
        9,0,639,640,5,63,0,0,640,642,1,0,0,0,641,635,1,0,0,0,642,645,1,0,
        0,0,643,641,1,0,0,0,643,644,1,0,0,0,644,647,1,0,0,0,645,643,1,0,
        0,0,646,616,1,0,0,0,646,624,1,0,0,0,647,67,1,0,0,0,648,652,5,23,
        0,0,649,653,5,74,0,0,650,653,3,22,11,0,651,653,5,40,0,0,652,649,
        1,0,0,0,652,650,1,0,0,0,652,651,1,0,0,0,653,654,1,0,0,0,654,655,
        5,19,0,0,655,679,3,12,6,0,656,660,5,23,0,0,657,661,5,74,0,0,658,
        661,3,22,11,0,659,661,5,40,0,0,660,657,1,0,0,0,660,658,1,0,0,0,660,
        659,1,0,0,0,661,662,1,0,0,0,662,663,5,20,0,0,663,664,5,74,0,0,664,
        665,5,62,0,0,665,666,3,18,9,0,666,675,5,63,0,0,667,668,5,61,0,0,
        668,669,5,74,0,0,669,670,5,62,0,0,670,671,3,18,9,0,671,672,5,63,
        0,0,672,674,1,0,0,0,673,667,1,0,0,0,674,677,1,0,0,0,675,673,1,0,
        0,0,675,676,1,0,0,0,676,679,1,0,0,0,677,675,1,0,0,0,678,648,1,0,
        0,0,678,656,1,0,0,0,679,69,1,0,0,0,680,684,5,26,0,0,681,685,5,74,
        0,0,682,685,3,22,11,0,683,685,5,40,0,0,684,681,1,0,0,0,684,682,1,
        0,0,0,684,683,1,0,0,0,685,686,1,0,0,0,686,687,5,27,0,0,687,688,3,
        24,12,0,688,71,1,0,0,0,689,690,5,28,0,0,690,691,5,74,0,0,691,692,
        3,70,35,0,692,73,1,0,0,0,693,694,5,31,0,0,694,695,3,28,14,0,695,
        696,5,59,0,0,696,697,3,6,3,0,697,698,5,32,0,0,698,699,5,59,0,0,699,
        700,3,6,3,0,700,707,1,0,0,0,701,702,5,31,0,0,702,703,3,28,14,0,703,
        704,5,59,0,0,704,705,3,6,3,0,705,707,1,0,0,0,706,693,1,0,0,0,706,
        701,1,0,0,0,707,75,1,0,0,0,708,709,5,33,0,0,709,710,5,74,0,0,710,
        711,5,43,0,0,711,712,3,20,10,0,712,713,5,59,0,0,713,714,3,6,3,0,
        714,715,5,25,0,0,715,77,1,0,0,0,716,717,5,34,0,0,717,718,3,28,14,
        0,718,719,5,59,0,0,719,720,3,6,3,0,720,721,5,25,0,0,721,79,1,0,0,
        0,722,723,5,35,0,0,723,727,5,62,0,0,724,726,5,72,0,0,725,724,1,0,
        0,0,726,729,1,0,0,0,727,725,1,0,0,0,727,728,1,0,0,0,728,730,1,0,
        0,0,729,727,1,0,0,0,730,731,5,63,0,0,731,81,1,0,0,0,732,733,5,36,
        0,0,733,734,5,62,0,0,734,735,3,18,9,0,735,736,5,63,0,0,736,83,1,
        0,0,0,737,738,5,37,0,0,738,739,3,28,14,0,739,85,1,0,0,0,740,741,
        5,6,0,0,741,742,5,62,0,0,742,743,5,69,0,0,743,744,5,63,0,0,744,87,
        1,0,0,0,745,746,5,8,0,0,746,747,5,62,0,0,747,748,3,12,6,0,748,749,
        5,61,0,0,749,750,3,12,6,0,750,751,5,63,0,0,751,89,1,0,0,0,752,753,
        5,7,0,0,753,754,5,62,0,0,754,755,5,74,0,0,755,756,5,60,0,0,756,757,
        5,5,0,0,757,758,1,0,0,0,758,759,5,63,0,0,759,91,1,0,0,0,71,97,104,
        118,140,150,161,170,180,188,196,204,212,220,228,236,239,251,253,
        262,264,273,275,278,289,296,307,316,325,334,344,353,363,372,381,
        384,389,398,413,423,430,439,443,450,461,472,496,517,529,544,549,
        555,562,568,576,583,589,597,604,610,614,620,628,643,646,652,660,
        675,678,684,706,727
    ]

class BoardGameParser ( Parser ):

    grammarFileName = "BoardGameParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'GAME'", "'DEFINE'", "'BOARD'", "'PLAYERS'", 
                     "'CONDITIONS'", "'TIMER'", "'SCORE'", "'DICE'", "'RULES'", 
                     "'PIECES'", "'OBSTACLES'", "'BOOSTERS'", "'PLAYER'", 
                     "'COLOR'", "'ORDER'", "'CONDITION'", "'RULE'", "'PIECE'", 
                     "'COUNT'", "'ACTION'", "'SETUP'", "'OBSTACLE'", "'BOOSTER'", 
                     "'START'", "'END'", "'MOVE'", "'TO'", "'TURN'", "'ROW'", 
                     "'COLUMN'", "'IF'", "'ELSE'", "'FOR'", "'WHILE'", "'INPUT'", 
                     "'PRINT'", "'RETURN'", "'BREAK'", "'ERROR'", "'ALL'", 
                     "'ANY'", "'NONE'", "'IN'", "'AT'", "'AND'", "'OR'", 
                     "'NOT'", "'=='", "'='", "'<'", "'<='", "'>'", "'>='", 
                     "'+'", "'-'", "'*'", "'/'", "'^'", "':'", "'.'", "','", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'...'" ]

    symbolicNames = [ "<INVALID>", "GAME", "DEFINE", "BOARD", "PLAYERS", 
                      "CONDITIONS", "TIMER", "SCORE", "DICE", "RULES", "PIECES", 
                      "OBSTACLES", "BOOSTERS", "PLAYER", "COLOR", "ORDER", 
                      "CONDITION", "RULE", "PIECE", "COUNT", "ACTION", "SETUP", 
                      "OBSTACLE", "BOOSTER", "START", "END", "MOVE", "TO", 
                      "TURN", "ROW", "COLUMN", "IF", "ELSE", "FOR", "WHILE", 
                      "INPUT", "PRINT", "RETURN", "BREAK", "ERROR", "ALL", 
                      "ANY", "NONE", "IN", "AT", "AND_OPT", "OR_OPT", "NOT_OPT", 
                      "EQUAL_OPT", "ASSIGN_OPT", "LESS_THAN_OPT", "LESS_EQUAL_OPT", 
                      "GREATER_THAN_OPT", "GREATER_EQUAL_OPT", "ADD_OPT", 
                      "SUB_OPT", "MUL_OPT", "DIV_OPT", "EXP_OPT", "COLON", 
                      "DOT", "COMMA", "OPEN_PAR", "CLOSE_PAR", "OPEN_BRACKET", 
                      "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", "ELIPSIS", 
                      "POSITIVE_INT_LITERAL", "NEGATIVE_INT_LITERAL", "FLOAT_LITERAL", 
                      "STRING_LITERAL", "BOOLEAN_LITERAL", "IDENTIFIER", 
                      "COMMENT", "WS", "INVALID_IDENTIFIER" ]

    RULE_program = 0
    RULE_define_block = 1
    RULE_gameplay_block = 2
    RULE_code_block = 3
    RULE_statement = 4
    RULE_game_entities = 5
    RULE_int_literal = 6
    RULE_literal = 7
    RULE_primary = 8
    RULE_param_list = 9
    RULE_list = 10
    RULE_object_access = 11
    RULE_board_pos = 12
    RULE_conditional_opt = 13
    RULE_expression = 14
    RULE_objects = 15
    RULE_method_call = 16
    RULE_conditional_expression = 17
    RULE_in_expression = 18
    RULE_at_expression = 19
    RULE_any_expression = 20
    RULE_assignment_expression = 21
    RULE_exponent = 22
    RULE_multiplicative = 23
    RULE_additive = 24
    RULE_math_expression = 25
    RULE_logical_opt = 26
    RULE_game_entities_statement = 27
    RULE_player_statement = 28
    RULE_condition_statement = 29
    RULE_rule_statement = 30
    RULE_piece_statement = 31
    RULE_board_statement = 32
    RULE_obstacle_statement = 33
    RULE_booster_statement = 34
    RULE_move_statement = 35
    RULE_turn_statement = 36
    RULE_if_statement = 37
    RULE_for_statement = 38
    RULE_while_statement = 39
    RULE_input_statement = 40
    RULE_print_statement = 41
    RULE_return_statement = 42
    RULE_timer_statement = 43
    RULE_dice_statement = 44
    RULE_score_statement = 45

    ruleNames =  [ "program", "define_block", "gameplay_block", "code_block", 
                   "statement", "game_entities", "int_literal", "literal", 
                   "primary", "param_list", "list", "object_access", "board_pos", 
                   "conditional_opt", "expression", "objects", "method_call", 
                   "conditional_expression", "in_expression", "at_expression", 
                   "any_expression", "assignment_expression", "exponent", 
                   "multiplicative", "additive", "math_expression", "logical_opt", 
                   "game_entities_statement", "player_statement", "condition_statement", 
                   "rule_statement", "piece_statement", "board_statement", 
                   "obstacle_statement", "booster_statement", "move_statement", 
                   "turn_statement", "if_statement", "for_statement", "while_statement", 
                   "input_statement", "print_statement", "return_statement", 
                   "timer_statement", "dice_statement", "score_statement" ]

    EOF = Token.EOF
    GAME=1
    DEFINE=2
    BOARD=3
    PLAYERS=4
    CONDITIONS=5
    TIMER=6
    SCORE=7
    DICE=8
    RULES=9
    PIECES=10
    OBSTACLES=11
    BOOSTERS=12
    PLAYER=13
    COLOR=14
    ORDER=15
    CONDITION=16
    RULE=17
    PIECE=18
    COUNT=19
    ACTION=20
    SETUP=21
    OBSTACLE=22
    BOOSTER=23
    START=24
    END=25
    MOVE=26
    TO=27
    TURN=28
    ROW=29
    COLUMN=30
    IF=31
    ELSE=32
    FOR=33
    WHILE=34
    INPUT=35
    PRINT=36
    RETURN=37
    BREAK=38
    ERROR=39
    ALL=40
    ANY=41
    NONE=42
    IN=43
    AT=44
    AND_OPT=45
    OR_OPT=46
    NOT_OPT=47
    EQUAL_OPT=48
    ASSIGN_OPT=49
    LESS_THAN_OPT=50
    LESS_EQUAL_OPT=51
    GREATER_THAN_OPT=52
    GREATER_EQUAL_OPT=53
    ADD_OPT=54
    SUB_OPT=55
    MUL_OPT=56
    DIV_OPT=57
    EXP_OPT=58
    COLON=59
    DOT=60
    COMMA=61
    OPEN_PAR=62
    CLOSE_PAR=63
    OPEN_BRACKET=64
    CLOSE_BRACKET=65
    OPEN_BRACE=66
    CLOSE_BRACE=67
    ELIPSIS=68
    POSITIVE_INT_LITERAL=69
    NEGATIVE_INT_LITERAL=70
    FLOAT_LITERAL=71
    STRING_LITERAL=72
    BOOLEAN_LITERAL=73
    IDENTIFIER=74
    COMMENT=75
    WS=76
    INVALID_IDENTIFIER=77

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GAME(self):
            return self.getToken(BoardGameParser.GAME, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def gameplay_block(self):
            return self.getTypedRuleContext(BoardGameParser.Gameplay_blockContext,0)


        def define_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Define_blockContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Define_blockContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = BoardGameParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(BoardGameParser.GAME)
            self.state = 93
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.define_block()
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 99
            self.gameplay_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(BoardGameParser.DEFINE, 0)

        def COLON(self):
            return self.getToken(BoardGameParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(BoardGameParser.Code_blockContext,0)


        def END(self):
            return self.getToken(BoardGameParser.END, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_define_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_block" ):
                listener.enterDefine_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_block" ):
                listener.exitDefine_block(self)




    def define_block(self):

        localctx = BoardGameParser.Define_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_define_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(BoardGameParser.DEFINE)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 102
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 103
                self.object_access()
                pass


            self.state = 106
            self.match(BoardGameParser.COLON)
            self.state = 107
            self.code_block()
            self.state = 108
            self.match(BoardGameParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gameplay_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(BoardGameParser.START, 0)

        def COLON(self):
            return self.getToken(BoardGameParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(BoardGameParser.Code_blockContext,0)


        def END(self):
            return self.getToken(BoardGameParser.END, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_gameplay_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGameplay_block" ):
                listener.enterGameplay_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGameplay_block" ):
                listener.exitGameplay_block(self)




    def gameplay_block(self):

        localctx = BoardGameParser.Gameplay_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_gameplay_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(BoardGameParser.START)
            self.state = 111
            self.match(BoardGameParser.COLON)
            self.state = 112
            self.code_block()
            self.state = 113
            self.match(BoardGameParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.StatementContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.StatementContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)




    def code_block(self):

        localctx = BoardGameParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 115
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 118 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def game_entities_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Game_entities_statementContext,0)


        def board_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Board_statementContext,0)


        def player_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Player_statementContext,0)


        def condition_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Condition_statementContext,0)


        def rule_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Rule_statementContext,0)


        def piece_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Piece_statementContext,0)


        def obstacle_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Obstacle_statementContext,0)


        def booster_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Booster_statementContext,0)


        def turn_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Turn_statementContext,0)


        def move_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Move_statementContext,0)


        def timer_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Timer_statementContext,0)


        def dice_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Dice_statementContext,0)


        def score_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Score_statementContext,0)


        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(BoardGameParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BoardGameParser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(BoardGameParser.While_statementContext,0)


        def input_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Input_statementContext,0)


        def print_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Print_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Return_statementContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = BoardGameParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.game_entities_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.board_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.player_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.condition_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.rule_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 125
                self.piece_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 126
                self.obstacle_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 127
                self.booster_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 128
                self.turn_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 129
                self.move_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 130
                self.timer_statement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 131
                self.dice_statement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 132
                self.score_statement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 133
                self.expression()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 134
                self.if_statement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 135
                self.for_statement()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 136
                self.while_statement()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 137
                self.input_statement()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 138
                self.print_statement()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 139
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Game_entitiesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOARD(self):
            return self.getToken(BoardGameParser.BOARD, 0)

        def PLAYERS(self):
            return self.getToken(BoardGameParser.PLAYERS, 0)

        def CONDITIONS(self):
            return self.getToken(BoardGameParser.CONDITIONS, 0)

        def RULES(self):
            return self.getToken(BoardGameParser.RULES, 0)

        def PIECES(self):
            return self.getToken(BoardGameParser.PIECES, 0)

        def OBSTACLES(self):
            return self.getToken(BoardGameParser.OBSTACLES, 0)

        def BOOSTERS(self):
            return self.getToken(BoardGameParser.BOOSTERS, 0)

        def COLOR(self):
            return self.getToken(BoardGameParser.COLOR, 0)

        def SCORE(self):
            return self.getToken(BoardGameParser.SCORE, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_game_entities

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGame_entities" ):
                listener.enterGame_entities(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGame_entities" ):
                listener.exitGame_entities(self)




    def game_entities(self):

        localctx = BoardGameParser.Game_entitiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_game_entities)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24248) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSITIVE_INT_LITERAL(self):
            return self.getToken(BoardGameParser.POSITIVE_INT_LITERAL, 0)

        def NEGATIVE_INT_LITERAL(self):
            return self.getToken(BoardGameParser.NEGATIVE_INT_LITERAL, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_int_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_literal" ):
                listener.enterInt_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_literal" ):
                listener.exitInt_literal(self)




    def int_literal(self):

        localctx = BoardGameParser.Int_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_int_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not(_la==69 or _la==70):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_literal(self):
            return self.getTypedRuleContext(BoardGameParser.Int_literalContext,0)


        def FLOAT_LITERAL(self):
            return self.getToken(BoardGameParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(BoardGameParser.STRING_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(BoardGameParser.BOOLEAN_LITERAL, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = BoardGameParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literal)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [69, 70]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.int_literal()
                pass
            elif token in [71]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(BoardGameParser.FLOAT_LITERAL)
                pass
            elif token in [72]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.match(BoardGameParser.STRING_LITERAL)
                pass
            elif token in [73]:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.match(BoardGameParser.BOOLEAN_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BoardGameParser.LiteralContext,0)


        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def list_(self):
            return self.getTypedRuleContext(BoardGameParser.ListContext,0)


        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def method_call(self):
            return self.getTypedRuleContext(BoardGameParser.Method_callContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = BoardGameParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primary)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.object_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 154
                self.list_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 155
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 156
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 157
                self.expression()
                self.state = 158
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 160
                self.method_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)

        def literal(self):
            return self.getTypedRuleContext(BoardGameParser.LiteralContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.COMMA)
            else:
                return self.getToken(BoardGameParser.COMMA, i)

        def param_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Param_listContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Param_listContext,i)


        def objects(self):
            return self.getTypedRuleContext(BoardGameParser.ObjectsContext,0)


        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def NONE(self):
            return self.getToken(BoardGameParser.NONE, 0)

        def ANY(self):
            return self.getToken(BoardGameParser.ANY, 0)

        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)

        def list_(self):
            return self.getTypedRuleContext(BoardGameParser.ListContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)




    def param_list(self):

        localctx = BoardGameParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param_list)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 164
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 165
                self.literal()
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 166
                        self.match(BoardGameParser.COMMA)
                        self.state = 167
                        self.param_list() 
                    self.state = 172
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 174
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 175
                self.objects()
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 176
                        self.match(BoardGameParser.COMMA)
                        self.state = 177
                        self.param_list() 
                    self.state = 182
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 184
                        self.match(BoardGameParser.COMMA)
                        self.state = 185
                        self.param_list() 
                    self.state = 190
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.literal()
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 192
                        self.match(BoardGameParser.COMMA)
                        self.state = 193
                        self.param_list() 
                    self.state = 198
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 199
                self.object_access()
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 200
                        self.match(BoardGameParser.COMMA)
                        self.state = 201
                        self.param_list() 
                    self.state = 206
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 207
                self.match(BoardGameParser.NONE)
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 208
                        self.match(BoardGameParser.COMMA)
                        self.state = 209
                        self.param_list() 
                    self.state = 214
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 215
                self.match(BoardGameParser.ANY)
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 216
                        self.match(BoardGameParser.COMMA)
                        self.state = 217
                        self.param_list() 
                    self.state = 222
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 223
                self.match(BoardGameParser.ALL)
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 224
                        self.match(BoardGameParser.COMMA)
                        self.state = 225
                        self.param_list() 
                    self.state = 230
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 231
                self.list_()
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 232
                        self.match(BoardGameParser.COMMA)
                        self.state = 233
                        self.param_list() 
                    self.state = 238
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(BoardGameParser.OPEN_BRACKET, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(BoardGameParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = BoardGameParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(BoardGameParser.OPEN_BRACKET)
            self.state = 242
            self.param_list()
            self.state = 243
            self.match(BoardGameParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.DOT)
            else:
                return self.getToken(BoardGameParser.DOT, i)

        def game_entities(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Game_entitiesContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Game_entitiesContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_object_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_access" ):
                listener.enterObject_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_access" ):
                listener.exitObject_access(self)




    def object_access(self):

        localctx = BoardGameParser.Object_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_object_access)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 246
                self.match(BoardGameParser.DOT)
                self.state = 247
                self.game_entities()
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 251
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [60]:
                            self.state = 248
                            self.match(BoardGameParser.DOT)
                            self.state = 249
                            self.game_entities()
                            pass
                        elif token in [74]:
                            self.state = 250
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 255
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.game_entities()
                self.state = 257
                self.match(BoardGameParser.DOT)
                self.state = 258
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 262
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [60]:
                            self.state = 259
                            self.match(BoardGameParser.DOT)
                            self.state = 260
                            self.game_entities()
                            pass
                        elif token in [74]:
                            self.state = 261
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 266
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 268
                self.match(BoardGameParser.DOT)
                self.state = 269
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 273
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [60]:
                            self.state = 270
                            self.match(BoardGameParser.DOT)
                            self.state = 271
                            self.game_entities()
                            pass
                        elif token in [74]:
                            self.state = 272
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 277
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Board_posContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOARD(self):
            return self.getToken(BoardGameParser.BOARD, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.DOT)
            else:
                return self.getToken(BoardGameParser.DOT, i)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def ROW(self):
            return self.getToken(BoardGameParser.ROW, 0)

        def COLUMN(self):
            return self.getToken(BoardGameParser.COLUMN, 0)

        def int_literal(self):
            return self.getTypedRuleContext(BoardGameParser.Int_literalContext,0)


        def board_pos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Board_posContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Board_posContext,i)


        def ELIPSIS(self):
            return self.getToken(BoardGameParser.ELIPSIS, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_board_pos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoard_pos" ):
                listener.enterBoard_pos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoard_pos" ):
                listener.exitBoard_pos(self)



    def board_pos(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BoardGameParser.Board_posContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_board_pos, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 281
                self.match(BoardGameParser.BOARD)
                self.state = 282
                self.match(BoardGameParser.DOT)
                self.state = 283
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 284
                self.match(BoardGameParser.BOARD)
                self.state = 285
                self.match(BoardGameParser.DOT)
                self.state = 286
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 287
                self.match(BoardGameParser.DOT)

                self.state = 288
                self.int_literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.Board_posContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_board_pos)
                    self.state = 291
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 292
                    self.match(BoardGameParser.ELIPSIS)
                    self.state = 293
                    self.board_pos(2) 
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Conditional_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_OPT(self):
            return self.getToken(BoardGameParser.EQUAL_OPT, 0)

        def LESS_THAN_OPT(self):
            return self.getToken(BoardGameParser.LESS_THAN_OPT, 0)

        def LESS_EQUAL_OPT(self):
            return self.getToken(BoardGameParser.LESS_EQUAL_OPT, 0)

        def GREATER_THAN_OPT(self):
            return self.getToken(BoardGameParser.GREATER_THAN_OPT, 0)

        def GREATER_EQUAL_OPT(self):
            return self.getToken(BoardGameParser.GREATER_EQUAL_OPT, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_conditional_opt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_opt" ):
                listener.enterConditional_opt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_opt" ):
                listener.exitConditional_opt(self)




    def conditional_opt(self):

        localctx = BoardGameParser.Conditional_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_conditional_opt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17169973579350016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Assignment_expressionContext,0)


        def logical_opt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Logical_optContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Logical_optContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.ExpressionContext,i)


        def math_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Math_expressionContext,0)


        def in_expression(self):
            return self.getTypedRuleContext(BoardGameParser.In_expressionContext,0)


        def at_expression(self):
            return self.getTypedRuleContext(BoardGameParser.At_expressionContext,0)


        def any_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Any_expressionContext,0)


        def primary(self):
            return self.getTypedRuleContext(BoardGameParser.PrimaryContext,0)


        def NOT_OPT(self):
            return self.getToken(BoardGameParser.NOT_OPT, 0)

        def conditional_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Conditional_expressionContext,0)


        def move_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Move_statementContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = BoardGameParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.assignment_expression()
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 302
                        self.logical_opt()
                        self.state = 303
                        self.expression() 
                    self.state = 309
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.math_expression()
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 311
                        self.logical_opt()
                        self.state = 312
                        self.expression() 
                    self.state = 318
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
                self.in_expression()
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 320
                        self.logical_opt()
                        self.state = 321
                        self.expression() 
                    self.state = 327
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.at_expression()
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 329
                        self.logical_opt()
                        self.state = 330
                        self.expression() 
                    self.state = 336
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 337
                self.any_expression()
                self.state = 338
                self.expression()
                self.state = 344
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 339
                        self.logical_opt()
                        self.state = 340
                        self.expression() 
                    self.state = 346
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 347
                self.primary()
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 348
                        self.logical_opt()
                        self.state = 349
                        self.expression() 
                    self.state = 355
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 356
                self.match(BoardGameParser.NOT_OPT)
                self.state = 357
                self.expression()
                self.state = 363
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 358
                        self.logical_opt()
                        self.state = 359
                        self.expression() 
                    self.state = 365
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 366
                self.conditional_expression()
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 367
                        self.logical_opt()
                        self.state = 368
                        self.expression() 
                    self.state = 374
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 375
                self.move_statement()
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 376
                        self.logical_opt()
                        self.state = 377
                        self.expression() 
                    self.state = 383
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_objects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjects" ):
                listener.enterObjects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjects" ):
                listener.exitObjects(self)




    def objects(self):

        localctx = BoardGameParser.ObjectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_objects)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.object_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 388
                self.board_pos(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objects(self):
            return self.getTypedRuleContext(BoardGameParser.ObjectsContext,0)


        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def param_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Param_listContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Param_listContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_method_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_call" ):
                listener.enterMethod_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_call" ):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = BoardGameParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.objects()
            self.state = 392
            self.match(BoardGameParser.DOT)
            self.state = 393
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 394
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581418680) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 2017) != 0):
                self.state = 395
                self.param_list()
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 401
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.PrimaryContext,i)


        def conditional_opt(self):
            return self.getTypedRuleContext(BoardGameParser.Conditional_optContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_conditional_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_expression" ):
                listener.enterConditional_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_expression" ):
                listener.exitConditional_expression(self)




    def conditional_expression(self):

        localctx = BoardGameParser.Conditional_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_conditional_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.primary()
            self.state = 404
            self.conditional_opt()
            self.state = 405
            self.primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class In_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.PrimaryContext,i)


        def IN(self):
            return self.getToken(BoardGameParser.IN, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_in_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIn_expression" ):
                listener.enterIn_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIn_expression" ):
                listener.exitIn_expression(self)




    def in_expression(self):

        localctx = BoardGameParser.In_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_in_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.primary()
            self.state = 408
            self.match(BoardGameParser.IN)
            self.state = 409
            self.primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class At_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(BoardGameParser.AT, 0)

        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)


        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_at_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAt_expression" ):
                listener.enterAt_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAt_expression" ):
                listener.exitAt_expression(self)




    def at_expression(self):

        localctx = BoardGameParser.At_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_at_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 411
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 412
                self.object_access()
                pass


            self.state = 415
            self.match(BoardGameParser.AT)
            self.state = 416
            self.board_pos(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANY(self):
            return self.getToken(BoardGameParser.ANY, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def list_(self):
            return self.getTypedRuleContext(BoardGameParser.ListContext,0)


        def game_entities(self):
            return self.getTypedRuleContext(BoardGameParser.Game_entitiesContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_any_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_expression" ):
                listener.enterAny_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_expression" ):
                listener.exitAny_expression(self)




    def any_expression(self):

        localctx = BoardGameParser.Any_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_any_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(BoardGameParser.ANY)
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 419
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 420
                self.object_access()
                pass

            elif la_ == 3:
                self.state = 421
                self.list_()
                pass

            elif la_ == 4:
                self.state = 422
                self.game_entities()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)

        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def input_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Input_statementContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_assignment_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_expression" ):
                listener.enterAssignment_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_expression" ):
                listener.exitAssignment_expression(self)




    def assignment_expression(self):

        localctx = BoardGameParser.Assignment_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignment_expression)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 425
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 426
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 427
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 428
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 429
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 432
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 433
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 434
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 435
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 436
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 437
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 438
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 441
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 442
                self.input_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.PrimaryContext,i)


        def EXP_OPT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.EXP_OPT)
            else:
                return self.getToken(BoardGameParser.EXP_OPT, i)

        def getRuleIndex(self):
            return BoardGameParser.RULE_exponent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponent" ):
                listener.enterExponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponent" ):
                listener.exitExponent(self)




    def exponent(self):

        localctx = BoardGameParser.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exponent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.primary()
            self.state = 450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 446
                    self.match(BoardGameParser.EXP_OPT)
                    self.state = 447
                    self.primary() 
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exponent(self):
            return self.getTypedRuleContext(BoardGameParser.ExponentContext,0)


        def multiplicative(self):
            return self.getTypedRuleContext(BoardGameParser.MultiplicativeContext,0)


        def MUL_OPT(self):
            return self.getToken(BoardGameParser.MUL_OPT, 0)

        def DIV_OPT(self):
            return self.getToken(BoardGameParser.DIV_OPT, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_multiplicative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative" ):
                listener.enterMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative" ):
                listener.exitMultiplicative(self)



    def multiplicative(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BoardGameParser.MultiplicativeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_multiplicative, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.exponent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 461
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.MultiplicativeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative)
                    self.state = 456
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 457
                    _la = self._input.LA(1)
                    if not(_la==56 or _la==57):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 458
                    self.exponent() 
                self.state = 463
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative(self):
            return self.getTypedRuleContext(BoardGameParser.MultiplicativeContext,0)


        def additive(self):
            return self.getTypedRuleContext(BoardGameParser.AdditiveContext,0)


        def ADD_OPT(self):
            return self.getToken(BoardGameParser.ADD_OPT, 0)

        def SUB_OPT(self):
            return self.getToken(BoardGameParser.SUB_OPT, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_additive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)



    def additive(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BoardGameParser.AdditiveContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_additive, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.multiplicative(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 472
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.AdditiveContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                    self.state = 467
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 468
                    _la = self._input.LA(1)
                    if not(_la==54 or _la==55):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 469
                    self.multiplicative(0) 
                self.state = 474
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Math_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self):
            return self.getTypedRuleContext(BoardGameParser.AdditiveContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_math_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_expression" ):
                listener.enterMath_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_expression" ):
                listener.exitMath_expression(self)




    def math_expression(self):

        localctx = BoardGameParser.Math_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_math_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.additive(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND_OPT(self):
            return self.getToken(BoardGameParser.AND_OPT, 0)

        def OR_OPT(self):
            return self.getToken(BoardGameParser.OR_OPT, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_logical_opt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_opt" ):
                listener.enterLogical_opt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_opt" ):
                listener.exitLogical_opt(self)




    def logical_opt(self):

        localctx = BoardGameParser.Logical_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_logical_opt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            _la = self._input.LA(1)
            if not(_la==45 or _la==46):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Game_entities_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def game_entities(self):
            return self.getTypedRuleContext(BoardGameParser.Game_entitiesContext,0)


        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_game_entities_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGame_entities_statement" ):
                listener.enterGame_entities_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGame_entities_statement" ):
                listener.exitGame_entities_statement(self)




    def game_entities_statement(self):

        localctx = BoardGameParser.Game_entities_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_game_entities_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.game_entities()
            self.state = 480
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 481
            self.param_list()
            self.state = 482
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Player_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLAYER(self):
            return self.getToken(BoardGameParser.PLAYER, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def COLOR(self):
            return self.getToken(BoardGameParser.COLOR, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def AT(self):
            return self.getToken(BoardGameParser.AT, 0)

        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)


        def ORDER(self):
            return self.getToken(BoardGameParser.ORDER, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def list_(self):
            return self.getTypedRuleContext(BoardGameParser.ListContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_player_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayer_statement" ):
                listener.enterPlayer_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayer_statement" ):
                listener.exitPlayer_statement(self)




    def player_statement(self):

        localctx = BoardGameParser.Player_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_player_statement)
        try:
            self.state = 496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.match(BoardGameParser.PLAYER)
                self.state = 485
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 486
                self.match(BoardGameParser.COLOR)
                self.state = 487
                self.object_access()
                self.state = 488
                self.match(BoardGameParser.AT)
                self.state = 489
                self.board_pos(0)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.match(BoardGameParser.ORDER)
                self.state = 492
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 493
                self.list_()
                self.state = 494
                self.match(BoardGameParser.CLOSE_PAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONDITION(self):
            return self.getToken(BoardGameParser.CONDITION, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_condition_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_statement" ):
                listener.enterCondition_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_statement" ):
                listener.exitCondition_statement(self)




    def condition_statement(self):

        localctx = BoardGameParser.Condition_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_condition_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(BoardGameParser.CONDITION)
            self.state = 499
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 500
            self.expression()
            self.state = 501
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE(self):
            return self.getToken(BoardGameParser.RULE, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_rule_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_statement" ):
                listener.enterRule_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_statement" ):
                listener.exitRule_statement(self)




    def rule_statement(self):

        localctx = BoardGameParser.Rule_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_rule_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(BoardGameParser.RULE)
            self.state = 504
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 505
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 506
            self.expression()
            self.state = 507
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Piece_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIECE(self):
            return self.getToken(BoardGameParser.PIECE, 0)

        def COUNT(self):
            return self.getToken(BoardGameParser.COUNT, 0)

        def int_literal(self):
            return self.getTypedRuleContext(BoardGameParser.Int_literalContext,0)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)

        def OPEN_PAR(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.OPEN_PAR)
            else:
                return self.getToken(BoardGameParser.OPEN_PAR, i)

        def param_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Param_listContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Param_listContext,i)


        def CLOSE_PAR(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.CLOSE_PAR)
            else:
                return self.getToken(BoardGameParser.CLOSE_PAR, i)

        def ACTION(self):
            return self.getToken(BoardGameParser.ACTION, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.COMMA)
            else:
                return self.getToken(BoardGameParser.COMMA, i)

        def assignment_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Assignment_expressionContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_piece_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPiece_statement" ):
                listener.enterPiece_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPiece_statement" ):
                listener.exitPiece_statement(self)




    def piece_statement(self):

        localctx = BoardGameParser.Piece_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_piece_statement)
        self._la = 0 # Token type
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.match(BoardGameParser.PIECE)
                self.state = 517
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 510
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 511
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 512
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 4:
                    self.state = 513
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 514
                    self.param_list()
                    self.state = 515
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 519
                self.match(BoardGameParser.COUNT)
                self.state = 520
                self.int_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 521
                self.match(BoardGameParser.PIECE)
                self.state = 529
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 522
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 523
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 524
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 4:
                    self.state = 525
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 526
                    self.param_list()
                    self.state = 527
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 531
                self.match(BoardGameParser.ACTION)
                self.state = 532
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 533
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 534
                self.param_list()
                self.state = 535
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 544
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 536
                    self.match(BoardGameParser.COMMA)
                    self.state = 537
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 538
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 539
                    self.param_list()
                    self.state = 540
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 546
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 547
                self.match(BoardGameParser.PIECE)
                self.state = 548
                self.assignment_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Board_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIECE(self):
            return self.getToken(BoardGameParser.PIECE, 0)

        def SETUP(self):
            return self.getToken(BoardGameParser.SETUP, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)


        def PLAYER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.PLAYER)
            else:
                return self.getToken(BoardGameParser.PLAYER, i)

        def OBSTACLE(self):
            return self.getToken(BoardGameParser.OBSTACLE, 0)

        def BOOSTER(self):
            return self.getToken(BoardGameParser.BOOSTER, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_board_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoard_statement" ):
                listener.enterBoard_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoard_statement" ):
                listener.exitBoard_statement(self)




    def board_statement(self):

        localctx = BoardGameParser.Board_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_board_statement)
        self._la = 0 # Token type
        try:
            self.state = 614
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 551
                    self.match(BoardGameParser.PLAYER)
                    self.state = 552
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 557
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 558
                self.match(BoardGameParser.PIECE)
                self.state = 562
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 559
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 560
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 561
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 564
                self.match(BoardGameParser.SETUP)
                self.state = 565
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 568
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 566
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 567
                    self.board_pos(0)
                    pass


                self.state = 570
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 576
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 572
                    self.match(BoardGameParser.PLAYER)
                    self.state = 573
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 578
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 579
                self.match(BoardGameParser.OBSTACLE)
                self.state = 583
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                if la_ == 1:
                    self.state = 580
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 581
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 582
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 585
                self.match(BoardGameParser.SETUP)
                self.state = 586
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 589
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 587
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 588
                    self.board_pos(0)
                    pass


                self.state = 591
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 597
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 593
                    self.match(BoardGameParser.PLAYER)
                    self.state = 594
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 599
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 600
                self.match(BoardGameParser.BOOSTER)
                self.state = 604
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 601
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 602
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 603
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 606
                self.match(BoardGameParser.SETUP)
                self.state = 607
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 610
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                if la_ == 1:
                    self.state = 608
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 609
                    self.board_pos(0)
                    pass


                self.state = 612
                self.match(BoardGameParser.CLOSE_PAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obstacle_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBSTACLE(self):
            return self.getToken(BoardGameParser.OBSTACLE, 0)

        def COUNT(self):
            return self.getToken(BoardGameParser.COUNT, 0)

        def int_literal(self):
            return self.getTypedRuleContext(BoardGameParser.Int_literalContext,0)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)

        def ACTION(self):
            return self.getToken(BoardGameParser.ACTION, 0)

        def OPEN_PAR(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.OPEN_PAR)
            else:
                return self.getToken(BoardGameParser.OPEN_PAR, i)

        def param_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Param_listContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Param_listContext,i)


        def CLOSE_PAR(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.CLOSE_PAR)
            else:
                return self.getToken(BoardGameParser.CLOSE_PAR, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.COMMA)
            else:
                return self.getToken(BoardGameParser.COMMA, i)

        def getRuleIndex(self):
            return BoardGameParser.RULE_obstacle_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObstacle_statement" ):
                listener.enterObstacle_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObstacle_statement" ):
                listener.exitObstacle_statement(self)




    def obstacle_statement(self):

        localctx = BoardGameParser.Obstacle_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_obstacle_statement)
        self._la = 0 # Token type
        try:
            self.state = 646
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 616
                self.match(BoardGameParser.OBSTACLE)
                self.state = 620
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 617
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 618
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 619
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 622
                self.match(BoardGameParser.COUNT)
                self.state = 623
                self.int_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 624
                self.match(BoardGameParser.OBSTACLE)
                self.state = 628
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                if la_ == 1:
                    self.state = 625
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 626
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 627
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 630
                self.match(BoardGameParser.ACTION)
                self.state = 631
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 632
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 633
                self.param_list()
                self.state = 634
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 643
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 635
                    self.match(BoardGameParser.COMMA)
                    self.state = 636
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 637
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 638
                    self.param_list()
                    self.state = 639
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 645
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Booster_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOSTER(self):
            return self.getToken(BoardGameParser.BOOSTER, 0)

        def COUNT(self):
            return self.getToken(BoardGameParser.COUNT, 0)

        def int_literal(self):
            return self.getTypedRuleContext(BoardGameParser.Int_literalContext,0)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)

        def ACTION(self):
            return self.getToken(BoardGameParser.ACTION, 0)

        def OPEN_PAR(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.OPEN_PAR)
            else:
                return self.getToken(BoardGameParser.OPEN_PAR, i)

        def param_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Param_listContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Param_listContext,i)


        def CLOSE_PAR(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.CLOSE_PAR)
            else:
                return self.getToken(BoardGameParser.CLOSE_PAR, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.COMMA)
            else:
                return self.getToken(BoardGameParser.COMMA, i)

        def getRuleIndex(self):
            return BoardGameParser.RULE_booster_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooster_statement" ):
                listener.enterBooster_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooster_statement" ):
                listener.exitBooster_statement(self)




    def booster_statement(self):

        localctx = BoardGameParser.Booster_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_booster_statement)
        self._la = 0 # Token type
        try:
            self.state = 678
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 648
                self.match(BoardGameParser.BOOSTER)
                self.state = 652
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 649
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 650
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 651
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 654
                self.match(BoardGameParser.COUNT)
                self.state = 655
                self.int_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 656
                self.match(BoardGameParser.BOOSTER)
                self.state = 660
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                if la_ == 1:
                    self.state = 657
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 658
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 659
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 662
                self.match(BoardGameParser.ACTION)
                self.state = 663
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 664
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 665
                self.param_list()
                self.state = 666
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 675
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 667
                    self.match(BoardGameParser.COMMA)
                    self.state = 668
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 669
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 670
                    self.param_list()
                    self.state = 671
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 677
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Move_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVE(self):
            return self.getToken(BoardGameParser.MOVE, 0)

        def TO(self):
            return self.getToken(BoardGameParser.TO, 0)

        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)


        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_move_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove_statement" ):
                listener.enterMove_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove_statement" ):
                listener.exitMove_statement(self)




    def move_statement(self):

        localctx = BoardGameParser.Move_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_move_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680
            self.match(BoardGameParser.MOVE)
            self.state = 684
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.state = 681
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 682
                self.object_access()
                pass

            elif la_ == 3:
                self.state = 683
                self.match(BoardGameParser.ALL)
                pass


            self.state = 686
            self.match(BoardGameParser.TO)
            self.state = 687
            self.board_pos(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Turn_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TURN(self):
            return self.getToken(BoardGameParser.TURN, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def move_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Move_statementContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_turn_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTurn_statement" ):
                listener.enterTurn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTurn_statement" ):
                listener.exitTurn_statement(self)




    def turn_statement(self):

        localctx = BoardGameParser.Turn_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_turn_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 689
            self.match(BoardGameParser.TURN)
            self.state = 690
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 691
            self.move_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BoardGameParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.COLON)
            else:
                return self.getToken(BoardGameParser.COLON, i)

        def code_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Code_blockContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Code_blockContext,i)


        def ELSE(self):
            return self.getToken(BoardGameParser.ELSE, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = BoardGameParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_if_statement)
        try:
            self.state = 706
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 693
                self.match(BoardGameParser.IF)
                self.state = 694
                self.expression()
                self.state = 695
                self.match(BoardGameParser.COLON)
                self.state = 696
                self.code_block()
                self.state = 697
                self.match(BoardGameParser.ELSE)
                self.state = 698
                self.match(BoardGameParser.COLON)
                self.state = 699
                self.code_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 701
                self.match(BoardGameParser.IF)
                self.state = 702
                self.expression()
                self.state = 703
                self.match(BoardGameParser.COLON)
                self.state = 704
                self.code_block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BoardGameParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def IN(self):
            return self.getToken(BoardGameParser.IN, 0)

        def list_(self):
            return self.getTypedRuleContext(BoardGameParser.ListContext,0)


        def COLON(self):
            return self.getToken(BoardGameParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(BoardGameParser.Code_blockContext,0)


        def END(self):
            return self.getToken(BoardGameParser.END, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)




    def for_statement(self):

        localctx = BoardGameParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 708
            self.match(BoardGameParser.FOR)
            self.state = 709
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 710
            self.match(BoardGameParser.IN)
            self.state = 711
            self.list_()
            self.state = 712
            self.match(BoardGameParser.COLON)
            self.state = 713
            self.code_block()
            self.state = 714
            self.match(BoardGameParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BoardGameParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(BoardGameParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(BoardGameParser.Code_blockContext,0)


        def END(self):
            return self.getToken(BoardGameParser.END, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = BoardGameParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
            self.match(BoardGameParser.WHILE)
            self.state = 717
            self.expression()
            self.state = 718
            self.match(BoardGameParser.COLON)
            self.state = 719
            self.code_block()
            self.state = 720
            self.match(BoardGameParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(BoardGameParser.INPUT, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.STRING_LITERAL)
            else:
                return self.getToken(BoardGameParser.STRING_LITERAL, i)

        def getRuleIndex(self):
            return BoardGameParser.RULE_input_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_statement" ):
                listener.enterInput_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_statement" ):
                listener.exitInput_statement(self)




    def input_statement(self):

        localctx = BoardGameParser.Input_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_input_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
            self.match(BoardGameParser.INPUT)
            self.state = 723
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 727
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==72:
                self.state = 724
                self.match(BoardGameParser.STRING_LITERAL)
                self.state = 729
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 730
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(BoardGameParser.PRINT, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_print_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_statement" ):
                listener.enterPrint_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_statement" ):
                listener.exitPrint_statement(self)




    def print_statement(self):

        localctx = BoardGameParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
            self.match(BoardGameParser.PRINT)
            self.state = 733
            self.match(BoardGameParser.OPEN_PAR)

            self.state = 734
            self.param_list()
            self.state = 735
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BoardGameParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = BoardGameParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 737
            self.match(BoardGameParser.RETURN)
            self.state = 738
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Timer_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIMER(self):
            return self.getToken(BoardGameParser.TIMER, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def POSITIVE_INT_LITERAL(self):
            return self.getToken(BoardGameParser.POSITIVE_INT_LITERAL, 0)

        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_timer_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimer_statement" ):
                listener.enterTimer_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimer_statement" ):
                listener.exitTimer_statement(self)




    def timer_statement(self):

        localctx = BoardGameParser.Timer_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_timer_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 740
            self.match(BoardGameParser.TIMER)
            self.state = 741
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 742
            self.match(BoardGameParser.POSITIVE_INT_LITERAL)
            self.state = 743
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dice_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DICE(self):
            return self.getToken(BoardGameParser.DICE, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def int_literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Int_literalContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Int_literalContext,i)


        def COMMA(self):
            return self.getToken(BoardGameParser.COMMA, 0)

        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_dice_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDice_statement" ):
                listener.enterDice_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDice_statement" ):
                listener.exitDice_statement(self)




    def dice_statement(self):

        localctx = BoardGameParser.Dice_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_dice_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 745
            self.match(BoardGameParser.DICE)
            self.state = 746
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 747
            self.int_literal()
            self.state = 748
            self.match(BoardGameParser.COMMA)
            self.state = 749
            self.int_literal()
            self.state = 750
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Score_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCORE(self):
            return self.getToken(BoardGameParser.SCORE, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)

        def CONDITIONS(self):
            return self.getToken(BoardGameParser.CONDITIONS, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_score_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScore_statement" ):
                listener.enterScore_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScore_statement" ):
                listener.exitScore_statement(self)




    def score_statement(self):

        localctx = BoardGameParser.Score_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_score_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 752
            self.match(BoardGameParser.SCORE)
            self.state = 753
            self.match(BoardGameParser.OPEN_PAR)

            self.state = 754
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 755
            self.match(BoardGameParser.DOT)
            self.state = 756
            self.match(BoardGameParser.CONDITIONS)
            self.state = 758
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.board_pos_sempred
        self._predicates[23] = self.multiplicative_sempred
        self._predicates[24] = self.additive_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def board_pos_sempred(self, localctx:Board_posContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def multiplicative_sempred(self, localctx:MultiplicativeContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def additive_sempred(self, localctx:AdditiveContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




