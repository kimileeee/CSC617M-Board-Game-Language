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
        4,1,75,638,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,4,0,72,8,0,11,0,12,0,73,1,0,1,0,1,1,1,1,1,1,3,1,
        81,8,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,4,3,93,8,3,11,3,12,
        3,94,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,107,8,4,1,5,1,5,
        1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,122,8,7,1,8,1,8,
        1,8,5,8,127,8,8,10,8,12,8,130,9,8,1,8,1,8,1,8,1,8,1,8,5,8,137,8,
        8,10,8,12,8,140,9,8,1,8,1,8,1,8,1,8,1,8,5,8,147,8,8,10,8,12,8,150,
        9,8,1,8,1,8,1,8,5,8,155,8,8,10,8,12,8,158,9,8,1,8,1,8,1,8,5,8,163,
        8,8,10,8,12,8,166,9,8,1,8,1,8,1,8,5,8,171,8,8,10,8,12,8,174,9,8,
        1,8,1,8,1,8,5,8,179,8,8,10,8,12,8,182,9,8,1,8,1,8,1,8,5,8,187,8,
        8,10,8,12,8,190,9,8,1,8,1,8,1,8,5,8,195,8,8,10,8,12,8,198,9,8,3,
        8,200,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,212,
        8,10,10,10,12,10,215,9,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,223,
        8,10,10,10,12,10,226,9,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,234,
        8,10,10,10,12,10,237,9,10,3,10,239,8,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,3,11,250,8,11,1,11,1,11,1,11,5,11,255,8,11,10,
        11,12,11,258,9,11,1,12,1,12,1,12,1,12,1,12,5,12,265,8,12,10,12,12,
        12,268,9,12,1,12,1,12,1,12,1,12,5,12,274,8,12,10,12,12,12,277,9,
        12,1,12,1,12,1,12,1,12,5,12,283,8,12,10,12,12,12,286,9,12,1,12,1,
        12,1,12,1,12,5,12,292,8,12,10,12,12,12,295,9,12,1,12,1,12,1,12,1,
        12,5,12,301,8,12,10,12,12,12,304,9,12,1,12,1,12,1,12,1,12,1,12,5,
        12,311,8,12,10,12,12,12,314,9,12,1,12,1,12,1,12,1,12,5,12,320,8,
        12,10,12,12,12,323,9,12,3,12,325,8,12,1,12,1,12,1,12,1,12,1,12,1,
        12,5,12,333,8,12,10,12,12,12,336,9,12,5,12,338,8,12,10,12,12,12,
        341,9,12,1,13,1,13,1,13,3,13,346,8,13,1,14,1,14,1,14,1,14,1,14,5,
        14,353,8,14,10,14,12,14,356,9,14,1,14,1,14,1,15,1,15,1,15,1,15,1,
        16,1,16,3,16,366,8,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,3,
        17,376,8,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,3,18,394,8,18,1,19,1,19,1,20,1,20,1,
        20,1,20,1,20,1,20,5,20,404,8,20,10,20,12,20,407,9,20,1,21,1,21,1,
        21,1,21,1,21,1,21,5,21,415,8,21,10,21,12,21,418,9,21,1,22,1,22,1,
        23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,3,25,441,8,25,1,26,1,26,1,26,1,26,1,
        26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,3,28,462,8,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,3,28,474,8,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,1,28,5,28,487,8,28,10,28,12,28,490,9,28,1,28,1,28,3,28,494,
        8,28,1,29,1,29,5,29,498,8,29,10,29,12,29,501,9,29,1,29,1,29,1,29,
        1,29,3,29,507,8,29,1,29,1,29,1,29,1,29,3,29,513,8,29,1,29,1,29,1,
        29,1,29,5,29,519,8,29,10,29,12,29,522,9,29,1,29,1,29,1,29,1,29,3,
        29,528,8,29,1,29,1,29,1,29,1,29,3,29,534,8,29,1,29,1,29,1,29,1,29,
        5,29,540,8,29,10,29,12,29,543,9,29,1,29,1,29,1,29,1,29,3,29,549,
        8,29,1,29,1,29,1,29,1,29,3,29,555,8,29,1,29,1,29,3,29,559,8,29,1,
        30,1,30,1,30,1,30,3,30,565,8,30,1,30,1,30,1,30,1,30,1,30,1,30,3,
        30,573,8,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,
        30,5,30,586,8,30,10,30,12,30,589,9,30,3,30,591,8,30,1,31,1,31,1,
        31,1,31,3,31,597,8,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,605,8,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,618,
        8,31,10,31,12,31,621,9,31,3,31,623,8,31,1,32,1,32,1,32,1,32,3,32,
        629,8,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,0,4,22,24,40,42,
        34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,0,7,3,0,3,5,9,12,14,14,1,0,68,
        71,1,0,29,30,2,0,48,48,50,53,1,0,56,57,1,0,54,55,1,0,45,46,708,0,
        68,1,0,0,0,2,77,1,0,0,0,4,86,1,0,0,0,6,92,1,0,0,0,8,106,1,0,0,0,
        10,108,1,0,0,0,12,110,1,0,0,0,14,121,1,0,0,0,16,199,1,0,0,0,18,201,
        1,0,0,0,20,238,1,0,0,0,22,249,1,0,0,0,24,324,1,0,0,0,26,345,1,0,
        0,0,28,347,1,0,0,0,30,359,1,0,0,0,32,365,1,0,0,0,34,375,1,0,0,0,
        36,393,1,0,0,0,38,395,1,0,0,0,40,397,1,0,0,0,42,408,1,0,0,0,44,419,
        1,0,0,0,46,421,1,0,0,0,48,423,1,0,0,0,50,440,1,0,0,0,52,442,1,0,
        0,0,54,447,1,0,0,0,56,493,1,0,0,0,58,558,1,0,0,0,60,590,1,0,0,0,
        62,622,1,0,0,0,64,624,1,0,0,0,66,633,1,0,0,0,68,69,5,1,0,0,69,71,
        5,72,0,0,70,72,3,2,1,0,71,70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,
        73,74,1,0,0,0,74,75,1,0,0,0,75,76,3,4,2,0,76,1,1,0,0,0,77,80,5,2,
        0,0,78,81,5,72,0,0,79,81,3,20,10,0,80,78,1,0,0,0,80,79,1,0,0,0,81,
        82,1,0,0,0,82,83,5,58,0,0,83,84,3,6,3,0,84,85,5,25,0,0,85,3,1,0,
        0,0,86,87,5,24,0,0,87,88,5,58,0,0,88,89,3,6,3,0,89,90,5,25,0,0,90,
        5,1,0,0,0,91,93,3,8,4,0,92,91,1,0,0,0,93,94,1,0,0,0,94,92,1,0,0,
        0,94,95,1,0,0,0,95,7,1,0,0,0,96,107,3,48,24,0,97,107,3,58,29,0,98,
        107,3,50,25,0,99,107,3,52,26,0,100,107,3,54,27,0,101,107,3,56,28,
        0,102,107,3,60,30,0,103,107,3,62,31,0,104,107,3,66,33,0,105,107,
        3,64,32,0,106,96,1,0,0,0,106,97,1,0,0,0,106,98,1,0,0,0,106,99,1,
        0,0,0,106,100,1,0,0,0,106,101,1,0,0,0,106,102,1,0,0,0,106,103,1,
        0,0,0,106,104,1,0,0,0,106,105,1,0,0,0,107,9,1,0,0,0,108,109,7,0,
        0,0,109,11,1,0,0,0,110,111,7,1,0,0,111,13,1,0,0,0,112,122,3,12,6,
        0,113,122,3,20,10,0,114,122,3,18,9,0,115,122,5,72,0,0,116,117,5,
        61,0,0,117,118,3,24,12,0,118,119,5,62,0,0,119,122,1,0,0,0,120,122,
        3,28,14,0,121,112,1,0,0,0,121,113,1,0,0,0,121,114,1,0,0,0,121,115,
        1,0,0,0,121,116,1,0,0,0,121,120,1,0,0,0,122,15,1,0,0,0,123,128,5,
        72,0,0,124,125,5,60,0,0,125,127,3,16,8,0,126,124,1,0,0,0,127,130,
        1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,200,1,0,0,0,130,128,
        1,0,0,0,131,132,5,72,0,0,132,133,5,49,0,0,133,138,3,12,6,0,134,135,
        5,60,0,0,135,137,3,16,8,0,136,134,1,0,0,0,137,140,1,0,0,0,138,136,
        1,0,0,0,138,139,1,0,0,0,139,200,1,0,0,0,140,138,1,0,0,0,141,142,
        5,72,0,0,142,143,5,49,0,0,143,148,3,26,13,0,144,145,5,60,0,0,145,
        147,3,16,8,0,146,144,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,
        149,1,0,0,0,149,200,1,0,0,0,150,148,1,0,0,0,151,156,3,12,6,0,152,
        153,5,60,0,0,153,155,3,16,8,0,154,152,1,0,0,0,155,158,1,0,0,0,156,
        154,1,0,0,0,156,157,1,0,0,0,157,200,1,0,0,0,158,156,1,0,0,0,159,
        164,3,20,10,0,160,161,5,60,0,0,161,163,3,16,8,0,162,160,1,0,0,0,
        163,166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,200,1,0,0,0,
        166,164,1,0,0,0,167,172,5,42,0,0,168,169,5,60,0,0,169,171,3,16,8,
        0,170,168,1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,
        0,173,200,1,0,0,0,174,172,1,0,0,0,175,180,5,41,0,0,176,177,5,60,
        0,0,177,179,3,16,8,0,178,176,1,0,0,0,179,182,1,0,0,0,180,178,1,0,
        0,0,180,181,1,0,0,0,181,200,1,0,0,0,182,180,1,0,0,0,183,188,5,40,
        0,0,184,185,5,60,0,0,185,187,3,16,8,0,186,184,1,0,0,0,187,190,1,
        0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,200,1,0,0,0,190,188,1,
        0,0,0,191,196,3,18,9,0,192,193,5,60,0,0,193,195,3,16,8,0,194,192,
        1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,200,
        1,0,0,0,198,196,1,0,0,0,199,123,1,0,0,0,199,131,1,0,0,0,199,141,
        1,0,0,0,199,151,1,0,0,0,199,159,1,0,0,0,199,167,1,0,0,0,199,175,
        1,0,0,0,199,183,1,0,0,0,199,191,1,0,0,0,200,17,1,0,0,0,201,202,5,
        63,0,0,202,203,3,16,8,0,203,204,5,64,0,0,204,19,1,0,0,0,205,206,
        5,72,0,0,206,207,5,59,0,0,207,213,3,10,5,0,208,209,5,59,0,0,209,
        212,3,10,5,0,210,212,5,72,0,0,211,208,1,0,0,0,211,210,1,0,0,0,212,
        215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,239,1,0,0,0,215,
        213,1,0,0,0,216,217,3,10,5,0,217,218,5,59,0,0,218,224,5,72,0,0,219,
        220,5,59,0,0,220,223,3,10,5,0,221,223,5,72,0,0,222,219,1,0,0,0,222,
        221,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,
        239,1,0,0,0,226,224,1,0,0,0,227,228,5,72,0,0,228,229,5,59,0,0,229,
        235,5,72,0,0,230,231,5,59,0,0,231,234,3,10,5,0,232,234,5,72,0,0,
        233,230,1,0,0,0,233,232,1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,
        235,236,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,238,205,1,0,0,0,
        238,216,1,0,0,0,238,227,1,0,0,0,239,21,1,0,0,0,240,241,6,11,-1,0,
        241,242,5,3,0,0,242,243,5,59,0,0,243,250,5,72,0,0,244,245,5,3,0,
        0,245,246,5,59,0,0,246,247,7,2,0,0,247,248,5,59,0,0,248,250,5,68,
        0,0,249,240,1,0,0,0,249,244,1,0,0,0,250,256,1,0,0,0,251,252,10,1,
        0,0,252,253,5,67,0,0,253,255,3,22,11,2,254,251,1,0,0,0,255,258,1,
        0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,23,1,0,0,0,258,256,1,0,
        0,0,259,260,6,12,-1,0,260,266,3,34,17,0,261,262,3,46,23,0,262,263,
        3,24,12,0,263,265,1,0,0,0,264,261,1,0,0,0,265,268,1,0,0,0,266,264,
        1,0,0,0,266,267,1,0,0,0,267,325,1,0,0,0,268,266,1,0,0,0,269,275,
        3,44,22,0,270,271,3,46,23,0,271,272,3,24,12,0,272,274,1,0,0,0,273,
        270,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,
        325,1,0,0,0,277,275,1,0,0,0,278,284,3,30,15,0,279,280,3,46,23,0,
        280,281,3,24,12,0,281,283,1,0,0,0,282,279,1,0,0,0,283,286,1,0,0,
        0,284,282,1,0,0,0,284,285,1,0,0,0,285,325,1,0,0,0,286,284,1,0,0,
        0,287,293,3,32,16,0,288,289,3,46,23,0,289,290,3,24,12,0,290,292,
        1,0,0,0,291,288,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,
        1,0,0,0,294,325,1,0,0,0,295,293,1,0,0,0,296,302,3,14,7,0,297,298,
        3,46,23,0,298,299,3,24,12,0,299,301,1,0,0,0,300,297,1,0,0,0,301,
        304,1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,325,1,0,0,0,304,
        302,1,0,0,0,305,306,5,47,0,0,306,312,3,24,12,0,307,308,3,46,23,0,
        308,309,3,24,12,0,309,311,1,0,0,0,310,307,1,0,0,0,311,314,1,0,0,
        0,312,310,1,0,0,0,312,313,1,0,0,0,313,325,1,0,0,0,314,312,1,0,0,
        0,315,321,3,64,32,0,316,317,3,46,23,0,317,318,3,24,12,0,318,320,
        1,0,0,0,319,316,1,0,0,0,320,323,1,0,0,0,321,319,1,0,0,0,321,322,
        1,0,0,0,322,325,1,0,0,0,323,321,1,0,0,0,324,259,1,0,0,0,324,269,
        1,0,0,0,324,278,1,0,0,0,324,287,1,0,0,0,324,296,1,0,0,0,324,305,
        1,0,0,0,324,315,1,0,0,0,325,339,1,0,0,0,326,327,10,2,0,0,327,328,
        3,38,19,0,328,334,3,24,12,0,329,330,3,46,23,0,330,331,3,24,12,0,
        331,333,1,0,0,0,332,329,1,0,0,0,333,336,1,0,0,0,334,332,1,0,0,0,
        334,335,1,0,0,0,335,338,1,0,0,0,336,334,1,0,0,0,337,326,1,0,0,0,
        338,341,1,0,0,0,339,337,1,0,0,0,339,340,1,0,0,0,340,25,1,0,0,0,341,
        339,1,0,0,0,342,346,5,72,0,0,343,346,3,20,10,0,344,346,3,22,11,0,
        345,342,1,0,0,0,345,343,1,0,0,0,345,344,1,0,0,0,346,27,1,0,0,0,347,
        348,3,26,13,0,348,349,5,59,0,0,349,350,5,72,0,0,350,354,5,61,0,0,
        351,353,3,16,8,0,352,351,1,0,0,0,353,356,1,0,0,0,354,352,1,0,0,0,
        354,355,1,0,0,0,355,357,1,0,0,0,356,354,1,0,0,0,357,358,5,62,0,0,
        358,29,1,0,0,0,359,360,3,14,7,0,360,361,5,43,0,0,361,362,3,14,7,
        0,362,31,1,0,0,0,363,366,5,72,0,0,364,366,3,20,10,0,365,363,1,0,
        0,0,365,364,1,0,0,0,366,367,1,0,0,0,367,368,5,44,0,0,368,369,3,22,
        11,0,369,33,1,0,0,0,370,376,5,72,0,0,371,372,5,72,0,0,372,373,5,
        61,0,0,373,374,5,72,0,0,374,376,5,62,0,0,375,370,1,0,0,0,375,371,
        1,0,0,0,376,377,1,0,0,0,377,378,5,49,0,0,378,379,3,24,12,0,379,35,
        1,0,0,0,380,381,5,31,0,0,381,382,3,24,12,0,382,383,5,58,0,0,383,
        384,3,6,3,0,384,385,5,32,0,0,385,386,5,58,0,0,386,387,3,6,3,0,387,
        394,1,0,0,0,388,389,5,31,0,0,389,390,3,24,12,0,390,391,5,58,0,0,
        391,392,3,6,3,0,392,394,1,0,0,0,393,380,1,0,0,0,393,388,1,0,0,0,
        394,37,1,0,0,0,395,396,7,3,0,0,396,39,1,0,0,0,397,398,6,20,-1,0,
        398,399,3,14,7,0,399,405,1,0,0,0,400,401,10,2,0,0,401,402,7,4,0,
        0,402,404,3,14,7,0,403,400,1,0,0,0,404,407,1,0,0,0,405,403,1,0,0,
        0,405,406,1,0,0,0,406,41,1,0,0,0,407,405,1,0,0,0,408,409,6,21,-1,
        0,409,410,3,40,20,0,410,416,1,0,0,0,411,412,10,2,0,0,412,413,7,5,
        0,0,413,415,3,40,20,0,414,411,1,0,0,0,415,418,1,0,0,0,416,414,1,
        0,0,0,416,417,1,0,0,0,417,43,1,0,0,0,418,416,1,0,0,0,419,420,3,42,
        21,0,420,45,1,0,0,0,421,422,7,6,0,0,422,47,1,0,0,0,423,424,3,10,
        5,0,424,425,5,61,0,0,425,426,3,16,8,0,426,427,5,62,0,0,427,49,1,
        0,0,0,428,429,5,13,0,0,429,430,5,72,0,0,430,431,5,14,0,0,431,432,
        3,20,10,0,432,433,5,44,0,0,433,434,3,22,11,0,434,441,1,0,0,0,435,
        436,5,15,0,0,436,437,5,61,0,0,437,438,3,18,9,0,438,439,5,62,0,0,
        439,441,1,0,0,0,440,428,1,0,0,0,440,435,1,0,0,0,441,51,1,0,0,0,442,
        443,5,16,0,0,443,444,5,61,0,0,444,445,3,16,8,0,445,446,5,62,0,0,
        446,53,1,0,0,0,447,448,5,17,0,0,448,449,5,72,0,0,449,450,5,61,0,
        0,450,451,3,24,12,0,451,452,5,62,0,0,452,55,1,0,0,0,453,461,5,18,
        0,0,454,462,5,72,0,0,455,462,3,20,10,0,456,462,5,40,0,0,457,458,
        5,61,0,0,458,459,3,16,8,0,459,460,5,62,0,0,460,462,1,0,0,0,461,454,
        1,0,0,0,461,455,1,0,0,0,461,456,1,0,0,0,461,457,1,0,0,0,462,463,
        1,0,0,0,463,464,5,19,0,0,464,494,5,68,0,0,465,473,5,18,0,0,466,474,
        5,72,0,0,467,474,3,20,10,0,468,474,5,40,0,0,469,470,5,61,0,0,470,
        471,3,16,8,0,471,472,5,62,0,0,472,474,1,0,0,0,473,466,1,0,0,0,473,
        467,1,0,0,0,473,468,1,0,0,0,473,469,1,0,0,0,474,475,1,0,0,0,475,
        476,5,20,0,0,476,477,5,72,0,0,477,478,5,61,0,0,478,479,3,16,8,0,
        479,488,5,62,0,0,480,481,5,60,0,0,481,482,5,72,0,0,482,483,5,61,
        0,0,483,484,3,16,8,0,484,485,5,62,0,0,485,487,1,0,0,0,486,480,1,
        0,0,0,487,490,1,0,0,0,488,486,1,0,0,0,488,489,1,0,0,0,489,494,1,
        0,0,0,490,488,1,0,0,0,491,492,5,18,0,0,492,494,3,34,17,0,493,453,
        1,0,0,0,493,465,1,0,0,0,493,491,1,0,0,0,494,57,1,0,0,0,495,496,5,
        13,0,0,496,498,5,72,0,0,497,495,1,0,0,0,498,501,1,0,0,0,499,497,
        1,0,0,0,499,500,1,0,0,0,500,502,1,0,0,0,501,499,1,0,0,0,502,506,
        5,18,0,0,503,507,5,72,0,0,504,507,3,20,10,0,505,507,5,40,0,0,506,
        503,1,0,0,0,506,504,1,0,0,0,506,505,1,0,0,0,507,508,1,0,0,0,508,
        509,5,21,0,0,509,512,5,61,0,0,510,513,3,16,8,0,511,513,3,22,11,0,
        512,510,1,0,0,0,512,511,1,0,0,0,513,514,1,0,0,0,514,515,5,62,0,0,
        515,559,1,0,0,0,516,517,5,13,0,0,517,519,5,72,0,0,518,516,1,0,0,
        0,519,522,1,0,0,0,520,518,1,0,0,0,520,521,1,0,0,0,521,523,1,0,0,
        0,522,520,1,0,0,0,523,527,5,22,0,0,524,528,5,72,0,0,525,528,3,20,
        10,0,526,528,5,40,0,0,527,524,1,0,0,0,527,525,1,0,0,0,527,526,1,
        0,0,0,528,529,1,0,0,0,529,530,5,21,0,0,530,533,5,61,0,0,531,534,
        3,16,8,0,532,534,3,22,11,0,533,531,1,0,0,0,533,532,1,0,0,0,534,535,
        1,0,0,0,535,536,5,62,0,0,536,559,1,0,0,0,537,538,5,13,0,0,538,540,
        5,72,0,0,539,537,1,0,0,0,540,543,1,0,0,0,541,539,1,0,0,0,541,542,
        1,0,0,0,542,544,1,0,0,0,543,541,1,0,0,0,544,548,5,23,0,0,545,549,
        5,72,0,0,546,549,3,20,10,0,547,549,5,40,0,0,548,545,1,0,0,0,548,
        546,1,0,0,0,548,547,1,0,0,0,549,550,1,0,0,0,550,551,5,21,0,0,551,
        554,5,61,0,0,552,555,3,16,8,0,553,555,3,22,11,0,554,552,1,0,0,0,
        554,553,1,0,0,0,555,556,1,0,0,0,556,557,5,62,0,0,557,559,1,0,0,0,
        558,499,1,0,0,0,558,520,1,0,0,0,558,541,1,0,0,0,559,59,1,0,0,0,560,
        564,5,22,0,0,561,565,5,72,0,0,562,565,3,20,10,0,563,565,5,40,0,0,
        564,561,1,0,0,0,564,562,1,0,0,0,564,563,1,0,0,0,565,566,1,0,0,0,
        566,567,5,19,0,0,567,591,5,68,0,0,568,572,5,22,0,0,569,573,5,72,
        0,0,570,573,3,20,10,0,571,573,5,40,0,0,572,569,1,0,0,0,572,570,1,
        0,0,0,572,571,1,0,0,0,573,574,1,0,0,0,574,575,5,20,0,0,575,576,5,
        72,0,0,576,577,5,61,0,0,577,578,3,16,8,0,578,587,5,62,0,0,579,580,
        5,60,0,0,580,581,5,72,0,0,581,582,5,61,0,0,582,583,3,16,8,0,583,
        584,5,62,0,0,584,586,1,0,0,0,585,579,1,0,0,0,586,589,1,0,0,0,587,
        585,1,0,0,0,587,588,1,0,0,0,588,591,1,0,0,0,589,587,1,0,0,0,590,
        560,1,0,0,0,590,568,1,0,0,0,591,61,1,0,0,0,592,596,5,23,0,0,593,
        597,5,72,0,0,594,597,3,20,10,0,595,597,5,40,0,0,596,593,1,0,0,0,
        596,594,1,0,0,0,596,595,1,0,0,0,597,598,1,0,0,0,598,599,5,19,0,0,
        599,623,5,68,0,0,600,604,5,23,0,0,601,605,5,72,0,0,602,605,3,20,
        10,0,603,605,5,40,0,0,604,601,1,0,0,0,604,602,1,0,0,0,604,603,1,
        0,0,0,605,606,1,0,0,0,606,607,5,20,0,0,607,608,5,72,0,0,608,609,
        5,61,0,0,609,610,3,16,8,0,610,619,5,62,0,0,611,612,5,60,0,0,612,
        613,5,72,0,0,613,614,5,61,0,0,614,615,3,16,8,0,615,616,5,62,0,0,
        616,618,1,0,0,0,617,611,1,0,0,0,618,621,1,0,0,0,619,617,1,0,0,0,
        619,620,1,0,0,0,620,623,1,0,0,0,621,619,1,0,0,0,622,592,1,0,0,0,
        622,600,1,0,0,0,623,63,1,0,0,0,624,628,5,26,0,0,625,629,5,72,0,0,
        626,629,3,20,10,0,627,629,5,40,0,0,628,625,1,0,0,0,628,626,1,0,0,
        0,628,627,1,0,0,0,629,630,1,0,0,0,630,631,5,27,0,0,631,632,3,22,
        11,0,632,65,1,0,0,0,633,634,5,28,0,0,634,635,5,72,0,0,635,636,3,
        64,32,0,636,67,1,0,0,0,65,73,80,94,106,121,128,138,148,156,164,172,
        180,188,196,199,211,213,222,224,233,235,238,249,256,266,275,284,
        293,302,312,321,324,334,339,345,354,365,375,393,405,416,440,461,
        473,488,493,499,506,512,520,527,533,541,548,554,558,564,572,587,
        590,596,604,619,622,628
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
                     "'+'", "'-'", "'*'", "'/'", "':'", "'.'", "','", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "'...'" ]

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
                      "SUB_OPT", "MUL_OPT", "DIV_OPT", "COLON", "DOT", "COMMA", 
                      "OPEN_PAR", "CLOSE_PAR", "OPEN_BRACKET", "CLOSE_BRACKET", 
                      "OPEN_BRACE", "CLOSE_BRACE", "ELIPSIS", "INT_LITERAL", 
                      "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "IDENTIFIER", "COMMENT", "WS", "INVALID_IDENTIFIER" ]

    RULE_program = 0
    RULE_define_block = 1
    RULE_gameplay_block = 2
    RULE_code_block = 3
    RULE_statement = 4
    RULE_game_entities = 5
    RULE_literal = 6
    RULE_primary = 7
    RULE_param_list = 8
    RULE_list = 9
    RULE_object_access = 10
    RULE_board_pos = 11
    RULE_expression = 12
    RULE_objects = 13
    RULE_method_call = 14
    RULE_in_expression = 15
    RULE_at_expression = 16
    RULE_assignment_expression = 17
    RULE_if_statement = 18
    RULE_conditional_opt = 19
    RULE_multiplicative = 20
    RULE_additive = 21
    RULE_math_expression = 22
    RULE_logical_opt = 23
    RULE_game_entities_statement = 24
    RULE_player_statement = 25
    RULE_condition_statement = 26
    RULE_rule_statement = 27
    RULE_piece_statement = 28
    RULE_board_statement = 29
    RULE_obstacle_statement = 30
    RULE_booster_statement = 31
    RULE_move_statement = 32
    RULE_turn_statement = 33

    ruleNames =  [ "program", "define_block", "gameplay_block", "code_block", 
                   "statement", "game_entities", "literal", "primary", "param_list", 
                   "list", "object_access", "board_pos", "expression", "objects", 
                   "method_call", "in_expression", "at_expression", "assignment_expression", 
                   "if_statement", "conditional_opt", "multiplicative", 
                   "additive", "math_expression", "logical_opt", "game_entities_statement", 
                   "player_statement", "condition_statement", "rule_statement", 
                   "piece_statement", "board_statement", "obstacle_statement", 
                   "booster_statement", "move_statement", "turn_statement" ]

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
    COLON=58
    DOT=59
    COMMA=60
    OPEN_PAR=61
    CLOSE_PAR=62
    OPEN_BRACKET=63
    CLOSE_BRACKET=64
    OPEN_BRACE=65
    CLOSE_BRACE=66
    ELIPSIS=67
    INT_LITERAL=68
    FLOAT_LITERAL=69
    STRING_LITERAL=70
    BOOLEAN_LITERAL=71
    IDENTIFIER=72
    COMMENT=73
    WS=74
    INVALID_IDENTIFIER=75

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
            self.state = 68
            self.match(BoardGameParser.GAME)
            self.state = 69
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.define_block()
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 75
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
            self.state = 77
            self.match(BoardGameParser.DEFINE)
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 78
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 79
                self.object_access()
                pass


            self.state = 82
            self.match(BoardGameParser.COLON)
            self.state = 83
            self.code_block()
            self.state = 84
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
            self.state = 86
            self.match(BoardGameParser.START)
            self.state = 87
            self.match(BoardGameParser.COLON)
            self.state = 88
            self.code_block()
            self.state = 89
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 91
                self.statement()
                self.state = 94 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 348651064) != 0)):
                    break

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
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.game_entities_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.board_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.player_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self.condition_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 100
                self.rule_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 101
                self.piece_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 102
                self.obstacle_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 103
                self.booster_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 104
                self.turn_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 105
                self.move_statement()
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
            self.state = 108
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24120) != 0)):
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

        def INT_LITERAL(self):
            return self.getToken(BoardGameParser.INT_LITERAL, 0)

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
        self.enterRule(localctx, 12, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 15) != 0)):
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
        self.enterRule(localctx, 14, self.RULE_primary)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.object_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.list_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 115
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 116
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 117
                self.expression(0)
                self.state = 118
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 120
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


        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)

        def literal(self):
            return self.getTypedRuleContext(BoardGameParser.LiteralContext,0)


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
        self.enterRule(localctx, 16, self.RULE_param_list)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 124
                        self.match(BoardGameParser.COMMA)
                        self.state = 125
                        self.param_list() 
                    self.state = 130
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 132
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 133
                self.literal()
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 134
                        self.match(BoardGameParser.COMMA)
                        self.state = 135
                        self.param_list() 
                    self.state = 140
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 142
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 143
                self.objects()
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 144
                        self.match(BoardGameParser.COMMA)
                        self.state = 145
                        self.param_list() 
                    self.state = 150
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.literal()
                self.state = 156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 152
                        self.match(BoardGameParser.COMMA)
                        self.state = 153
                        self.param_list() 
                    self.state = 158
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 159
                self.object_access()
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 160
                        self.match(BoardGameParser.COMMA)
                        self.state = 161
                        self.param_list() 
                    self.state = 166
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 167
                self.match(BoardGameParser.NONE)
                self.state = 172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 168
                        self.match(BoardGameParser.COMMA)
                        self.state = 169
                        self.param_list() 
                    self.state = 174
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 175
                self.match(BoardGameParser.ANY)
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 176
                        self.match(BoardGameParser.COMMA)
                        self.state = 177
                        self.param_list() 
                    self.state = 182
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 183
                self.match(BoardGameParser.ALL)
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 184
                        self.match(BoardGameParser.COMMA)
                        self.state = 185
                        self.param_list() 
                    self.state = 190
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 191
                self.list_()
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 192
                        self.match(BoardGameParser.COMMA)
                        self.state = 193
                        self.param_list() 
                    self.state = 198
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(BoardGameParser.OPEN_BRACKET)
            self.state = 202
            self.param_list()
            self.state = 203
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
        self.enterRule(localctx, 20, self.RULE_object_access)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 206
                self.match(BoardGameParser.DOT)
                self.state = 207
                self.game_entities()
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 211
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [59]:
                            self.state = 208
                            self.match(BoardGameParser.DOT)
                            self.state = 209
                            self.game_entities()
                            pass
                        elif token in [72]:
                            self.state = 210
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 215
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.game_entities()
                self.state = 217
                self.match(BoardGameParser.DOT)
                self.state = 218
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 222
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [59]:
                            self.state = 219
                            self.match(BoardGameParser.DOT)
                            self.state = 220
                            self.game_entities()
                            pass
                        elif token in [72]:
                            self.state = 221
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 226
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 228
                self.match(BoardGameParser.DOT)
                self.state = 229
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 233
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [59]:
                            self.state = 230
                            self.match(BoardGameParser.DOT)
                            self.state = 231
                            self.game_entities()
                            pass
                        elif token in [72]:
                            self.state = 232
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 237
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def INT_LITERAL(self):
            return self.getToken(BoardGameParser.INT_LITERAL, 0)

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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_board_pos, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 241
                self.match(BoardGameParser.BOARD)
                self.state = 242
                self.match(BoardGameParser.DOT)
                self.state = 243
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 244
                self.match(BoardGameParser.BOARD)
                self.state = 245
                self.match(BoardGameParser.DOT)
                self.state = 246
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.match(BoardGameParser.DOT)

                self.state = 248
                self.match(BoardGameParser.INT_LITERAL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.Board_posContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_board_pos)
                    self.state = 251
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 252
                    self.match(BoardGameParser.ELIPSIS)
                    self.state = 253
                    self.board_pos(2) 
                self.state = 258
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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


        def primary(self):
            return self.getTypedRuleContext(BoardGameParser.PrimaryContext,0)


        def NOT_OPT(self):
            return self.getToken(BoardGameParser.NOT_OPT, 0)

        def move_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Move_statementContext,0)


        def conditional_opt(self):
            return self.getTypedRuleContext(BoardGameParser.Conditional_optContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BoardGameParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 260
                self.assignment_expression()
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 261
                        self.logical_opt()
                        self.state = 262
                        self.expression(0) 
                    self.state = 268
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                pass

            elif la_ == 2:
                self.state = 269
                self.math_expression()
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 270
                        self.logical_opt()
                        self.state = 271
                        self.expression(0) 
                    self.state = 277
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass

            elif la_ == 3:
                self.state = 278
                self.in_expression()
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 279
                        self.logical_opt()
                        self.state = 280
                        self.expression(0) 
                    self.state = 286
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                pass

            elif la_ == 4:
                self.state = 287
                self.at_expression()
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 288
                        self.logical_opt()
                        self.state = 289
                        self.expression(0) 
                    self.state = 295
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                pass

            elif la_ == 5:
                self.state = 296
                self.primary()
                self.state = 302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 297
                        self.logical_opt()
                        self.state = 298
                        self.expression(0) 
                    self.state = 304
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                pass

            elif la_ == 6:
                self.state = 305
                self.match(BoardGameParser.NOT_OPT)
                self.state = 306
                self.expression(0)
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 307
                        self.logical_opt()
                        self.state = 308
                        self.expression(0) 
                    self.state = 314
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                pass

            elif la_ == 7:
                self.state = 315
                self.move_statement()
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 316
                        self.logical_opt()
                        self.state = 317
                        self.expression(0) 
                    self.state = 323
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 339
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 326
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 327
                    self.conditional_opt()
                    self.state = 328
                    self.expression(0)
                    self.state = 334
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 329
                            self.logical_opt()
                            self.state = 330
                            self.expression(0) 
                        self.state = 336
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
             
                self.state = 341
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 26, self.RULE_objects)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.object_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 344
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
        self.enterRule(localctx, 28, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.objects()
            self.state = 348
            self.match(BoardGameParser.DOT)
            self.state = 349
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 350
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223364340273357256) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 31) != 0):
                self.state = 351
                self.param_list()
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 357
            self.match(BoardGameParser.CLOSE_PAR)
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
        self.enterRule(localctx, 30, self.RULE_in_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.primary()
            self.state = 360
            self.match(BoardGameParser.IN)
            self.state = 361
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
        self.enterRule(localctx, 32, self.RULE_at_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 363
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 364
                self.object_access()
                pass


            self.state = 367
            self.match(BoardGameParser.AT)
            self.state = 368
            self.board_pos(0)
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
        self.enterRule(localctx, 34, self.RULE_assignment_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 370
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 371
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 372
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 373
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 374
                self.match(BoardGameParser.CLOSE_PAR)
                pass


            self.state = 377
            self.match(BoardGameParser.ASSIGN_OPT)
            self.state = 378
            self.expression(0)
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
        self.enterRule(localctx, 36, self.RULE_if_statement)
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(BoardGameParser.IF)
                self.state = 381
                self.expression(0)
                self.state = 382
                self.match(BoardGameParser.COLON)
                self.state = 383
                self.code_block()
                self.state = 384
                self.match(BoardGameParser.ELSE)
                self.state = 385
                self.match(BoardGameParser.COLON)
                self.state = 386
                self.code_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.match(BoardGameParser.IF)
                self.state = 389
                self.expression(0)
                self.state = 390
                self.match(BoardGameParser.COLON)
                self.state = 391
                self.code_block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 38, self.RULE_conditional_opt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
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


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(BoardGameParser.PrimaryContext,0)


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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_multiplicative, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.primary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.MultiplicativeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    _la = self._input.LA(1)
                    if not(_la==56 or _la==57):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 402
                    self.primary() 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_additive, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.multiplicative(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 416
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.AdditiveContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    _la = self._input.LA(1)
                    if not(_la==54 or _la==55):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 413
                    self.multiplicative(0) 
                self.state = 418
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 44, self.RULE_math_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
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
        self.enterRule(localctx, 46, self.RULE_logical_opt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
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
        self.enterRule(localctx, 48, self.RULE_game_entities_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.game_entities()
            self.state = 424
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 425
            self.param_list()
            self.state = 426
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
        self.enterRule(localctx, 50, self.RULE_player_statement)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(BoardGameParser.PLAYER)
                self.state = 429
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 430
                self.match(BoardGameParser.COLOR)
                self.state = 431
                self.object_access()
                self.state = 432
                self.match(BoardGameParser.AT)
                self.state = 433
                self.board_pos(0)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.match(BoardGameParser.ORDER)
                self.state = 436
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 437
                self.list_()
                self.state = 438
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

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


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
        self.enterRule(localctx, 52, self.RULE_condition_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(BoardGameParser.CONDITION)
            self.state = 443
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 444
            self.param_list()
            self.state = 445
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
        self.enterRule(localctx, 54, self.RULE_rule_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(BoardGameParser.RULE)
            self.state = 448
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 449
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 450
            self.expression(0)
            self.state = 451
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

        def INT_LITERAL(self):
            return self.getToken(BoardGameParser.INT_LITERAL, 0)

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
        self.enterRule(localctx, 56, self.RULE_piece_statement)
        self._la = 0 # Token type
        try:
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(BoardGameParser.PIECE)
                self.state = 461
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 454
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 455
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 456
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 4:
                    self.state = 457
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 458
                    self.param_list()
                    self.state = 459
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 463
                self.match(BoardGameParser.COUNT)
                self.state = 464
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.match(BoardGameParser.PIECE)
                self.state = 473
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 466
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 467
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 468
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 4:
                    self.state = 469
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 470
                    self.param_list()
                    self.state = 471
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 475
                self.match(BoardGameParser.ACTION)
                self.state = 476
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 477
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 478
                self.param_list()
                self.state = 479
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 488
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==60:
                    self.state = 480
                    self.match(BoardGameParser.COMMA)
                    self.state = 481
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 482
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 483
                    self.param_list()
                    self.state = 484
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 490
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 491
                self.match(BoardGameParser.PIECE)
                self.state = 492
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
        self.enterRule(localctx, 58, self.RULE_board_statement)
        self._la = 0 # Token type
        try:
            self.state = 558
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 495
                    self.match(BoardGameParser.PLAYER)
                    self.state = 496
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 501
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 502
                self.match(BoardGameParser.PIECE)
                self.state = 506
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 503
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 504
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 505
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 508
                self.match(BoardGameParser.SETUP)
                self.state = 509
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 512
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                if la_ == 1:
                    self.state = 510
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 511
                    self.board_pos(0)
                    pass


                self.state = 514
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 516
                    self.match(BoardGameParser.PLAYER)
                    self.state = 517
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 522
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 523
                self.match(BoardGameParser.OBSTACLE)
                self.state = 527
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 524
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 525
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 526
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 529
                self.match(BoardGameParser.SETUP)
                self.state = 530
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 533
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 531
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 532
                    self.board_pos(0)
                    pass


                self.state = 535
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 541
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 537
                    self.match(BoardGameParser.PLAYER)
                    self.state = 538
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 543
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 544
                self.match(BoardGameParser.BOOSTER)
                self.state = 548
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 545
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 546
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 547
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 550
                self.match(BoardGameParser.SETUP)
                self.state = 551
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 554
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                if la_ == 1:
                    self.state = 552
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 553
                    self.board_pos(0)
                    pass


                self.state = 556
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

        def INT_LITERAL(self):
            return self.getToken(BoardGameParser.INT_LITERAL, 0)

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
        self.enterRule(localctx, 60, self.RULE_obstacle_statement)
        self._la = 0 # Token type
        try:
            self.state = 590
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self.match(BoardGameParser.OBSTACLE)
                self.state = 564
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 561
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 562
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 563
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 566
                self.match(BoardGameParser.COUNT)
                self.state = 567
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self.match(BoardGameParser.OBSTACLE)
                self.state = 572
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 569
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 570
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 571
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 574
                self.match(BoardGameParser.ACTION)
                self.state = 575
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 576
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 577
                self.param_list()
                self.state = 578
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 587
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==60:
                    self.state = 579
                    self.match(BoardGameParser.COMMA)
                    self.state = 580
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 581
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 582
                    self.param_list()
                    self.state = 583
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 589
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

        def INT_LITERAL(self):
            return self.getToken(BoardGameParser.INT_LITERAL, 0)

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
        self.enterRule(localctx, 62, self.RULE_booster_statement)
        self._la = 0 # Token type
        try:
            self.state = 622
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 592
                self.match(BoardGameParser.BOOSTER)
                self.state = 596
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 593
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 594
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 595
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 598
                self.match(BoardGameParser.COUNT)
                self.state = 599
                self.match(BoardGameParser.INT_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 600
                self.match(BoardGameParser.BOOSTER)
                self.state = 604
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
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
                self.match(BoardGameParser.ACTION)
                self.state = 607
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 608
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 609
                self.param_list()
                self.state = 610
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 619
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==60:
                    self.state = 611
                    self.match(BoardGameParser.COMMA)
                    self.state = 612
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 613
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 614
                    self.param_list()
                    self.state = 615
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 621
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
        self.enterRule(localctx, 64, self.RULE_move_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.match(BoardGameParser.MOVE)
            self.state = 628
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
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
            self.match(BoardGameParser.TO)
            self.state = 631
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
        self.enterRule(localctx, 66, self.RULE_turn_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.match(BoardGameParser.TURN)
            self.state = 634
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 635
            self.move_statement()
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
        self._predicates[11] = self.board_pos_sempred
        self._predicates[12] = self.expression_sempred
        self._predicates[20] = self.multiplicative_sempred
        self._predicates[21] = self.additive_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def board_pos_sempred(self, localctx:Board_posContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplicative_sempred(self, localctx:MultiplicativeContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def additive_sempred(self, localctx:AdditiveContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




