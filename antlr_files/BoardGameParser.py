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
        4,1,79,763,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,1,0,1,0,1,0,4,0,114,8,0,11,0,12,0,115,1,0,1,
        0,1,1,1,1,1,1,3,1,123,8,1,1,1,1,1,1,1,1,1,1,1,3,1,130,8,1,1,2,1,
        2,1,2,1,2,1,2,1,3,4,3,138,8,3,11,3,12,3,139,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,160,8,4,
        1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,3,7,170,8,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,182,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        3,9,224,8,9,3,9,226,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,11,1,11,5,11,238,8,11,10,11,12,11,241,9,11,1,11,1,11,1,11,1,11,
        1,11,1,11,5,11,249,8,11,10,11,12,11,252,9,11,1,11,1,11,1,11,1,11,
        1,11,1,11,5,11,260,8,11,10,11,12,11,263,9,11,3,11,265,8,11,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,279,
        8,12,1,12,1,12,1,12,5,12,284,8,12,10,12,12,12,287,9,12,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,3,14,296,8,14,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,3,15,309,8,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,324,8,16,1,17,
        1,17,1,17,3,17,329,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,19,1,19,1,19,1,19,1,19,5,19,345,8,19,10,19,12,19,348,9,19,
        1,19,1,19,1,20,1,20,1,20,1,20,4,20,356,8,20,11,20,12,20,357,1,20,
        1,20,1,21,1,21,3,21,364,8,21,1,22,1,22,1,22,1,22,5,22,370,8,22,10,
        22,12,22,373,9,22,1,22,1,22,1,22,1,22,3,22,379,8,22,1,23,1,23,1,
        23,1,23,1,24,1,24,3,24,387,8,24,1,24,1,24,1,24,1,25,1,25,1,25,1,
        25,1,25,3,25,397,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,3,26,411,8,26,1,27,1,27,3,27,415,8,27,1,28,1,28,
        1,28,1,28,1,28,3,28,422,8,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,
        1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,441,8,31,
        1,32,3,32,444,8,32,1,32,1,32,1,33,1,33,1,33,5,33,451,8,33,10,33,
        12,33,454,9,33,1,34,1,34,1,34,5,34,459,8,34,10,34,12,34,462,9,34,
        1,35,1,35,1,35,5,35,467,8,35,10,35,12,35,470,9,35,1,36,1,36,1,37,
        1,37,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,5,39,
        487,8,39,10,39,12,39,490,9,39,1,39,1,39,1,39,1,39,1,39,3,39,497,
        8,39,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,42,
        1,42,1,42,1,42,1,42,1,42,1,42,1,42,3,42,518,8,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,1,42,1,42,1,42,3,42,530,8,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,5,42,543,8,42,10,42,12,42,
        546,9,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,3,42,
        558,8,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,
        5,42,571,8,42,10,42,12,42,574,9,42,1,42,1,42,3,42,578,8,42,1,43,
        1,43,1,43,1,43,1,43,1,43,3,43,586,8,43,1,43,1,43,1,43,1,43,3,43,
        592,8,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,3,43,602,8,43,1,
        43,1,43,1,43,1,43,3,43,608,8,43,1,43,1,43,1,43,1,43,1,43,1,43,1,
        43,1,43,3,43,618,8,43,1,43,1,43,1,43,1,43,3,43,624,8,43,1,43,1,43,
        3,43,628,8,43,1,44,1,44,1,44,1,44,3,44,634,8,44,1,44,1,44,1,44,1,
        44,1,44,1,44,3,44,642,8,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,
        44,1,44,1,44,1,44,5,44,655,8,44,10,44,12,44,658,9,44,3,44,660,8,
        44,1,45,1,45,1,45,1,45,3,45,666,8,45,1,45,1,45,1,45,1,45,1,45,1,
        45,3,45,674,8,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,
        45,1,45,5,45,687,8,45,10,45,12,45,690,9,45,3,45,692,8,45,1,46,1,
        46,1,46,1,46,3,46,698,8,46,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,
        48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,3,
        48,720,8,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,50,1,50,1,
        50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,5,51,741,8,51,10,51,12,
        51,744,9,51,1,51,1,51,1,52,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,
        54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,0,1,24,55,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,0,8,4,0,1,1,3,7,9,12,14,14,1,0,71,72,1,0,41,43,1,
        0,29,30,2,0,49,50,52,55,1,0,56,57,1,0,58,59,1,0,46,47,845,0,110,
        1,0,0,0,2,129,1,0,0,0,4,131,1,0,0,0,6,137,1,0,0,0,8,159,1,0,0,0,
        10,161,1,0,0,0,12,163,1,0,0,0,14,169,1,0,0,0,16,181,1,0,0,0,18,225,
        1,0,0,0,20,227,1,0,0,0,22,264,1,0,0,0,24,278,1,0,0,0,26,288,1,0,
        0,0,28,295,1,0,0,0,30,308,1,0,0,0,32,323,1,0,0,0,34,328,1,0,0,0,
        36,330,1,0,0,0,38,339,1,0,0,0,40,351,1,0,0,0,42,363,1,0,0,0,44,378,
        1,0,0,0,46,380,1,0,0,0,48,386,1,0,0,0,50,391,1,0,0,0,52,410,1,0,
        0,0,54,414,1,0,0,0,56,421,1,0,0,0,58,423,1,0,0,0,60,426,1,0,0,0,
        62,440,1,0,0,0,64,443,1,0,0,0,66,447,1,0,0,0,68,455,1,0,0,0,70,463,
        1,0,0,0,72,471,1,0,0,0,74,473,1,0,0,0,76,475,1,0,0,0,78,496,1,0,
        0,0,80,498,1,0,0,0,82,503,1,0,0,0,84,577,1,0,0,0,86,627,1,0,0,0,
        88,659,1,0,0,0,90,691,1,0,0,0,92,693,1,0,0,0,94,702,1,0,0,0,96,719,
        1,0,0,0,98,721,1,0,0,0,100,729,1,0,0,0,102,735,1,0,0,0,104,747,1,
        0,0,0,106,752,1,0,0,0,108,755,1,0,0,0,110,111,5,1,0,0,111,113,5,
        76,0,0,112,114,3,2,1,0,113,112,1,0,0,0,114,115,1,0,0,0,115,113,1,
        0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,118,3,4,2,0,118,1,1,0,
        0,0,119,122,5,2,0,0,120,123,5,76,0,0,121,123,3,22,11,0,122,120,1,
        0,0,0,122,121,1,0,0,0,123,124,1,0,0,0,124,125,5,61,0,0,125,126,3,
        6,3,0,126,127,5,25,0,0,127,130,1,0,0,0,128,130,3,36,18,0,129,119,
        1,0,0,0,129,128,1,0,0,0,130,3,1,0,0,0,131,132,5,24,0,0,132,133,5,
        61,0,0,133,134,3,6,3,0,134,135,5,25,0,0,135,5,1,0,0,0,136,138,3,
        8,4,0,137,136,1,0,0,0,138,139,1,0,0,0,139,137,1,0,0,0,139,140,1,
        0,0,0,140,7,1,0,0,0,141,160,3,76,38,0,142,160,3,86,43,0,143,160,
        3,78,39,0,144,160,3,80,40,0,145,160,3,82,41,0,146,160,3,84,42,0,
        147,160,3,88,44,0,148,160,3,90,45,0,149,160,3,94,47,0,150,160,3,
        92,46,0,151,160,3,108,54,0,152,160,3,28,14,0,153,160,3,96,48,0,154,
        160,3,98,49,0,155,160,3,100,50,0,156,160,3,102,51,0,157,160,3,104,
        52,0,158,160,3,106,53,0,159,141,1,0,0,0,159,142,1,0,0,0,159,143,
        1,0,0,0,159,144,1,0,0,0,159,145,1,0,0,0,159,146,1,0,0,0,159,147,
        1,0,0,0,159,148,1,0,0,0,159,149,1,0,0,0,159,150,1,0,0,0,159,151,
        1,0,0,0,159,152,1,0,0,0,159,153,1,0,0,0,159,154,1,0,0,0,159,155,
        1,0,0,0,159,156,1,0,0,0,159,157,1,0,0,0,159,158,1,0,0,0,160,9,1,
        0,0,0,161,162,7,0,0,0,162,11,1,0,0,0,163,164,7,1,0,0,164,13,1,0,
        0,0,165,170,3,12,6,0,166,170,5,73,0,0,167,170,5,74,0,0,168,170,5,
        75,0,0,169,165,1,0,0,0,169,166,1,0,0,0,169,167,1,0,0,0,169,168,1,
        0,0,0,170,15,1,0,0,0,171,182,3,14,7,0,172,182,3,20,10,0,173,182,
        5,76,0,0,174,182,3,22,11,0,175,176,5,64,0,0,176,177,3,28,14,0,177,
        178,5,65,0,0,178,182,1,0,0,0,179,182,3,38,19,0,180,182,3,30,15,0,
        181,171,1,0,0,0,181,172,1,0,0,0,181,173,1,0,0,0,181,174,1,0,0,0,
        181,175,1,0,0,0,181,179,1,0,0,0,181,180,1,0,0,0,182,17,1,0,0,0,183,
        184,5,7,0,0,184,185,5,64,0,0,185,186,5,76,0,0,186,187,5,62,0,0,187,
        188,5,5,0,0,188,226,5,65,0,0,189,190,7,2,0,0,190,191,5,63,0,0,191,
        226,3,18,9,0,192,193,3,52,26,0,193,194,5,63,0,0,194,195,3,18,9,0,
        195,226,1,0,0,0,196,197,3,14,7,0,197,198,5,63,0,0,198,199,3,18,9,
        0,199,226,1,0,0,0,200,201,5,76,0,0,201,202,5,63,0,0,202,226,3,18,
        9,0,203,204,3,24,12,0,204,205,5,63,0,0,205,206,3,18,9,0,206,226,
        1,0,0,0,207,208,3,22,11,0,208,209,5,63,0,0,209,210,3,18,9,0,210,
        226,1,0,0,0,211,212,3,20,10,0,212,213,5,63,0,0,213,214,3,18,9,0,
        214,226,1,0,0,0,215,224,5,41,0,0,216,224,5,42,0,0,217,224,5,43,0,
        0,218,224,5,76,0,0,219,224,3,14,7,0,220,224,3,22,11,0,221,224,3,
        20,10,0,222,224,3,24,12,0,223,215,1,0,0,0,223,216,1,0,0,0,223,217,
        1,0,0,0,223,218,1,0,0,0,223,219,1,0,0,0,223,220,1,0,0,0,223,221,
        1,0,0,0,223,222,1,0,0,0,224,226,1,0,0,0,225,183,1,0,0,0,225,189,
        1,0,0,0,225,192,1,0,0,0,225,196,1,0,0,0,225,200,1,0,0,0,225,203,
        1,0,0,0,225,207,1,0,0,0,225,211,1,0,0,0,225,223,1,0,0,0,226,19,1,
        0,0,0,227,228,5,66,0,0,228,229,3,18,9,0,229,230,5,67,0,0,230,21,
        1,0,0,0,231,232,5,76,0,0,232,233,5,62,0,0,233,239,3,10,5,0,234,235,
        5,62,0,0,235,238,3,10,5,0,236,238,5,76,0,0,237,234,1,0,0,0,237,236,
        1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,265,
        1,0,0,0,241,239,1,0,0,0,242,243,3,10,5,0,243,244,5,62,0,0,244,250,
        5,76,0,0,245,246,5,62,0,0,246,249,3,10,5,0,247,249,5,76,0,0,248,
        245,1,0,0,0,248,247,1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,250,
        251,1,0,0,0,251,265,1,0,0,0,252,250,1,0,0,0,253,254,5,76,0,0,254,
        255,5,62,0,0,255,261,5,76,0,0,256,257,5,62,0,0,257,260,3,10,5,0,
        258,260,5,76,0,0,259,256,1,0,0,0,259,258,1,0,0,0,260,263,1,0,0,0,
        261,259,1,0,0,0,261,262,1,0,0,0,262,265,1,0,0,0,263,261,1,0,0,0,
        264,231,1,0,0,0,264,242,1,0,0,0,264,253,1,0,0,0,265,23,1,0,0,0,266,
        267,6,12,-1,0,267,268,5,3,0,0,268,269,5,62,0,0,269,279,5,76,0,0,
        270,271,5,3,0,0,271,272,5,62,0,0,272,273,7,3,0,0,273,274,5,62,0,
        0,274,279,3,12,6,0,275,276,5,3,0,0,276,277,5,62,0,0,277,279,3,12,
        6,0,278,266,1,0,0,0,278,270,1,0,0,0,278,275,1,0,0,0,279,285,1,0,
        0,0,280,281,10,1,0,0,281,282,5,70,0,0,282,284,3,24,12,2,283,280,
        1,0,0,0,284,287,1,0,0,0,285,283,1,0,0,0,285,286,1,0,0,0,286,25,1,
        0,0,0,287,285,1,0,0,0,288,289,7,4,0,0,289,27,1,0,0,0,290,291,3,32,
        16,0,291,292,3,74,37,0,292,293,3,28,14,0,293,296,1,0,0,0,294,296,
        3,32,16,0,295,290,1,0,0,0,295,294,1,0,0,0,296,29,1,0,0,0,297,298,
        3,10,5,0,298,299,5,62,0,0,299,300,5,19,0,0,300,309,1,0,0,0,301,302,
        5,76,0,0,302,303,5,62,0,0,303,309,5,19,0,0,304,305,3,22,11,0,305,
        306,5,62,0,0,306,307,5,19,0,0,307,309,1,0,0,0,308,297,1,0,0,0,308,
        301,1,0,0,0,308,304,1,0,0,0,309,31,1,0,0,0,310,324,3,16,8,0,311,
        324,3,52,26,0,312,324,3,72,36,0,313,324,3,46,23,0,314,324,3,48,24,
        0,315,324,3,44,22,0,316,324,3,92,46,0,317,318,3,50,25,0,318,319,
        3,28,14,0,319,324,1,0,0,0,320,321,5,48,0,0,321,324,3,28,14,0,322,
        324,3,30,15,0,323,310,1,0,0,0,323,311,1,0,0,0,323,312,1,0,0,0,323,
        313,1,0,0,0,323,314,1,0,0,0,323,315,1,0,0,0,323,316,1,0,0,0,323,
        317,1,0,0,0,323,320,1,0,0,0,323,322,1,0,0,0,324,33,1,0,0,0,325,329,
        5,76,0,0,326,329,3,24,12,0,327,329,3,22,11,0,328,325,1,0,0,0,328,
        326,1,0,0,0,328,327,1,0,0,0,329,35,1,0,0,0,330,331,5,2,0,0,331,332,
        5,76,0,0,332,333,5,64,0,0,333,334,3,18,9,0,334,335,5,65,0,0,335,
        336,5,61,0,0,336,337,3,6,3,0,337,338,5,25,0,0,338,37,1,0,0,0,339,
        340,3,34,17,0,340,341,5,62,0,0,341,342,5,76,0,0,342,346,5,64,0,0,
        343,345,3,18,9,0,344,343,1,0,0,0,345,348,1,0,0,0,346,344,1,0,0,0,
        346,347,1,0,0,0,347,349,1,0,0,0,348,346,1,0,0,0,349,350,5,65,0,0,
        350,39,1,0,0,0,351,352,5,2,0,0,352,353,5,76,0,0,353,355,5,61,0,0,
        354,356,3,42,21,0,355,354,1,0,0,0,356,357,1,0,0,0,357,355,1,0,0,
        0,357,358,1,0,0,0,358,359,1,0,0,0,359,360,5,25,0,0,360,41,1,0,0,
        0,361,364,3,52,26,0,362,364,3,36,18,0,363,361,1,0,0,0,363,362,1,
        0,0,0,364,43,1,0,0,0,365,371,3,70,35,0,366,367,3,26,13,0,367,368,
        3,70,35,0,368,370,1,0,0,0,369,366,1,0,0,0,370,373,1,0,0,0,371,369,
        1,0,0,0,371,372,1,0,0,0,372,379,1,0,0,0,373,371,1,0,0,0,374,375,
        3,16,8,0,375,376,3,26,13,0,376,377,3,16,8,0,377,379,1,0,0,0,378,
        365,1,0,0,0,378,374,1,0,0,0,379,45,1,0,0,0,380,381,3,16,8,0,381,
        382,5,44,0,0,382,383,3,16,8,0,383,47,1,0,0,0,384,387,5,76,0,0,385,
        387,3,22,11,0,386,384,1,0,0,0,386,385,1,0,0,0,387,388,1,0,0,0,388,
        389,5,45,0,0,389,390,3,24,12,0,390,49,1,0,0,0,391,396,5,42,0,0,392,
        397,5,76,0,0,393,397,3,22,11,0,394,397,3,20,10,0,395,397,3,10,5,
        0,396,392,1,0,0,0,396,393,1,0,0,0,396,394,1,0,0,0,396,395,1,0,0,
        0,397,51,1,0,0,0,398,399,5,76,0,0,399,400,5,51,0,0,400,411,3,28,
        14,0,401,402,5,76,0,0,402,403,5,51,0,0,403,411,3,60,30,0,404,405,
        5,76,0,0,405,406,5,51,0,0,406,411,3,38,19,0,407,408,5,76,0,0,408,
        409,5,51,0,0,409,411,3,102,51,0,410,398,1,0,0,0,410,401,1,0,0,0,
        410,404,1,0,0,0,410,407,1,0,0,0,411,53,1,0,0,0,412,415,3,44,22,0,
        413,415,3,58,29,0,414,412,1,0,0,0,414,413,1,0,0,0,415,55,1,0,0,0,
        416,417,3,54,27,0,417,418,3,74,37,0,418,419,3,56,28,0,419,422,1,
        0,0,0,420,422,3,54,27,0,421,416,1,0,0,0,421,420,1,0,0,0,422,57,1,
        0,0,0,423,424,5,48,0,0,424,425,3,44,22,0,425,59,1,0,0,0,426,427,
        5,31,0,0,427,428,5,64,0,0,428,429,3,56,28,0,429,430,5,65,0,0,430,
        61,1,0,0,0,431,432,5,64,0,0,432,433,3,56,28,0,433,434,5,65,0,0,434,
        441,1,0,0,0,435,441,3,12,6,0,436,441,5,73,0,0,437,441,5,75,0,0,438,
        441,5,76,0,0,439,441,3,22,11,0,440,431,1,0,0,0,440,435,1,0,0,0,440,
        436,1,0,0,0,440,437,1,0,0,0,440,438,1,0,0,0,440,439,1,0,0,0,441,
        63,1,0,0,0,442,444,7,5,0,0,443,442,1,0,0,0,443,444,1,0,0,0,444,445,
        1,0,0,0,445,446,3,62,31,0,446,65,1,0,0,0,447,452,3,64,32,0,448,449,
        5,60,0,0,449,451,3,64,32,0,450,448,1,0,0,0,451,454,1,0,0,0,452,450,
        1,0,0,0,452,453,1,0,0,0,453,67,1,0,0,0,454,452,1,0,0,0,455,460,3,
        66,33,0,456,457,7,6,0,0,457,459,3,66,33,0,458,456,1,0,0,0,459,462,
        1,0,0,0,460,458,1,0,0,0,460,461,1,0,0,0,461,69,1,0,0,0,462,460,1,
        0,0,0,463,468,3,68,34,0,464,465,7,5,0,0,465,467,3,68,34,0,466,464,
        1,0,0,0,467,470,1,0,0,0,468,466,1,0,0,0,468,469,1,0,0,0,469,71,1,
        0,0,0,470,468,1,0,0,0,471,472,3,70,35,0,472,73,1,0,0,0,473,474,7,
        7,0,0,474,75,1,0,0,0,475,476,3,10,5,0,476,477,5,64,0,0,477,478,3,
        18,9,0,478,479,5,65,0,0,479,77,1,0,0,0,480,481,5,13,0,0,481,482,
        5,76,0,0,482,483,5,14,0,0,483,488,3,22,11,0,484,485,5,45,0,0,485,
        487,3,24,12,0,486,484,1,0,0,0,487,490,1,0,0,0,488,486,1,0,0,0,488,
        489,1,0,0,0,489,497,1,0,0,0,490,488,1,0,0,0,491,492,5,15,0,0,492,
        493,5,64,0,0,493,494,3,20,10,0,494,495,5,65,0,0,495,497,1,0,0,0,
        496,480,1,0,0,0,496,491,1,0,0,0,497,79,1,0,0,0,498,499,5,16,0,0,
        499,500,5,64,0,0,500,501,3,28,14,0,501,502,5,65,0,0,502,81,1,0,0,
        0,503,504,5,17,0,0,504,505,5,76,0,0,505,506,5,64,0,0,506,507,3,28,
        14,0,507,508,5,65,0,0,508,83,1,0,0,0,509,517,5,18,0,0,510,518,5,
        76,0,0,511,518,3,22,11,0,512,518,5,41,0,0,513,514,5,64,0,0,514,515,
        3,18,9,0,515,516,5,65,0,0,516,518,1,0,0,0,517,510,1,0,0,0,517,511,
        1,0,0,0,517,512,1,0,0,0,517,513,1,0,0,0,518,519,1,0,0,0,519,520,
        5,19,0,0,520,578,3,12,6,0,521,529,5,18,0,0,522,530,5,76,0,0,523,
        530,3,22,11,0,524,530,5,41,0,0,525,526,5,64,0,0,526,527,3,18,9,0,
        527,528,5,65,0,0,528,530,1,0,0,0,529,522,1,0,0,0,529,523,1,0,0,0,
        529,524,1,0,0,0,529,525,1,0,0,0,530,531,1,0,0,0,531,532,5,20,0,0,
        532,533,5,76,0,0,533,534,5,64,0,0,534,535,3,18,9,0,535,544,5,65,
        0,0,536,537,5,63,0,0,537,538,5,76,0,0,538,539,5,64,0,0,539,540,3,
        18,9,0,540,541,5,65,0,0,541,543,1,0,0,0,542,536,1,0,0,0,543,546,
        1,0,0,0,544,542,1,0,0,0,544,545,1,0,0,0,545,578,1,0,0,0,546,544,
        1,0,0,0,547,557,5,18,0,0,548,558,5,76,0,0,549,558,3,22,11,0,550,
        558,5,41,0,0,551,552,5,64,0,0,552,553,3,18,9,0,553,554,5,65,0,0,
        554,558,1,0,0,0,555,558,5,42,0,0,556,558,5,43,0,0,557,548,1,0,0,
        0,557,549,1,0,0,0,557,550,1,0,0,0,557,551,1,0,0,0,557,555,1,0,0,
        0,557,556,1,0,0,0,558,559,1,0,0,0,559,560,5,20,0,0,560,561,5,76,
        0,0,561,562,5,64,0,0,562,563,3,28,14,0,563,572,5,65,0,0,564,565,
        5,63,0,0,565,566,5,76,0,0,566,567,5,64,0,0,567,568,3,28,14,0,568,
        569,5,65,0,0,569,571,1,0,0,0,570,564,1,0,0,0,571,574,1,0,0,0,572,
        570,1,0,0,0,572,573,1,0,0,0,573,578,1,0,0,0,574,572,1,0,0,0,575,
        576,5,18,0,0,576,578,3,52,26,0,577,509,1,0,0,0,577,521,1,0,0,0,577,
        547,1,0,0,0,577,575,1,0,0,0,578,85,1,0,0,0,579,580,5,13,0,0,580,
        581,5,76,0,0,581,585,5,18,0,0,582,586,5,76,0,0,583,586,3,22,11,0,
        584,586,5,41,0,0,585,582,1,0,0,0,585,583,1,0,0,0,585,584,1,0,0,0,
        586,587,1,0,0,0,587,588,5,21,0,0,588,591,5,64,0,0,589,592,3,18,9,
        0,590,592,3,24,12,0,591,589,1,0,0,0,591,590,1,0,0,0,592,593,1,0,
        0,0,593,594,5,65,0,0,594,628,1,0,0,0,595,596,5,13,0,0,596,597,5,
        76,0,0,597,601,5,22,0,0,598,602,5,76,0,0,599,602,3,22,11,0,600,602,
        5,41,0,0,601,598,1,0,0,0,601,599,1,0,0,0,601,600,1,0,0,0,602,603,
        1,0,0,0,603,604,5,21,0,0,604,607,5,64,0,0,605,608,3,18,9,0,606,608,
        3,24,12,0,607,605,1,0,0,0,607,606,1,0,0,0,608,609,1,0,0,0,609,610,
        5,65,0,0,610,628,1,0,0,0,611,612,5,13,0,0,612,613,5,76,0,0,613,617,
        5,23,0,0,614,618,5,76,0,0,615,618,3,22,11,0,616,618,5,41,0,0,617,
        614,1,0,0,0,617,615,1,0,0,0,617,616,1,0,0,0,618,619,1,0,0,0,619,
        620,5,21,0,0,620,623,5,64,0,0,621,624,3,18,9,0,622,624,3,24,12,0,
        623,621,1,0,0,0,623,622,1,0,0,0,624,625,1,0,0,0,625,626,5,65,0,0,
        626,628,1,0,0,0,627,579,1,0,0,0,627,595,1,0,0,0,627,611,1,0,0,0,
        628,87,1,0,0,0,629,633,5,22,0,0,630,634,5,76,0,0,631,634,3,22,11,
        0,632,634,5,41,0,0,633,630,1,0,0,0,633,631,1,0,0,0,633,632,1,0,0,
        0,634,635,1,0,0,0,635,636,5,19,0,0,636,660,3,12,6,0,637,641,5,22,
        0,0,638,642,5,76,0,0,639,642,3,22,11,0,640,642,5,41,0,0,641,638,
        1,0,0,0,641,639,1,0,0,0,641,640,1,0,0,0,642,643,1,0,0,0,643,644,
        5,20,0,0,644,645,5,76,0,0,645,646,5,64,0,0,646,647,3,18,9,0,647,
        656,5,65,0,0,648,649,5,63,0,0,649,650,5,76,0,0,650,651,5,64,0,0,
        651,652,3,18,9,0,652,653,5,65,0,0,653,655,1,0,0,0,654,648,1,0,0,
        0,655,658,1,0,0,0,656,654,1,0,0,0,656,657,1,0,0,0,657,660,1,0,0,
        0,658,656,1,0,0,0,659,629,1,0,0,0,659,637,1,0,0,0,660,89,1,0,0,0,
        661,665,5,23,0,0,662,666,5,76,0,0,663,666,3,22,11,0,664,666,5,41,
        0,0,665,662,1,0,0,0,665,663,1,0,0,0,665,664,1,0,0,0,666,667,1,0,
        0,0,667,668,5,19,0,0,668,692,3,12,6,0,669,673,5,23,0,0,670,674,5,
        76,0,0,671,674,3,22,11,0,672,674,5,41,0,0,673,670,1,0,0,0,673,671,
        1,0,0,0,673,672,1,0,0,0,674,675,1,0,0,0,675,676,5,20,0,0,676,677,
        5,76,0,0,677,678,5,64,0,0,678,679,3,18,9,0,679,688,5,65,0,0,680,
        681,5,63,0,0,681,682,5,76,0,0,682,683,5,64,0,0,683,684,3,18,9,0,
        684,685,5,65,0,0,685,687,1,0,0,0,686,680,1,0,0,0,687,690,1,0,0,0,
        688,686,1,0,0,0,688,689,1,0,0,0,689,692,1,0,0,0,690,688,1,0,0,0,
        691,661,1,0,0,0,691,669,1,0,0,0,692,91,1,0,0,0,693,697,5,26,0,0,
        694,698,5,76,0,0,695,698,3,22,11,0,696,698,5,41,0,0,697,694,1,0,
        0,0,697,695,1,0,0,0,697,696,1,0,0,0,698,699,1,0,0,0,699,700,5,27,
        0,0,700,701,3,24,12,0,701,93,1,0,0,0,702,703,5,28,0,0,703,704,5,
        76,0,0,704,705,3,92,46,0,705,95,1,0,0,0,706,707,5,32,0,0,707,708,
        3,28,14,0,708,709,5,61,0,0,709,710,3,6,3,0,710,711,5,33,0,0,711,
        712,5,61,0,0,712,713,3,6,3,0,713,720,1,0,0,0,714,715,5,32,0,0,715,
        716,3,28,14,0,716,717,5,61,0,0,717,718,3,6,3,0,718,720,1,0,0,0,719,
        706,1,0,0,0,719,714,1,0,0,0,720,97,1,0,0,0,721,722,5,34,0,0,722,
        723,5,76,0,0,723,724,5,44,0,0,724,725,3,20,10,0,725,726,5,61,0,0,
        726,727,3,6,3,0,727,728,5,25,0,0,728,99,1,0,0,0,729,730,5,35,0,0,
        730,731,3,28,14,0,731,732,5,61,0,0,732,733,3,6,3,0,733,734,5,25,
        0,0,734,101,1,0,0,0,735,736,5,76,0,0,736,737,5,51,0,0,737,738,5,
        36,0,0,738,742,5,64,0,0,739,741,5,74,0,0,740,739,1,0,0,0,741,744,
        1,0,0,0,742,740,1,0,0,0,742,743,1,0,0,0,743,745,1,0,0,0,744,742,
        1,0,0,0,745,746,5,65,0,0,746,103,1,0,0,0,747,748,5,37,0,0,748,749,
        5,64,0,0,749,750,3,18,9,0,750,751,5,65,0,0,751,105,1,0,0,0,752,753,
        5,38,0,0,753,754,3,28,14,0,754,107,1,0,0,0,755,756,5,8,0,0,756,757,
        5,64,0,0,757,758,3,12,6,0,758,759,5,63,0,0,759,760,3,12,6,0,760,
        761,5,65,0,0,761,109,1,0,0,0,63,115,122,129,139,159,169,181,223,
        225,237,239,248,250,259,261,264,278,285,295,308,323,328,346,357,
        363,371,378,386,396,410,414,421,440,443,452,460,468,488,496,517,
        529,544,557,572,577,585,591,601,607,617,623,627,633,641,656,659,
        665,673,688,691,697,719,742
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
                     "'COLUMN'", "'EVALUATE'", "'IF'", "'ELSE'", "'FOR'", 
                     "'WHILE'", "'INPUT'", "'PRINT'", "'RETURN'", "'BREAK'", 
                     "'ERROR'", "'ALL'", "'ANY'", "'NONE'", "'IN'", "'AT'", 
                     "'AND'", "'OR'", "'NOT'", "'=='", "'!='", "'='", "'<'", 
                     "'<='", "'>'", "'>='", "'+'", "'-'", "'*'", "'/'", 
                     "'^'", "':'", "'.'", "','", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "'...'" ]

    symbolicNames = [ "<INVALID>", "GAME", "DEFINE", "BOARD", "PLAYERS", 
                      "CONDITIONS", "TIMER", "SCORE", "DICE", "RULES", "PIECES", 
                      "OBSTACLES", "BOOSTERS", "PLAYER", "COLOR", "ORDER", 
                      "CONDITION", "RULE", "PIECE", "COUNT", "ACTION", "SETUP", 
                      "OBSTACLE", "BOOSTER", "START", "END", "MOVE", "TO", 
                      "TURN", "ROW", "COLUMN", "EVALUATE", "IF", "ELSE", 
                      "FOR", "WHILE", "INPUT", "PRINT", "RETURN", "BREAK", 
                      "ERROR", "ALL", "ANY", "NONE", "IN", "AT", "AND_OPT", 
                      "OR_OPT", "NOT_OPT", "EQUAL_OPT", "NOT_EQUAL_OPT", 
                      "ASSIGN_OPT", "LESS_THAN_OPT", "LESS_EQUAL_OPT", "GREATER_THAN_OPT", 
                      "GREATER_EQUAL_OPT", "ADD_OPT", "SUB_OPT", "MUL_OPT", 
                      "DIV_OPT", "EXP_OPT", "COLON", "DOT", "COMMA", "OPEN_PAR", 
                      "CLOSE_PAR", "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", 
                      "CLOSE_BRACE", "ELIPSIS", "POSITIVE_INT_LITERAL", 
                      "NEGATIVE_INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "BOOLEAN_LITERAL", "IDENTIFIER", "COMMENT", "WS", 
                      "INVALID_IDENTIFIER" ]

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
    RULE_entity_count_expression = 15
    RULE_base_expression = 16
    RULE_objects = 17
    RULE_method_declaration = 18
    RULE_method_call = 19
    RULE_class_define_block = 20
    RULE_class_statement = 21
    RULE_conditional_expression = 22
    RULE_in_expression = 23
    RULE_at_expression = 24
    RULE_any_expression = 25
    RULE_assignment_expression = 26
    RULE_eval_base_expressions = 27
    RULE_eval_expression = 28
    RULE_not_expression = 29
    RULE_evaluate_statement = 30
    RULE_primary_eval = 31
    RULE_unary = 32
    RULE_exponent = 33
    RULE_multiplicative = 34
    RULE_additive = 35
    RULE_math_expression = 36
    RULE_logical_opt = 37
    RULE_game_entities_statement = 38
    RULE_player_statement = 39
    RULE_condition_statement = 40
    RULE_rule_statement = 41
    RULE_piece_statement = 42
    RULE_board_statement = 43
    RULE_obstacle_statement = 44
    RULE_booster_statement = 45
    RULE_move_statement = 46
    RULE_turn_statement = 47
    RULE_if_statement = 48
    RULE_for_statement = 49
    RULE_while_statement = 50
    RULE_input_statement = 51
    RULE_print_statement = 52
    RULE_return_statement = 53
    RULE_dice_statement = 54

    ruleNames =  [ "program", "define_block", "gameplay_block", "code_block", 
                   "statement", "game_entities", "int_literal", "literal", 
                   "primary", "param_list", "list", "object_access", "board_pos", 
                   "conditional_opt", "expression", "entity_count_expression", 
                   "base_expression", "objects", "method_declaration", "method_call", 
                   "class_define_block", "class_statement", "conditional_expression", 
                   "in_expression", "at_expression", "any_expression", "assignment_expression", 
                   "eval_base_expressions", "eval_expression", "not_expression", 
                   "evaluate_statement", "primary_eval", "unary", "exponent", 
                   "multiplicative", "additive", "math_expression", "logical_opt", 
                   "game_entities_statement", "player_statement", "condition_statement", 
                   "rule_statement", "piece_statement", "board_statement", 
                   "obstacle_statement", "booster_statement", "move_statement", 
                   "turn_statement", "if_statement", "for_statement", "while_statement", 
                   "input_statement", "print_statement", "return_statement", 
                   "dice_statement" ]

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
    EVALUATE=31
    IF=32
    ELSE=33
    FOR=34
    WHILE=35
    INPUT=36
    PRINT=37
    RETURN=38
    BREAK=39
    ERROR=40
    ALL=41
    ANY=42
    NONE=43
    IN=44
    AT=45
    AND_OPT=46
    OR_OPT=47
    NOT_OPT=48
    EQUAL_OPT=49
    NOT_EQUAL_OPT=50
    ASSIGN_OPT=51
    LESS_THAN_OPT=52
    LESS_EQUAL_OPT=53
    GREATER_THAN_OPT=54
    GREATER_EQUAL_OPT=55
    ADD_OPT=56
    SUB_OPT=57
    MUL_OPT=58
    DIV_OPT=59
    EXP_OPT=60
    COLON=61
    DOT=62
    COMMA=63
    OPEN_PAR=64
    CLOSE_PAR=65
    OPEN_BRACKET=66
    CLOSE_BRACKET=67
    OPEN_BRACE=68
    CLOSE_BRACE=69
    ELIPSIS=70
    POSITIVE_INT_LITERAL=71
    NEGATIVE_INT_LITERAL=72
    FLOAT_LITERAL=73
    STRING_LITERAL=74
    BOOLEAN_LITERAL=75
    IDENTIFIER=76
    COMMENT=77
    WS=78
    INVALID_IDENTIFIER=79

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BoardGameParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(BoardGameParser.GAME)
            self.state = 111
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 113 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self.define_block()
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 117
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


        def getRuleIndex(self):
            return BoardGameParser.RULE_define_block

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DefineContext(Define_blockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Define_blockContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine" ):
                listener.enterDefine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine" ):
                listener.exitDefine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine" ):
                return visitor.visitDefine(self)
            else:
                return visitor.visitChildren(self)


    class MethodDeclarationContext(Define_blockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Define_blockContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def method_declaration(self):
            return self.getTypedRuleContext(BoardGameParser.Method_declarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def define_block(self):

        localctx = BoardGameParser.Define_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_define_block)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = BoardGameParser.DefineContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(BoardGameParser.DEFINE)
                self.state = 122
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 120
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 121
                    self.object_access()
                    pass


                self.state = 124
                self.match(BoardGameParser.COLON)
                self.state = 125
                self.code_block()
                self.state = 126
                self.match(BoardGameParser.END)
                pass

            elif la_ == 2:
                localctx = BoardGameParser.MethodDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.method_declaration()
                pass


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


        def getRuleIndex(self):
            return BoardGameParser.RULE_gameplay_block

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GameplayContext(Gameplay_blockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Gameplay_blockContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def START(self):
            return self.getToken(BoardGameParser.START, 0)
        def COLON(self):
            return self.getToken(BoardGameParser.COLON, 0)
        def code_block(self):
            return self.getTypedRuleContext(BoardGameParser.Code_blockContext,0)

        def END(self):
            return self.getToken(BoardGameParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGameplay" ):
                listener.enterGameplay(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGameplay" ):
                listener.exitGameplay(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGameplay" ):
                return visitor.visitGameplay(self)
            else:
                return visitor.visitChildren(self)



    def gameplay_block(self):

        localctx = BoardGameParser.Gameplay_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_gameplay_block)
        try:
            localctx = BoardGameParser.GameplayContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(BoardGameParser.START)
            self.state = 132
            self.match(BoardGameParser.COLON)
            self.state = 133
            self.code_block()
            self.state = 134
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode_block" ):
                return visitor.visitCode_block(self)
            else:
                return visitor.visitChildren(self)




    def code_block(self):

        localctx = BoardGameParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 136
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 139 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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


        def dice_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Dice_statementContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BoardGameParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.game_entities_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.board_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.player_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.condition_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.rule_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.piece_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 147
                self.obstacle_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 148
                self.booster_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 149
                self.turn_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 150
                self.move_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 151
                self.dice_statement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 152
                self.expression()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 153
                self.if_statement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 154
                self.for_statement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 155
                self.while_statement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 156
                self.input_statement()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 157
                self.print_statement()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 158
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

        def GAME(self):
            return self.getToken(BoardGameParser.GAME, 0)

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

        def TIMER(self):
            return self.getToken(BoardGameParser.TIMER, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_game_entities

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGame_entities" ):
                listener.enterGame_entities(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGame_entities" ):
                listener.exitGame_entities(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGame_entities" ):
                return visitor.visitGame_entities(self)
            else:
                return visitor.visitChildren(self)




    def game_entities(self):

        localctx = BoardGameParser.Game_entitiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_game_entities)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24314) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_literal" ):
                return visitor.visitInt_literal(self)
            else:
                return visitor.visitChildren(self)




    def int_literal(self):

        localctx = BoardGameParser.Int_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_int_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not(_la==71 or _la==72):
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


        def getRuleIndex(self):
            return BoardGameParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntegerContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def int_literal(self):
            return self.getTypedRuleContext(BoardGameParser.Int_literalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LITERAL(self):
            return self.getToken(BoardGameParser.FLOAT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(BoardGameParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class BooleanContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(BoardGameParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = BoardGameParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literal)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [71, 72]:
                localctx = BoardGameParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.int_literal()
                pass
            elif token in [73]:
                localctx = BoardGameParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(BoardGameParser.FLOAT_LITERAL)
                pass
            elif token in [74]:
                localctx = BoardGameParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.match(BoardGameParser.STRING_LITERAL)
                pass
            elif token in [75]:
                localctx = BoardGameParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 168
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


        def list_(self):
            return self.getTypedRuleContext(BoardGameParser.ListContext,0)


        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def method_call(self):
            return self.getTypedRuleContext(BoardGameParser.Method_callContext,0)


        def entity_count_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Entity_count_expressionContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = BoardGameParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primary)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.list_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.object_access()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 176
                self.expression()
                self.state = 177
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.method_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 180
                self.entity_count_expression()
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


        def getRuleIndex(self):
            return BoardGameParser.RULE_param_list

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SingleParamContext(Param_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Param_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)
        def ANY(self):
            return self.getToken(BoardGameParser.ANY, 0)
        def NONE(self):
            return self.getToken(BoardGameParser.NONE, 0)
        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)
        def literal(self):
            return self.getTypedRuleContext(BoardGameParser.LiteralContext,0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)

        def list_(self):
            return self.getTypedRuleContext(BoardGameParser.ListContext,0)

        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleParam" ):
                listener.enterSingleParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleParam" ):
                listener.exitSingleParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleParam" ):
                return visitor.visitSingleParam(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentParamContext(Param_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Param_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Assignment_expressionContext,0)

        def COMMA(self):
            return self.getToken(BoardGameParser.COMMA, 0)
        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentParam" ):
                listener.enterAssignmentParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentParam" ):
                listener.exitAssignmentParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentParam" ):
                return visitor.visitAssignmentParam(self)
            else:
                return visitor.visitChildren(self)


    class ScoreParamContext(Param_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Param_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SCORE(self):
            return self.getToken(BoardGameParser.SCORE, 0)
        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)
        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)
        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)
        def CONDITIONS(self):
            return self.getToken(BoardGameParser.CONDITIONS, 0)
        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScoreParam" ):
                listener.enterScoreParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScoreParam" ):
                listener.exitScoreParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScoreParam" ):
                return visitor.visitScoreParam(self)
            else:
                return visitor.visitChildren(self)


    class BoardPosParamContext(Param_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Param_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)

        def COMMA(self):
            return self.getToken(BoardGameParser.COMMA, 0)
        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoardPosParam" ):
                listener.enterBoardPosParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoardPosParam" ):
                listener.exitBoardPosParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoardPosParam" ):
                return visitor.visitBoardPosParam(self)
            else:
                return visitor.visitChildren(self)


    class AllAnyNoneParamContext(Param_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Param_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(BoardGameParser.COMMA, 0)
        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)

        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)
        def ANY(self):
            return self.getToken(BoardGameParser.ANY, 0)
        def NONE(self):
            return self.getToken(BoardGameParser.NONE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllAnyNoneParam" ):
                listener.enterAllAnyNoneParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllAnyNoneParam" ):
                listener.exitAllAnyNoneParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllAnyNoneParam" ):
                return visitor.visitAllAnyNoneParam(self)
            else:
                return visitor.visitChildren(self)


    class ObjectAccessParamContext(Param_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Param_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)

        def COMMA(self):
            return self.getToken(BoardGameParser.COMMA, 0)
        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectAccessParam" ):
                listener.enterObjectAccessParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectAccessParam" ):
                listener.exitObjectAccessParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectAccessParam" ):
                return visitor.visitObjectAccessParam(self)
            else:
                return visitor.visitChildren(self)


    class LiteralParamContext(Param_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Param_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(BoardGameParser.LiteralContext,0)

        def COMMA(self):
            return self.getToken(BoardGameParser.COMMA, 0)
        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralParam" ):
                listener.enterLiteralParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralParam" ):
                listener.exitLiteralParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralParam" ):
                return visitor.visitLiteralParam(self)
            else:
                return visitor.visitChildren(self)


    class VariableParamContext(Param_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Param_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)
        def COMMA(self):
            return self.getToken(BoardGameParser.COMMA, 0)
        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableParam" ):
                listener.enterVariableParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableParam" ):
                listener.exitVariableParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableParam" ):
                return visitor.visitVariableParam(self)
            else:
                return visitor.visitChildren(self)


    class ListLiteralParamContext(Param_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Param_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_(self):
            return self.getTypedRuleContext(BoardGameParser.ListContext,0)

        def COMMA(self):
            return self.getToken(BoardGameParser.COMMA, 0)
        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteralParam" ):
                listener.enterListLiteralParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteralParam" ):
                listener.exitListLiteralParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteralParam" ):
                return visitor.visitListLiteralParam(self)
            else:
                return visitor.visitChildren(self)



    def param_list(self):

        localctx = BoardGameParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = BoardGameParser.ScoreParamContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(BoardGameParser.SCORE)
                self.state = 184
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 185
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 186
                self.match(BoardGameParser.DOT)
                self.state = 187
                self.match(BoardGameParser.CONDITIONS)
                self.state = 188
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                localctx = BoardGameParser.AllAnyNoneParamContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15393162788864) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 190
                self.match(BoardGameParser.COMMA)
                self.state = 191
                self.param_list()
                pass

            elif la_ == 3:
                localctx = BoardGameParser.AssignmentParamContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.assignment_expression()
                self.state = 193
                self.match(BoardGameParser.COMMA)
                self.state = 194
                self.param_list()
                pass

            elif la_ == 4:
                localctx = BoardGameParser.LiteralParamContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.literal()
                self.state = 197
                self.match(BoardGameParser.COMMA)
                self.state = 198
                self.param_list()
                pass

            elif la_ == 5:
                localctx = BoardGameParser.VariableParamContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 200
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 201
                self.match(BoardGameParser.COMMA)
                self.state = 202
                self.param_list()
                pass

            elif la_ == 6:
                localctx = BoardGameParser.BoardPosParamContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 203
                self.board_pos(0)
                self.state = 204
                self.match(BoardGameParser.COMMA)
                self.state = 205
                self.param_list()
                pass

            elif la_ == 7:
                localctx = BoardGameParser.ObjectAccessParamContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 207
                self.object_access()
                self.state = 208
                self.match(BoardGameParser.COMMA)
                self.state = 209
                self.param_list()
                pass

            elif la_ == 8:
                localctx = BoardGameParser.ListLiteralParamContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 211
                self.list_()
                self.state = 212
                self.match(BoardGameParser.COMMA)
                self.state = 213
                self.param_list()
                pass

            elif la_ == 9:
                localctx = BoardGameParser.SingleParamContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 223
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 215
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 2:
                    self.state = 216
                    self.match(BoardGameParser.ANY)
                    pass

                elif la_ == 3:
                    self.state = 217
                    self.match(BoardGameParser.NONE)
                    pass

                elif la_ == 4:
                    self.state = 218
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 5:
                    self.state = 219
                    self.literal()
                    pass

                elif la_ == 6:
                    self.state = 220
                    self.object_access()
                    pass

                elif la_ == 7:
                    self.state = 221
                    self.list_()
                    pass

                elif la_ == 8:
                    self.state = 222
                    self.board_pos(0)
                    pass


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = BoardGameParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(BoardGameParser.OPEN_BRACKET)
            self.state = 228
            self.param_list()
            self.state = 229
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


        def getRuleIndex(self):
            return BoardGameParser.RULE_object_access

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GameEntityAccessContext(Object_accessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Object_accessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def game_entities(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Game_entitiesContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Game_entitiesContext,i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.DOT)
            else:
                return self.getToken(BoardGameParser.DOT, i)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGameEntityAccess" ):
                listener.enterGameEntityAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGameEntityAccess" ):
                listener.exitGameEntityAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGameEntityAccess" ):
                return visitor.visitGameEntityAccess(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierAccessContext(Object_accessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Object_accessContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierAccess" ):
                listener.enterIdentifierAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierAccess" ):
                listener.exitIdentifierAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierAccess" ):
                return visitor.visitIdentifierAccess(self)
            else:
                return visitor.visitChildren(self)


    class ObjectEntityAccessContext(Object_accessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Object_accessContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectEntityAccess" ):
                listener.enterObjectEntityAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectEntityAccess" ):
                listener.exitObjectEntityAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectEntityAccess" ):
                return visitor.visitObjectEntityAccess(self)
            else:
                return visitor.visitChildren(self)



    def object_access(self):

        localctx = BoardGameParser.Object_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_object_access)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = BoardGameParser.ObjectEntityAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 232
                self.match(BoardGameParser.DOT)
                self.state = 233
                self.game_entities()
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 237
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [62]:
                            self.state = 234
                            self.match(BoardGameParser.DOT)
                            self.state = 235
                            self.game_entities()
                            pass
                        elif token in [76]:
                            self.state = 236
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 241
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 2:
                localctx = BoardGameParser.GameEntityAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.game_entities()
                self.state = 243
                self.match(BoardGameParser.DOT)
                self.state = 244
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 248
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [62]:
                            self.state = 245
                            self.match(BoardGameParser.DOT)
                            self.state = 246
                            self.game_entities()
                            pass
                        elif token in [76]:
                            self.state = 247
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 252
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 3:
                localctx = BoardGameParser.IdentifierAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 253
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 254
                self.match(BoardGameParser.DOT)
                self.state = 255
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 259
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [62]:
                            self.state = 256
                            self.match(BoardGameParser.DOT)
                            self.state = 257
                            self.game_entities()
                            pass
                        elif token in [76]:
                            self.state = 258
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 263
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


    class Board_posContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BoardGameParser.RULE_board_pos

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BoardPosRowColContext(Board_posContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Board_posContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOARD(self):
            return self.getToken(BoardGameParser.BOARD, 0)
        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.DOT)
            else:
                return self.getToken(BoardGameParser.DOT, i)
        def ROW(self):
            return self.getToken(BoardGameParser.ROW, 0)
        def COLUMN(self):
            return self.getToken(BoardGameParser.COLUMN, 0)
        def int_literal(self):
            return self.getTypedRuleContext(BoardGameParser.Int_literalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoardPosRowCol" ):
                listener.enterBoardPosRowCol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoardPosRowCol" ):
                listener.exitBoardPosRowCol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoardPosRowCol" ):
                return visitor.visitBoardPosRowCol(self)
            else:
                return visitor.visitChildren(self)


    class BoardPosIdentifierContext(Board_posContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Board_posContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOARD(self):
            return self.getToken(BoardGameParser.BOARD, 0)
        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)
        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoardPosIdentifier" ):
                listener.enterBoardPosIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoardPosIdentifier" ):
                listener.exitBoardPosIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoardPosIdentifier" ):
                return visitor.visitBoardPosIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class BoardPosIntContext(Board_posContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Board_posContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOARD(self):
            return self.getToken(BoardGameParser.BOARD, 0)
        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)
        def int_literal(self):
            return self.getTypedRuleContext(BoardGameParser.Int_literalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoardPosInt" ):
                listener.enterBoardPosInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoardPosInt" ):
                listener.exitBoardPosInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoardPosInt" ):
                return visitor.visitBoardPosInt(self)
            else:
                return visitor.visitChildren(self)


    class BoardPosRangeContext(Board_posContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Board_posContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def board_pos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Board_posContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Board_posContext,i)

        def ELIPSIS(self):
            return self.getToken(BoardGameParser.ELIPSIS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoardPosRange" ):
                listener.enterBoardPosRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoardPosRange" ):
                listener.exitBoardPosRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoardPosRange" ):
                return visitor.visitBoardPosRange(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = BoardGameParser.BoardPosIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 267
                self.match(BoardGameParser.BOARD)
                self.state = 268
                self.match(BoardGameParser.DOT)
                self.state = 269
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = BoardGameParser.BoardPosRowColContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 270
                self.match(BoardGameParser.BOARD)
                self.state = 271
                self.match(BoardGameParser.DOT)
                self.state = 272
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 273
                self.match(BoardGameParser.DOT)

                self.state = 274
                self.int_literal()
                pass

            elif la_ == 3:
                localctx = BoardGameParser.BoardPosIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 275
                self.match(BoardGameParser.BOARD)
                self.state = 276
                self.match(BoardGameParser.DOT)

                self.state = 277
                self.int_literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.BoardPosRangeContext(self, BoardGameParser.Board_posContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_board_pos)
                    self.state = 280
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 281
                    self.match(BoardGameParser.ELIPSIS)
                    self.state = 282
                    self.board_pos(2) 
                self.state = 287
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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

        def NOT_EQUAL_OPT(self):
            return self.getToken(BoardGameParser.NOT_EQUAL_OPT, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_opt" ):
                return visitor.visitConditional_opt(self)
            else:
                return visitor.visitChildren(self)




    def conditional_opt(self):

        localctx = BoardGameParser.Conditional_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_conditional_opt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 69242844270821376) != 0)):
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

        def base_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Base_expressionContext,0)


        def logical_opt(self):
            return self.getTypedRuleContext(BoardGameParser.Logical_optContext,0)


        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BoardGameParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.base_expression()
                self.state = 291
                self.logical_opt()
                self.state = 292
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.base_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Entity_count_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BoardGameParser.RULE_entity_count_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CountObjectAccessContext(Entity_count_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Entity_count_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)

        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)
        def COUNT(self):
            return self.getToken(BoardGameParser.COUNT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCountObjectAccess" ):
                listener.enterCountObjectAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCountObjectAccess" ):
                listener.exitCountObjectAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCountObjectAccess" ):
                return visitor.visitCountObjectAccess(self)
            else:
                return visitor.visitChildren(self)


    class CountIdentifierContext(Entity_count_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Entity_count_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)
        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)
        def COUNT(self):
            return self.getToken(BoardGameParser.COUNT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCountIdentifier" ):
                listener.enterCountIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCountIdentifier" ):
                listener.exitCountIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCountIdentifier" ):
                return visitor.visitCountIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class CountEntityContext(Entity_count_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Entity_count_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def game_entities(self):
            return self.getTypedRuleContext(BoardGameParser.Game_entitiesContext,0)

        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)
        def COUNT(self):
            return self.getToken(BoardGameParser.COUNT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCountEntity" ):
                listener.enterCountEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCountEntity" ):
                listener.exitCountEntity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCountEntity" ):
                return visitor.visitCountEntity(self)
            else:
                return visitor.visitChildren(self)



    def entity_count_expression(self):

        localctx = BoardGameParser.Entity_count_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_entity_count_expression)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                localctx = BoardGameParser.CountEntityContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.game_entities()
                self.state = 298
                self.match(BoardGameParser.DOT)
                self.state = 299
                self.match(BoardGameParser.COUNT)
                pass

            elif la_ == 2:
                localctx = BoardGameParser.CountIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 302
                self.match(BoardGameParser.DOT)
                self.state = 303
                self.match(BoardGameParser.COUNT)
                pass

            elif la_ == 3:
                localctx = BoardGameParser.CountObjectAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.object_access()
                self.state = 305
                self.match(BoardGameParser.DOT)
                self.state = 306
                self.match(BoardGameParser.COUNT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(BoardGameParser.PrimaryContext,0)


        def assignment_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Assignment_expressionContext,0)


        def math_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Math_expressionContext,0)


        def in_expression(self):
            return self.getTypedRuleContext(BoardGameParser.In_expressionContext,0)


        def at_expression(self):
            return self.getTypedRuleContext(BoardGameParser.At_expressionContext,0)


        def conditional_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Conditional_expressionContext,0)


        def move_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Move_statementContext,0)


        def any_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Any_expressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def NOT_OPT(self):
            return self.getToken(BoardGameParser.NOT_OPT, 0)

        def entity_count_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Entity_count_expressionContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_base_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_expression" ):
                listener.enterBase_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_expression" ):
                listener.exitBase_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBase_expression" ):
                return visitor.visitBase_expression(self)
            else:
                return visitor.visitChildren(self)




    def base_expression(self):

        localctx = BoardGameParser.Base_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_base_expression)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.assignment_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.math_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.in_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 314
                self.at_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 315
                self.conditional_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 316
                self.move_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 317
                self.any_expression()
                self.state = 318
                self.expression()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 320
                self.match(BoardGameParser.NOT_OPT)
                self.state = 321
                self.expression()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 322
                self.entity_count_expression()
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

        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)


        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_objects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjects" ):
                listener.enterObjects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjects" ):
                listener.exitObjects(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjects" ):
                return visitor.visitObjects(self)
            else:
                return visitor.visitChildren(self)




    def objects(self):

        localctx = BoardGameParser.ObjectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_objects)
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.board_pos(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.object_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(BoardGameParser.DEFINE, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def COLON(self):
            return self.getToken(BoardGameParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(BoardGameParser.Code_blockContext,0)


        def END(self):
            return self.getToken(BoardGameParser.END, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_method_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_declaration" ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_declaration" ):
                listener.exitMethod_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declaration" ):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)




    def method_declaration(self):

        localctx = BoardGameParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(BoardGameParser.DEFINE)
            self.state = 331
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 332
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 333
            self.param_list()
            self.state = 334
            self.match(BoardGameParser.CLOSE_PAR)
            self.state = 335
            self.match(BoardGameParser.COLON)
            self.state = 336
            self.code_block()
            self.state = 337
            self.match(BoardGameParser.END)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = BoardGameParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.objects()
            self.state = 340
            self.match(BoardGameParser.DOT)
            self.state = 341
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 342
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15393162813178) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 2017) != 0):
                self.state = 343
                self.param_list()
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 349
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_define_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(BoardGameParser.DEFINE, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(BoardGameParser.COLON, 0)

        def END(self):
            return self.getToken(BoardGameParser.END, 0)

        def class_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Class_statementContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Class_statementContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_class_define_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_define_block" ):
                listener.enterClass_define_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_define_block" ):
                listener.exitClass_define_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_define_block" ):
                return visitor.visitClass_define_block(self)
            else:
                return visitor.visitChildren(self)




    def class_define_block(self):

        localctx = BoardGameParser.Class_define_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_class_define_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(BoardGameParser.DEFINE)
            self.state = 352
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 353
            self.match(BoardGameParser.COLON)
            self.state = 355 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 354
                self.class_statement()
                self.state = 357 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==76):
                    break

            self.state = 359
            self.match(BoardGameParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Assignment_expressionContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(BoardGameParser.Method_declarationContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_class_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_statement" ):
                listener.enterClass_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_statement" ):
                listener.exitClass_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_statement" ):
                return visitor.visitClass_statement(self)
            else:
                return visitor.visitChildren(self)




    def class_statement(self):

        localctx = BoardGameParser.Class_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_class_statement)
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [76]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.assignment_expression()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.method_declaration()
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


    class Conditional_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.AdditiveContext,i)


        def conditional_opt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Conditional_optContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Conditional_optContext,i)


        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.PrimaryContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_conditional_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_expression" ):
                listener.enterConditional_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_expression" ):
                listener.exitConditional_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_expression" ):
                return visitor.visitConditional_expression(self)
            else:
                return visitor.visitChildren(self)




    def conditional_expression(self):

        localctx = BoardGameParser.Conditional_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_conditional_expression)
        self._la = 0 # Token type
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.additive()
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 69242844270821376) != 0):
                    self.state = 366
                    self.conditional_opt()
                    self.state = 367
                    self.additive()
                    self.state = 373
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.primary()
                self.state = 375
                self.conditional_opt()
                self.state = 376
                self.primary()
                pass


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIn_expression" ):
                return visitor.visitIn_expression(self)
            else:
                return visitor.visitChildren(self)




    def in_expression(self):

        localctx = BoardGameParser.In_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_in_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.primary()
            self.state = 381
            self.match(BoardGameParser.IN)
            self.state = 382
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAt_expression" ):
                return visitor.visitAt_expression(self)
            else:
                return visitor.visitChildren(self)




    def at_expression(self):

        localctx = BoardGameParser.At_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_at_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 384
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 385
                self.object_access()
                pass


            self.state = 388
            self.match(BoardGameParser.AT)
            self.state = 389
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAny_expression" ):
                return visitor.visitAny_expression(self)
            else:
                return visitor.visitChildren(self)




    def any_expression(self):

        localctx = BoardGameParser.Any_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_any_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(BoardGameParser.ANY)
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 392
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 393
                self.object_access()
                pass

            elif la_ == 3:
                self.state = 394
                self.list_()
                pass

            elif la_ == 4:
                self.state = 395
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


        def getRuleIndex(self):
            return BoardGameParser.RULE_assignment_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignEvaluateContext(Assignment_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Assignment_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)
        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)
        def evaluate_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Evaluate_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignEvaluate" ):
                listener.enterAssignEvaluate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignEvaluate" ):
                listener.exitAssignEvaluate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignEvaluate" ):
                return visitor.visitAssignEvaluate(self)
            else:
                return visitor.visitChildren(self)


    class AssignExpressionContext(Assignment_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Assignment_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)
        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)
        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpression" ):
                listener.enterAssignExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpression" ):
                listener.exitAssignExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpression" ):
                return visitor.visitAssignExpression(self)
            else:
                return visitor.visitChildren(self)


    class AssignMethodCallContext(Assignment_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Assignment_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)
        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)
        def method_call(self):
            return self.getTypedRuleContext(BoardGameParser.Method_callContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignMethodCall" ):
                listener.enterAssignMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignMethodCall" ):
                listener.exitAssignMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignMethodCall" ):
                return visitor.visitAssignMethodCall(self)
            else:
                return visitor.visitChildren(self)


    class AssignInputContext(Assignment_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BoardGameParser.Assignment_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)
        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)
        def input_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Input_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignInput" ):
                listener.enterAssignInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignInput" ):
                listener.exitAssignInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignInput" ):
                return visitor.visitAssignInput(self)
            else:
                return visitor.visitChildren(self)



    def assignment_expression(self):

        localctx = BoardGameParser.Assignment_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignment_expression)
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                localctx = BoardGameParser.AssignExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 399
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 400
                self.expression()
                pass

            elif la_ == 2:
                localctx = BoardGameParser.AssignEvaluateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 402
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 403
                self.evaluate_statement()
                pass

            elif la_ == 3:
                localctx = BoardGameParser.AssignMethodCallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 404
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 405
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 406
                self.method_call()
                pass

            elif la_ == 4:
                localctx = BoardGameParser.AssignInputContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 407
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 408
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 409
                self.input_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eval_base_expressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Conditional_expressionContext,0)


        def not_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Not_expressionContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_eval_base_expressions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEval_base_expressions" ):
                listener.enterEval_base_expressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEval_base_expressions" ):
                listener.exitEval_base_expressions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEval_base_expressions" ):
                return visitor.visitEval_base_expressions(self)
            else:
                return visitor.visitChildren(self)




    def eval_base_expressions(self):

        localctx = BoardGameParser.Eval_base_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_eval_base_expressions)
        try:
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 56, 57, 64, 66, 71, 72, 73, 74, 75, 76]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.conditional_expression()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.not_expression()
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


    class Eval_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eval_base_expressions(self):
            return self.getTypedRuleContext(BoardGameParser.Eval_base_expressionsContext,0)


        def logical_opt(self):
            return self.getTypedRuleContext(BoardGameParser.Logical_optContext,0)


        def eval_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Eval_expressionContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_eval_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEval_expression" ):
                listener.enterEval_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEval_expression" ):
                listener.exitEval_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEval_expression" ):
                return visitor.visitEval_expression(self)
            else:
                return visitor.visitChildren(self)




    def eval_expression(self):

        localctx = BoardGameParser.Eval_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_eval_expression)
        try:
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.eval_base_expressions()
                self.state = 417
                self.logical_opt()
                self.state = 418
                self.eval_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.eval_base_expressions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OPT(self):
            return self.getToken(BoardGameParser.NOT_OPT, 0)

        def conditional_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Conditional_expressionContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_not_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_expression" ):
                listener.enterNot_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_expression" ):
                listener.exitNot_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_expression" ):
                return visitor.visitNot_expression(self)
            else:
                return visitor.visitChildren(self)




    def not_expression(self):

        localctx = BoardGameParser.Not_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_not_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(BoardGameParser.NOT_OPT)
            self.state = 424
            self.conditional_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Evaluate_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVALUATE(self):
            return self.getToken(BoardGameParser.EVALUATE, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def eval_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Eval_expressionContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_evaluate_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluate_statement" ):
                listener.enterEvaluate_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluate_statement" ):
                listener.exitEvaluate_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvaluate_statement" ):
                return visitor.visitEvaluate_statement(self)
            else:
                return visitor.visitChildren(self)




    def evaluate_statement(self):

        localctx = BoardGameParser.Evaluate_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_evaluate_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(BoardGameParser.EVALUATE)
            self.state = 427
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 428
            self.eval_expression()
            self.state = 429
            self.match(BoardGameParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_evalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def eval_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Eval_expressionContext,0)


        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def int_literal(self):
            return self.getTypedRuleContext(BoardGameParser.Int_literalContext,0)


        def FLOAT_LITERAL(self):
            return self.getToken(BoardGameParser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(BoardGameParser.BOOLEAN_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_primary_eval

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_eval" ):
                listener.enterPrimary_eval(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_eval" ):
                listener.exitPrimary_eval(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_eval" ):
                return visitor.visitPrimary_eval(self)
            else:
                return visitor.visitChildren(self)




    def primary_eval(self):

        localctx = BoardGameParser.Primary_evalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_primary_eval)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 432
                self.eval_expression()
                self.state = 433
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.int_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
                self.match(BoardGameParser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 437
                self.match(BoardGameParser.BOOLEAN_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 438
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 439
                self.object_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_eval(self):
            return self.getTypedRuleContext(BoardGameParser.Primary_evalContext,0)


        def ADD_OPT(self):
            return self.getToken(BoardGameParser.ADD_OPT, 0)

        def SUB_OPT(self):
            return self.getToken(BoardGameParser.SUB_OPT, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = BoardGameParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56 or _la==57:
                self.state = 442
                _la = self._input.LA(1)
                if not(_la==56 or _la==57):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 445
            self.primary_eval()
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

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.UnaryContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.UnaryContext,i)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponent" ):
                return visitor.visitExponent(self)
            else:
                return visitor.visitChildren(self)




    def exponent(self):

        localctx = BoardGameParser.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exponent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.unary()
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 448
                self.match(BoardGameParser.EXP_OPT)
                self.state = 449
                self.unary()
                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def exponent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.ExponentContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.ExponentContext,i)


        def MUL_OPT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.MUL_OPT)
            else:
                return self.getToken(BoardGameParser.MUL_OPT, i)

        def DIV_OPT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.DIV_OPT)
            else:
                return self.getToken(BoardGameParser.DIV_OPT, i)

        def getRuleIndex(self):
            return BoardGameParser.RULE_multiplicative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative" ):
                listener.enterMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative" ):
                listener.exitMultiplicative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative(self):

        localctx = BoardGameParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.exponent()
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==58 or _la==59:
                self.state = 456
                _la = self._input.LA(1)
                if not(_la==58 or _la==59):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 457
                self.exponent()
                self.state = 462
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.MultiplicativeContext,i)


        def ADD_OPT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.ADD_OPT)
            else:
                return self.getToken(BoardGameParser.ADD_OPT, i)

        def SUB_OPT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.SUB_OPT)
            else:
                return self.getToken(BoardGameParser.SUB_OPT, i)

        def getRuleIndex(self):
            return BoardGameParser.RULE_additive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)




    def additive(self):

        localctx = BoardGameParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.multiplicative()
            self.state = 468
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 464
                    _la = self._input.LA(1)
                    if not(_la==56 or _la==57):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 465
                    self.multiplicative() 
                self.state = 470
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_expression" ):
                return visitor.visitMath_expression(self)
            else:
                return visitor.visitChildren(self)




    def math_expression(self):

        localctx = BoardGameParser.Math_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_math_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.additive()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_opt" ):
                return visitor.visitLogical_opt(self)
            else:
                return visitor.visitChildren(self)




    def logical_opt(self):

        localctx = BoardGameParser.Logical_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_logical_opt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            _la = self._input.LA(1)
            if not(_la==46 or _la==47):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGame_entities_statement" ):
                return visitor.visitGame_entities_statement(self)
            else:
                return visitor.visitChildren(self)




    def game_entities_statement(self):

        localctx = BoardGameParser.Game_entities_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_game_entities_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.game_entities()
            self.state = 476
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 477
            self.param_list()
            self.state = 478
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


        def AT(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.AT)
            else:
                return self.getToken(BoardGameParser.AT, i)

        def board_pos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.Board_posContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.Board_posContext,i)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayer_statement" ):
                return visitor.visitPlayer_statement(self)
            else:
                return visitor.visitChildren(self)




    def player_statement(self):

        localctx = BoardGameParser.Player_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_player_statement)
        self._la = 0 # Token type
        try:
            self.state = 496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.match(BoardGameParser.PLAYER)
                self.state = 481
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 482
                self.match(BoardGameParser.COLOR)
                self.state = 483
                self.object_access()
                self.state = 488
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 484
                    self.match(BoardGameParser.AT)
                    self.state = 485
                    self.board_pos(0)
                    self.state = 490
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_statement" ):
                return visitor.visitCondition_statement(self)
            else:
                return visitor.visitChildren(self)




    def condition_statement(self):

        localctx = BoardGameParser.Condition_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_condition_statement)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_statement" ):
                return visitor.visitRule_statement(self)
            else:
                return visitor.visitChildren(self)




    def rule_statement(self):

        localctx = BoardGameParser.Rule_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_rule_statement)
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.ExpressionContext,i)


        def ANY(self):
            return self.getToken(BoardGameParser.ANY, 0)

        def NONE(self):
            return self.getToken(BoardGameParser.NONE, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPiece_statement" ):
                return visitor.visitPiece_statement(self)
            else:
                return visitor.visitChildren(self)




    def piece_statement(self):

        localctx = BoardGameParser.Piece_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_piece_statement)
        self._la = 0 # Token type
        try:
            self.state = 577
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.match(BoardGameParser.PIECE)
                self.state = 517
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
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
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
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
                while _la==63:
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
                self.state = 557
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 548
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 549
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 550
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 4:
                    self.state = 551
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 552
                    self.param_list()
                    self.state = 553
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass

                elif la_ == 5:
                    self.state = 555
                    self.match(BoardGameParser.ANY)
                    pass

                elif la_ == 6:
                    self.state = 556
                    self.match(BoardGameParser.NONE)
                    pass


                self.state = 559
                self.match(BoardGameParser.ACTION)
                self.state = 560
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 561
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 562
                self.expression()
                self.state = 563
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 572
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==63:
                    self.state = 564
                    self.match(BoardGameParser.COMMA)
                    self.state = 565
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 566
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 567
                    self.expression()
                    self.state = 568
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 574
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 575
                self.match(BoardGameParser.PIECE)
                self.state = 576
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

        def PLAYER(self):
            return self.getToken(BoardGameParser.PLAYER, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def PIECE(self):
            return self.getToken(BoardGameParser.PIECE, 0)

        def SETUP(self):
            return self.getToken(BoardGameParser.SETUP, 0)

        def OPEN_PAR(self):
            return self.getToken(BoardGameParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(BoardGameParser.CLOSE_PAR, 0)

        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)

        def param_list(self):
            return self.getTypedRuleContext(BoardGameParser.Param_listContext,0)


        def board_pos(self):
            return self.getTypedRuleContext(BoardGameParser.Board_posContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoard_statement" ):
                return visitor.visitBoard_statement(self)
            else:
                return visitor.visitChildren(self)




    def board_statement(self):

        localctx = BoardGameParser.Board_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_board_statement)
        try:
            self.state = 627
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 579
                self.match(BoardGameParser.PLAYER)
                self.state = 580
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 581
                self.match(BoardGameParser.PIECE)
                self.state = 585
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                if la_ == 1:
                    self.state = 582
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 583
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 584
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 587
                self.match(BoardGameParser.SETUP)
                self.state = 588
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 591
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 589
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 590
                    self.board_pos(0)
                    pass


                self.state = 593
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 595
                self.match(BoardGameParser.PLAYER)
                self.state = 596
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 597
                self.match(BoardGameParser.OBSTACLE)
                self.state = 601
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 598
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 599
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 600
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 603
                self.match(BoardGameParser.SETUP)
                self.state = 604
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 607
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                if la_ == 1:
                    self.state = 605
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 606
                    self.board_pos(0)
                    pass


                self.state = 609
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 611
                self.match(BoardGameParser.PLAYER)
                self.state = 612
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 613
                self.match(BoardGameParser.BOOSTER)
                self.state = 617
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 614
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 615
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 616
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 619
                self.match(BoardGameParser.SETUP)
                self.state = 620
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 623
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 621
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 622
                    self.board_pos(0)
                    pass


                self.state = 625
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObstacle_statement" ):
                return visitor.visitObstacle_statement(self)
            else:
                return visitor.visitChildren(self)




    def obstacle_statement(self):

        localctx = BoardGameParser.Obstacle_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_obstacle_statement)
        self._la = 0 # Token type
        try:
            self.state = 659
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 629
                self.match(BoardGameParser.OBSTACLE)
                self.state = 633
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 630
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 631
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 632
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 635
                self.match(BoardGameParser.COUNT)
                self.state = 636
                self.int_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 637
                self.match(BoardGameParser.OBSTACLE)
                self.state = 641
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 638
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 639
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 640
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 643
                self.match(BoardGameParser.ACTION)
                self.state = 644
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 645
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 646
                self.param_list()
                self.state = 647
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 656
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==63:
                    self.state = 648
                    self.match(BoardGameParser.COMMA)
                    self.state = 649
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 650
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 651
                    self.param_list()
                    self.state = 652
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 658
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooster_statement" ):
                return visitor.visitBooster_statement(self)
            else:
                return visitor.visitChildren(self)




    def booster_statement(self):

        localctx = BoardGameParser.Booster_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_booster_statement)
        self._la = 0 # Token type
        try:
            self.state = 691
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 661
                self.match(BoardGameParser.BOOSTER)
                self.state = 665
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 662
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 663
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 664
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 667
                self.match(BoardGameParser.COUNT)
                self.state = 668
                self.int_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 669
                self.match(BoardGameParser.BOOSTER)
                self.state = 673
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 670
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 671
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 672
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 675
                self.match(BoardGameParser.ACTION)
                self.state = 676
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 677
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 678
                self.param_list()
                self.state = 679
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 688
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==63:
                    self.state = 680
                    self.match(BoardGameParser.COMMA)
                    self.state = 681
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 682
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 683
                    self.param_list()
                    self.state = 684
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 690
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMove_statement" ):
                return visitor.visitMove_statement(self)
            else:
                return visitor.visitChildren(self)




    def move_statement(self):

        localctx = BoardGameParser.Move_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_move_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 693
            self.match(BoardGameParser.MOVE)
            self.state = 697
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 694
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 695
                self.object_access()
                pass

            elif la_ == 3:
                self.state = 696
                self.match(BoardGameParser.ALL)
                pass


            self.state = 699
            self.match(BoardGameParser.TO)
            self.state = 700
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTurn_statement" ):
                return visitor.visitTurn_statement(self)
            else:
                return visitor.visitChildren(self)




    def turn_statement(self):

        localctx = BoardGameParser.Turn_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_turn_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702
            self.match(BoardGameParser.TURN)
            self.state = 703
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 704
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = BoardGameParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_if_statement)
        try:
            self.state = 719
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 706
                self.match(BoardGameParser.IF)
                self.state = 707
                self.expression()
                self.state = 708
                self.match(BoardGameParser.COLON)
                self.state = 709
                self.code_block()
                self.state = 710
                self.match(BoardGameParser.ELSE)
                self.state = 711
                self.match(BoardGameParser.COLON)
                self.state = 712
                self.code_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 714
                self.match(BoardGameParser.IF)
                self.state = 715
                self.expression()
                self.state = 716
                self.match(BoardGameParser.COLON)
                self.state = 717
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = BoardGameParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
            self.match(BoardGameParser.FOR)
            self.state = 722
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 723
            self.match(BoardGameParser.IN)
            self.state = 724
            self.list_()
            self.state = 725
            self.match(BoardGameParser.COLON)
            self.state = 726
            self.code_block()
            self.state = 727
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = BoardGameParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 729
            self.match(BoardGameParser.WHILE)
            self.state = 730
            self.expression()
            self.state = 731
            self.match(BoardGameParser.COLON)
            self.state = 732
            self.code_block()
            self.state = 733
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

        def IDENTIFIER(self):
            return self.getToken(BoardGameParser.IDENTIFIER, 0)

        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_statement" ):
                return visitor.visitInput_statement(self)
            else:
                return visitor.visitChildren(self)




    def input_statement(self):

        localctx = BoardGameParser.Input_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_input_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 735
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 736
            self.match(BoardGameParser.ASSIGN_OPT)
            self.state = 737
            self.match(BoardGameParser.INPUT)
            self.state = 738
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 742
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 739
                self.match(BoardGameParser.STRING_LITERAL)
                self.state = 744
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 745
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_statement" ):
                return visitor.visitPrint_statement(self)
            else:
                return visitor.visitChildren(self)




    def print_statement(self):

        localctx = BoardGameParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 747
            self.match(BoardGameParser.PRINT)
            self.state = 748
            self.match(BoardGameParser.OPEN_PAR)

            self.state = 749
            self.param_list()
            self.state = 750
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = BoardGameParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 752
            self.match(BoardGameParser.RETURN)
            self.state = 753
            self.expression()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDice_statement" ):
                return visitor.visitDice_statement(self)
            else:
                return visitor.visitChildren(self)




    def dice_statement(self):

        localctx = BoardGameParser.Dice_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_dice_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self.match(BoardGameParser.DICE)
            self.state = 756
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 757
            self.int_literal()
            self.state = 758
            self.match(BoardGameParser.COMMA)
            self.state = 759
            self.int_literal()
            self.state = 760
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
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def board_pos_sempred(self, localctx:Board_posContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




