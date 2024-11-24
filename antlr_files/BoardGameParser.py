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
        4,1,77,722,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,1,0,1,0,1,0,4,0,104,8,0,11,0,
        12,0,105,1,0,1,0,1,1,1,1,1,1,3,1,113,8,1,1,1,1,1,1,1,1,1,1,1,3,1,
        120,8,1,1,2,1,2,1,2,1,2,1,2,1,3,4,3,128,8,3,11,3,12,3,129,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,151,8,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,3,7,161,8,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,173,8,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,3,9,211,8,9,3,9,213,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,11,1,11,5,11,225,8,11,10,11,12,11,228,9,11,1,11,1,11,1,11,1,11,
        1,11,1,11,5,11,236,8,11,10,11,12,11,239,9,11,1,11,1,11,1,11,1,11,
        1,11,1,11,5,11,247,8,11,10,11,12,11,250,9,11,3,11,252,8,11,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,263,8,12,1,12,1,12,
        1,12,5,12,268,8,12,10,12,12,12,271,9,12,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,3,14,280,8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,299,8,16,1,17,
        1,17,1,17,3,17,304,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,19,1,19,1,19,1,19,1,19,5,19,320,8,19,10,19,12,19,323,9,19,
        1,19,1,19,1,20,1,20,1,20,1,20,4,20,331,8,20,11,20,12,20,332,1,20,
        1,20,1,21,1,21,3,21,339,8,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,
        1,23,1,24,1,24,3,24,351,8,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,
        1,25,3,25,361,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,3,26,374,8,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,
        383,8,26,1,26,1,26,3,26,387,8,26,1,27,1,27,1,27,5,27,392,8,27,10,
        27,12,27,395,9,27,1,28,1,28,1,28,1,28,1,28,1,28,5,28,403,8,28,10,
        28,12,28,406,9,28,1,29,1,29,1,29,1,29,1,29,1,29,5,29,414,8,29,10,
        29,12,29,417,9,29,1,30,1,30,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,
        33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,440,
        8,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,461,8,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,473,8,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,5,36,485,8,36,10,36,12,36,488,
        9,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,500,
        8,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,5,36,512,
        8,36,10,36,12,36,515,9,36,1,36,1,36,3,36,519,8,36,1,37,1,37,5,37,
        523,8,37,10,37,12,37,526,9,37,1,37,1,37,1,37,1,37,3,37,532,8,37,
        1,37,1,37,1,37,1,37,3,37,538,8,37,1,37,1,37,1,37,1,37,5,37,544,8,
        37,10,37,12,37,547,9,37,1,37,1,37,1,37,1,37,3,37,553,8,37,1,37,1,
        37,1,37,1,37,3,37,559,8,37,1,37,1,37,1,37,1,37,5,37,565,8,37,10,
        37,12,37,568,9,37,1,37,1,37,1,37,1,37,3,37,574,8,37,1,37,1,37,1,
        37,1,37,3,37,580,8,37,1,37,1,37,3,37,584,8,37,1,38,1,38,1,38,1,38,
        3,38,590,8,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,598,8,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,5,38,611,8,38,10,
        38,12,38,614,9,38,3,38,616,8,38,1,39,1,39,1,39,1,39,3,39,622,8,39,
        1,39,1,39,1,39,1,39,1,39,1,39,3,39,630,8,39,1,39,1,39,1,39,1,39,
        1,39,1,39,1,39,1,39,1,39,1,39,1,39,5,39,643,8,39,10,39,12,39,646,
        9,39,3,39,648,8,39,1,40,1,40,1,40,1,40,3,40,654,8,40,1,40,1,40,1,
        40,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,
        42,1,42,1,42,1,42,1,42,3,42,676,8,42,1,43,1,43,1,43,1,43,1,43,1,
        43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,5,45,695,
        8,45,10,45,12,45,698,9,45,1,45,1,45,1,46,1,46,1,46,1,46,1,46,1,47,
        1,47,1,47,1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,
        1,49,1,49,0,3,24,56,58,50,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,76,78,80,82,84,86,88,90,92,94,96,98,0,8,5,0,1,1,3,5,7,7,9,12,
        14,14,1,0,69,70,1,0,40,42,1,0,29,30,2,0,48,48,50,53,1,0,56,57,1,
        0,54,55,1,0,45,46,800,0,100,1,0,0,0,2,119,1,0,0,0,4,121,1,0,0,0,
        6,127,1,0,0,0,8,150,1,0,0,0,10,152,1,0,0,0,12,154,1,0,0,0,14,160,
        1,0,0,0,16,172,1,0,0,0,18,212,1,0,0,0,20,214,1,0,0,0,22,251,1,0,
        0,0,24,262,1,0,0,0,26,272,1,0,0,0,28,279,1,0,0,0,30,281,1,0,0,0,
        32,298,1,0,0,0,34,303,1,0,0,0,36,305,1,0,0,0,38,314,1,0,0,0,40,326,
        1,0,0,0,42,338,1,0,0,0,44,340,1,0,0,0,46,344,1,0,0,0,48,350,1,0,
        0,0,50,355,1,0,0,0,52,386,1,0,0,0,54,388,1,0,0,0,56,396,1,0,0,0,
        58,407,1,0,0,0,60,418,1,0,0,0,62,420,1,0,0,0,64,422,1,0,0,0,66,439,
        1,0,0,0,68,441,1,0,0,0,70,446,1,0,0,0,72,518,1,0,0,0,74,583,1,0,
        0,0,76,615,1,0,0,0,78,647,1,0,0,0,80,649,1,0,0,0,82,658,1,0,0,0,
        84,675,1,0,0,0,86,677,1,0,0,0,88,685,1,0,0,0,90,691,1,0,0,0,92,701,
        1,0,0,0,94,706,1,0,0,0,96,709,1,0,0,0,98,714,1,0,0,0,100,101,5,1,
        0,0,101,103,5,74,0,0,102,104,3,2,1,0,103,102,1,0,0,0,104,105,1,0,
        0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,108,3,4,
        2,0,108,1,1,0,0,0,109,112,5,2,0,0,110,113,5,74,0,0,111,113,3,22,
        11,0,112,110,1,0,0,0,112,111,1,0,0,0,113,114,1,0,0,0,114,115,5,59,
        0,0,115,116,3,6,3,0,116,117,5,25,0,0,117,120,1,0,0,0,118,120,3,36,
        18,0,119,109,1,0,0,0,119,118,1,0,0,0,120,3,1,0,0,0,121,122,5,24,
        0,0,122,123,5,59,0,0,123,124,3,6,3,0,124,125,5,25,0,0,125,5,1,0,
        0,0,126,128,3,8,4,0,127,126,1,0,0,0,128,129,1,0,0,0,129,127,1,0,
        0,0,129,130,1,0,0,0,130,7,1,0,0,0,131,151,3,64,32,0,132,151,3,74,
        37,0,133,151,3,66,33,0,134,151,3,68,34,0,135,151,3,70,35,0,136,151,
        3,72,36,0,137,151,3,76,38,0,138,151,3,78,39,0,139,151,3,82,41,0,
        140,151,3,80,40,0,141,151,3,96,48,0,142,151,3,98,49,0,143,151,3,
        28,14,0,144,151,3,84,42,0,145,151,3,86,43,0,146,151,3,88,44,0,147,
        151,3,90,45,0,148,151,3,92,46,0,149,151,3,94,47,0,150,131,1,0,0,
        0,150,132,1,0,0,0,150,133,1,0,0,0,150,134,1,0,0,0,150,135,1,0,0,
        0,150,136,1,0,0,0,150,137,1,0,0,0,150,138,1,0,0,0,150,139,1,0,0,
        0,150,140,1,0,0,0,150,141,1,0,0,0,150,142,1,0,0,0,150,143,1,0,0,
        0,150,144,1,0,0,0,150,145,1,0,0,0,150,146,1,0,0,0,150,147,1,0,0,
        0,150,148,1,0,0,0,150,149,1,0,0,0,151,9,1,0,0,0,152,153,7,0,0,0,
        153,11,1,0,0,0,154,155,7,1,0,0,155,13,1,0,0,0,156,161,3,12,6,0,157,
        161,5,71,0,0,158,161,5,72,0,0,159,161,5,73,0,0,160,156,1,0,0,0,160,
        157,1,0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,161,15,1,0,0,0,162,173,
        3,14,7,0,163,173,3,22,11,0,164,173,3,20,10,0,165,173,5,74,0,0,166,
        167,5,62,0,0,167,168,3,28,14,0,168,169,5,63,0,0,169,173,1,0,0,0,
        170,173,3,38,19,0,171,173,3,30,15,0,172,162,1,0,0,0,172,163,1,0,
        0,0,172,164,1,0,0,0,172,165,1,0,0,0,172,166,1,0,0,0,172,170,1,0,
        0,0,172,171,1,0,0,0,173,17,1,0,0,0,174,175,5,7,0,0,175,176,5,62,
        0,0,176,177,5,74,0,0,177,178,5,60,0,0,178,179,5,5,0,0,179,213,5,
        63,0,0,180,181,7,2,0,0,181,182,5,61,0,0,182,213,3,18,9,0,183,184,
        3,52,26,0,184,185,5,61,0,0,185,186,3,18,9,0,186,213,1,0,0,0,187,
        188,5,74,0,0,188,189,5,61,0,0,189,213,3,18,9,0,190,191,3,14,7,0,
        191,192,5,61,0,0,192,193,3,18,9,0,193,213,1,0,0,0,194,195,3,22,11,
        0,195,196,5,61,0,0,196,197,3,18,9,0,197,213,1,0,0,0,198,199,3,20,
        10,0,199,200,5,61,0,0,200,201,3,18,9,0,201,213,1,0,0,0,202,211,5,
        40,0,0,203,211,5,41,0,0,204,211,5,42,0,0,205,211,5,74,0,0,206,211,
        3,14,7,0,207,211,3,22,11,0,208,211,3,20,10,0,209,211,3,52,26,0,210,
        202,1,0,0,0,210,203,1,0,0,0,210,204,1,0,0,0,210,205,1,0,0,0,210,
        206,1,0,0,0,210,207,1,0,0,0,210,208,1,0,0,0,210,209,1,0,0,0,211,
        213,1,0,0,0,212,174,1,0,0,0,212,180,1,0,0,0,212,183,1,0,0,0,212,
        187,1,0,0,0,212,190,1,0,0,0,212,194,1,0,0,0,212,198,1,0,0,0,212,
        210,1,0,0,0,213,19,1,0,0,0,214,215,5,64,0,0,215,216,3,18,9,0,216,
        217,5,65,0,0,217,21,1,0,0,0,218,219,5,74,0,0,219,220,5,60,0,0,220,
        226,3,10,5,0,221,222,5,60,0,0,222,225,3,10,5,0,223,225,5,74,0,0,
        224,221,1,0,0,0,224,223,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,
        226,227,1,0,0,0,227,252,1,0,0,0,228,226,1,0,0,0,229,230,3,10,5,0,
        230,231,5,60,0,0,231,237,5,74,0,0,232,233,5,60,0,0,233,236,3,10,
        5,0,234,236,5,74,0,0,235,232,1,0,0,0,235,234,1,0,0,0,236,239,1,0,
        0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,252,1,0,0,0,239,237,1,0,
        0,0,240,241,5,74,0,0,241,242,5,60,0,0,242,248,5,74,0,0,243,244,5,
        60,0,0,244,247,3,10,5,0,245,247,5,74,0,0,246,243,1,0,0,0,246,245,
        1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,252,
        1,0,0,0,250,248,1,0,0,0,251,218,1,0,0,0,251,229,1,0,0,0,251,240,
        1,0,0,0,252,23,1,0,0,0,253,254,6,12,-1,0,254,255,5,3,0,0,255,256,
        5,60,0,0,256,263,5,74,0,0,257,258,5,3,0,0,258,259,5,60,0,0,259,260,
        7,3,0,0,260,261,5,60,0,0,261,263,3,12,6,0,262,253,1,0,0,0,262,257,
        1,0,0,0,263,269,1,0,0,0,264,265,10,1,0,0,265,266,5,68,0,0,266,268,
        3,24,12,2,267,264,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,270,
        1,0,0,0,270,25,1,0,0,0,271,269,1,0,0,0,272,273,7,4,0,0,273,27,1,
        0,0,0,274,275,3,32,16,0,275,276,3,62,31,0,276,277,3,28,14,0,277,
        280,1,0,0,0,278,280,3,32,16,0,279,274,1,0,0,0,279,278,1,0,0,0,280,
        29,1,0,0,0,281,282,3,10,5,0,282,283,5,60,0,0,283,284,5,19,0,0,284,
        31,1,0,0,0,285,299,3,52,26,0,286,299,3,60,30,0,287,299,3,46,23,0,
        288,299,3,48,24,0,289,299,3,44,22,0,290,299,3,80,40,0,291,292,3,
        50,25,0,292,293,3,28,14,0,293,299,1,0,0,0,294,299,3,16,8,0,295,296,
        5,47,0,0,296,299,3,28,14,0,297,299,3,30,15,0,298,285,1,0,0,0,298,
        286,1,0,0,0,298,287,1,0,0,0,298,288,1,0,0,0,298,289,1,0,0,0,298,
        290,1,0,0,0,298,291,1,0,0,0,298,294,1,0,0,0,298,295,1,0,0,0,298,
        297,1,0,0,0,299,33,1,0,0,0,300,304,5,74,0,0,301,304,3,22,11,0,302,
        304,3,24,12,0,303,300,1,0,0,0,303,301,1,0,0,0,303,302,1,0,0,0,304,
        35,1,0,0,0,305,306,5,2,0,0,306,307,5,74,0,0,307,308,5,62,0,0,308,
        309,3,18,9,0,309,310,5,63,0,0,310,311,5,59,0,0,311,312,3,6,3,0,312,
        313,5,25,0,0,313,37,1,0,0,0,314,315,3,34,17,0,315,316,5,60,0,0,316,
        317,5,74,0,0,317,321,5,62,0,0,318,320,3,18,9,0,319,318,1,0,0,0,320,
        323,1,0,0,0,321,319,1,0,0,0,321,322,1,0,0,0,322,324,1,0,0,0,323,
        321,1,0,0,0,324,325,5,63,0,0,325,39,1,0,0,0,326,327,5,2,0,0,327,
        328,5,74,0,0,328,330,5,59,0,0,329,331,3,42,21,0,330,329,1,0,0,0,
        331,332,1,0,0,0,332,330,1,0,0,0,332,333,1,0,0,0,333,334,1,0,0,0,
        334,335,5,25,0,0,335,41,1,0,0,0,336,339,3,52,26,0,337,339,3,36,18,
        0,338,336,1,0,0,0,338,337,1,0,0,0,339,43,1,0,0,0,340,341,3,16,8,
        0,341,342,3,26,13,0,342,343,3,16,8,0,343,45,1,0,0,0,344,345,3,16,
        8,0,345,346,5,43,0,0,346,347,3,16,8,0,347,47,1,0,0,0,348,351,5,74,
        0,0,349,351,3,22,11,0,350,348,1,0,0,0,350,349,1,0,0,0,351,352,1,
        0,0,0,352,353,5,44,0,0,353,354,3,24,12,0,354,49,1,0,0,0,355,360,
        5,41,0,0,356,361,5,74,0,0,357,361,3,22,11,0,358,361,3,20,10,0,359,
        361,3,10,5,0,360,356,1,0,0,0,360,357,1,0,0,0,360,358,1,0,0,0,360,
        359,1,0,0,0,361,51,1,0,0,0,362,363,5,74,0,0,363,364,5,49,0,0,364,
        387,3,14,7,0,365,366,5,74,0,0,366,367,5,49,0,0,367,387,3,38,19,0,
        368,374,5,74,0,0,369,370,5,74,0,0,370,371,5,62,0,0,371,372,5,74,
        0,0,372,374,5,63,0,0,373,368,1,0,0,0,373,369,1,0,0,0,374,375,1,0,
        0,0,375,376,5,49,0,0,376,387,3,28,14,0,377,383,5,74,0,0,378,379,
        5,74,0,0,379,380,5,62,0,0,380,381,5,74,0,0,381,383,5,63,0,0,382,
        377,1,0,0,0,382,378,1,0,0,0,383,384,1,0,0,0,384,385,5,49,0,0,385,
        387,3,90,45,0,386,362,1,0,0,0,386,365,1,0,0,0,386,373,1,0,0,0,386,
        382,1,0,0,0,387,53,1,0,0,0,388,393,3,16,8,0,389,390,5,58,0,0,390,
        392,3,16,8,0,391,389,1,0,0,0,392,395,1,0,0,0,393,391,1,0,0,0,393,
        394,1,0,0,0,394,55,1,0,0,0,395,393,1,0,0,0,396,397,6,28,-1,0,397,
        398,3,54,27,0,398,404,1,0,0,0,399,400,10,2,0,0,400,401,7,5,0,0,401,
        403,3,54,27,0,402,399,1,0,0,0,403,406,1,0,0,0,404,402,1,0,0,0,404,
        405,1,0,0,0,405,57,1,0,0,0,406,404,1,0,0,0,407,408,6,29,-1,0,408,
        409,3,56,28,0,409,415,1,0,0,0,410,411,10,2,0,0,411,412,7,6,0,0,412,
        414,3,56,28,0,413,410,1,0,0,0,414,417,1,0,0,0,415,413,1,0,0,0,415,
        416,1,0,0,0,416,59,1,0,0,0,417,415,1,0,0,0,418,419,3,58,29,0,419,
        61,1,0,0,0,420,421,7,7,0,0,421,63,1,0,0,0,422,423,3,10,5,0,423,424,
        5,62,0,0,424,425,3,18,9,0,425,426,5,63,0,0,426,65,1,0,0,0,427,428,
        5,13,0,0,428,429,5,74,0,0,429,430,5,14,0,0,430,431,3,22,11,0,431,
        432,5,44,0,0,432,433,3,24,12,0,433,440,1,0,0,0,434,435,5,15,0,0,
        435,436,5,62,0,0,436,437,3,20,10,0,437,438,5,63,0,0,438,440,1,0,
        0,0,439,427,1,0,0,0,439,434,1,0,0,0,440,67,1,0,0,0,441,442,5,16,
        0,0,442,443,5,62,0,0,443,444,3,28,14,0,444,445,5,63,0,0,445,69,1,
        0,0,0,446,447,5,17,0,0,447,448,5,74,0,0,448,449,5,62,0,0,449,450,
        3,28,14,0,450,451,5,63,0,0,451,71,1,0,0,0,452,460,5,18,0,0,453,461,
        5,74,0,0,454,461,3,22,11,0,455,461,5,40,0,0,456,457,5,62,0,0,457,
        458,3,18,9,0,458,459,5,63,0,0,459,461,1,0,0,0,460,453,1,0,0,0,460,
        454,1,0,0,0,460,455,1,0,0,0,460,456,1,0,0,0,461,462,1,0,0,0,462,
        463,5,19,0,0,463,519,3,12,6,0,464,472,5,18,0,0,465,473,5,74,0,0,
        466,473,3,22,11,0,467,473,5,40,0,0,468,469,5,62,0,0,469,470,3,18,
        9,0,470,471,5,63,0,0,471,473,1,0,0,0,472,465,1,0,0,0,472,466,1,0,
        0,0,472,467,1,0,0,0,472,468,1,0,0,0,473,474,1,0,0,0,474,475,5,20,
        0,0,475,476,5,62,0,0,476,477,3,18,9,0,477,486,5,63,0,0,478,479,5,
        61,0,0,479,480,5,74,0,0,480,481,5,62,0,0,481,482,3,18,9,0,482,483,
        5,63,0,0,483,485,1,0,0,0,484,478,1,0,0,0,485,488,1,0,0,0,486,484,
        1,0,0,0,486,487,1,0,0,0,487,519,1,0,0,0,488,486,1,0,0,0,489,499,
        5,18,0,0,490,500,5,74,0,0,491,500,3,22,11,0,492,500,5,40,0,0,493,
        494,5,62,0,0,494,495,3,18,9,0,495,496,5,63,0,0,496,500,1,0,0,0,497,
        500,5,41,0,0,498,500,5,42,0,0,499,490,1,0,0,0,499,491,1,0,0,0,499,
        492,1,0,0,0,499,493,1,0,0,0,499,497,1,0,0,0,499,498,1,0,0,0,500,
        501,1,0,0,0,501,502,5,20,0,0,502,503,5,62,0,0,503,504,3,28,14,0,
        504,513,5,63,0,0,505,506,5,61,0,0,506,507,5,74,0,0,507,508,5,62,
        0,0,508,509,3,28,14,0,509,510,5,63,0,0,510,512,1,0,0,0,511,505,1,
        0,0,0,512,515,1,0,0,0,513,511,1,0,0,0,513,514,1,0,0,0,514,519,1,
        0,0,0,515,513,1,0,0,0,516,517,5,18,0,0,517,519,3,52,26,0,518,452,
        1,0,0,0,518,464,1,0,0,0,518,489,1,0,0,0,518,516,1,0,0,0,519,73,1,
        0,0,0,520,521,5,13,0,0,521,523,5,74,0,0,522,520,1,0,0,0,523,526,
        1,0,0,0,524,522,1,0,0,0,524,525,1,0,0,0,525,527,1,0,0,0,526,524,
        1,0,0,0,527,531,5,18,0,0,528,532,5,74,0,0,529,532,3,22,11,0,530,
        532,5,40,0,0,531,528,1,0,0,0,531,529,1,0,0,0,531,530,1,0,0,0,532,
        533,1,0,0,0,533,534,5,21,0,0,534,537,5,62,0,0,535,538,3,18,9,0,536,
        538,3,24,12,0,537,535,1,0,0,0,537,536,1,0,0,0,538,539,1,0,0,0,539,
        540,5,63,0,0,540,584,1,0,0,0,541,542,5,13,0,0,542,544,5,74,0,0,543,
        541,1,0,0,0,544,547,1,0,0,0,545,543,1,0,0,0,545,546,1,0,0,0,546,
        548,1,0,0,0,547,545,1,0,0,0,548,552,5,22,0,0,549,553,5,74,0,0,550,
        553,3,22,11,0,551,553,5,40,0,0,552,549,1,0,0,0,552,550,1,0,0,0,552,
        551,1,0,0,0,553,554,1,0,0,0,554,555,5,21,0,0,555,558,5,62,0,0,556,
        559,3,18,9,0,557,559,3,24,12,0,558,556,1,0,0,0,558,557,1,0,0,0,559,
        560,1,0,0,0,560,561,5,63,0,0,561,584,1,0,0,0,562,563,5,13,0,0,563,
        565,5,74,0,0,564,562,1,0,0,0,565,568,1,0,0,0,566,564,1,0,0,0,566,
        567,1,0,0,0,567,569,1,0,0,0,568,566,1,0,0,0,569,573,5,23,0,0,570,
        574,5,74,0,0,571,574,3,22,11,0,572,574,5,40,0,0,573,570,1,0,0,0,
        573,571,1,0,0,0,573,572,1,0,0,0,574,575,1,0,0,0,575,576,5,21,0,0,
        576,579,5,62,0,0,577,580,3,18,9,0,578,580,3,24,12,0,579,577,1,0,
        0,0,579,578,1,0,0,0,580,581,1,0,0,0,581,582,5,63,0,0,582,584,1,0,
        0,0,583,524,1,0,0,0,583,545,1,0,0,0,583,566,1,0,0,0,584,75,1,0,0,
        0,585,589,5,22,0,0,586,590,5,74,0,0,587,590,3,22,11,0,588,590,5,
        40,0,0,589,586,1,0,0,0,589,587,1,0,0,0,589,588,1,0,0,0,590,591,1,
        0,0,0,591,592,5,19,0,0,592,616,3,12,6,0,593,597,5,22,0,0,594,598,
        5,74,0,0,595,598,3,22,11,0,596,598,5,40,0,0,597,594,1,0,0,0,597,
        595,1,0,0,0,597,596,1,0,0,0,598,599,1,0,0,0,599,600,5,20,0,0,600,
        601,5,74,0,0,601,602,5,62,0,0,602,603,3,18,9,0,603,612,5,63,0,0,
        604,605,5,61,0,0,605,606,5,74,0,0,606,607,5,62,0,0,607,608,3,18,
        9,0,608,609,5,63,0,0,609,611,1,0,0,0,610,604,1,0,0,0,611,614,1,0,
        0,0,612,610,1,0,0,0,612,613,1,0,0,0,613,616,1,0,0,0,614,612,1,0,
        0,0,615,585,1,0,0,0,615,593,1,0,0,0,616,77,1,0,0,0,617,621,5,23,
        0,0,618,622,5,74,0,0,619,622,3,22,11,0,620,622,5,40,0,0,621,618,
        1,0,0,0,621,619,1,0,0,0,621,620,1,0,0,0,622,623,1,0,0,0,623,624,
        5,19,0,0,624,648,3,12,6,0,625,629,5,23,0,0,626,630,5,74,0,0,627,
        630,3,22,11,0,628,630,5,40,0,0,629,626,1,0,0,0,629,627,1,0,0,0,629,
        628,1,0,0,0,630,631,1,0,0,0,631,632,5,20,0,0,632,633,5,74,0,0,633,
        634,5,62,0,0,634,635,3,18,9,0,635,644,5,63,0,0,636,637,5,61,0,0,
        637,638,5,74,0,0,638,639,5,62,0,0,639,640,3,18,9,0,640,641,5,63,
        0,0,641,643,1,0,0,0,642,636,1,0,0,0,643,646,1,0,0,0,644,642,1,0,
        0,0,644,645,1,0,0,0,645,648,1,0,0,0,646,644,1,0,0,0,647,617,1,0,
        0,0,647,625,1,0,0,0,648,79,1,0,0,0,649,653,5,26,0,0,650,654,5,74,
        0,0,651,654,3,22,11,0,652,654,5,40,0,0,653,650,1,0,0,0,653,651,1,
        0,0,0,653,652,1,0,0,0,654,655,1,0,0,0,655,656,5,27,0,0,656,657,3,
        24,12,0,657,81,1,0,0,0,658,659,5,28,0,0,659,660,5,74,0,0,660,661,
        3,80,40,0,661,83,1,0,0,0,662,663,5,31,0,0,663,664,3,28,14,0,664,
        665,5,59,0,0,665,666,3,6,3,0,666,667,5,32,0,0,667,668,5,59,0,0,668,
        669,3,6,3,0,669,676,1,0,0,0,670,671,5,31,0,0,671,672,3,28,14,0,672,
        673,5,59,0,0,673,674,3,6,3,0,674,676,1,0,0,0,675,662,1,0,0,0,675,
        670,1,0,0,0,676,85,1,0,0,0,677,678,5,33,0,0,678,679,5,74,0,0,679,
        680,5,43,0,0,680,681,3,20,10,0,681,682,5,59,0,0,682,683,3,6,3,0,
        683,684,5,25,0,0,684,87,1,0,0,0,685,686,5,34,0,0,686,687,3,28,14,
        0,687,688,5,59,0,0,688,689,3,6,3,0,689,690,5,25,0,0,690,89,1,0,0,
        0,691,692,5,35,0,0,692,696,5,62,0,0,693,695,5,72,0,0,694,693,1,0,
        0,0,695,698,1,0,0,0,696,694,1,0,0,0,696,697,1,0,0,0,697,699,1,0,
        0,0,698,696,1,0,0,0,699,700,5,63,0,0,700,91,1,0,0,0,701,702,5,36,
        0,0,702,703,5,62,0,0,703,704,3,18,9,0,704,705,5,63,0,0,705,93,1,
        0,0,0,706,707,5,37,0,0,707,708,3,28,14,0,708,95,1,0,0,0,709,710,
        5,6,0,0,710,711,5,62,0,0,711,712,5,69,0,0,712,713,5,63,0,0,713,97,
        1,0,0,0,714,715,5,8,0,0,715,716,5,62,0,0,716,717,3,12,6,0,717,718,
        5,61,0,0,718,719,3,12,6,0,719,720,5,63,0,0,720,99,1,0,0,0,60,105,
        112,119,129,150,160,172,210,212,224,226,235,237,246,248,251,262,
        269,279,298,303,321,332,338,350,360,373,382,386,393,404,415,439,
        460,472,486,499,513,518,524,531,537,545,552,558,566,573,579,583,
        589,597,612,615,621,629,644,647,653,675,696
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
    RULE_exponent = 27
    RULE_multiplicative = 28
    RULE_additive = 29
    RULE_math_expression = 30
    RULE_logical_opt = 31
    RULE_game_entities_statement = 32
    RULE_player_statement = 33
    RULE_condition_statement = 34
    RULE_rule_statement = 35
    RULE_piece_statement = 36
    RULE_board_statement = 37
    RULE_obstacle_statement = 38
    RULE_booster_statement = 39
    RULE_move_statement = 40
    RULE_turn_statement = 41
    RULE_if_statement = 42
    RULE_for_statement = 43
    RULE_while_statement = 44
    RULE_input_statement = 45
    RULE_print_statement = 46
    RULE_return_statement = 47
    RULE_timer_statement = 48
    RULE_dice_statement = 49

    ruleNames =  [ "program", "define_block", "gameplay_block", "code_block", 
                   "statement", "game_entities", "int_literal", "literal", 
                   "primary", "param_list", "list", "object_access", "board_pos", 
                   "conditional_opt", "expression", "entity_count_expression", 
                   "base_expression", "objects", "method_declaration", "method_call", 
                   "class_define_block", "class_statement", "conditional_expression", 
                   "in_expression", "at_expression", "any_expression", "assignment_expression", 
                   "exponent", "multiplicative", "additive", "math_expression", 
                   "logical_opt", "game_entities_statement", "player_statement", 
                   "condition_statement", "rule_statement", "piece_statement", 
                   "board_statement", "obstacle_statement", "booster_statement", 
                   "move_statement", "turn_statement", "if_statement", "for_statement", 
                   "while_statement", "input_statement", "print_statement", 
                   "return_statement", "timer_statement", "dice_statement" ]

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
            self.state = 100
            self.match(BoardGameParser.GAME)
            self.state = 101
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.define_block()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 107
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
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = BoardGameParser.DefineContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(BoardGameParser.DEFINE)
                self.state = 112
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 110
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 111
                    self.object_access()
                    pass


                self.state = 114
                self.match(BoardGameParser.COLON)
                self.state = 115
                self.code_block()
                self.state = 116
                self.match(BoardGameParser.END)
                pass

            elif la_ == 2:
                localctx = BoardGameParser.MethodDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 118
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
            self.state = 121
            self.match(BoardGameParser.START)
            self.state = 122
            self.match(BoardGameParser.COLON)
            self.state = 123
            self.code_block()
            self.state = 124
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
            self.state = 127 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 126
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 129 
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


        def timer_statement(self):
            return self.getTypedRuleContext(BoardGameParser.Timer_statementContext,0)


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
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.game_entities_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.board_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.player_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.condition_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.rule_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 136
                self.piece_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 137
                self.obstacle_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 138
                self.booster_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 139
                self.turn_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 140
                self.move_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 141
                self.timer_statement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 142
                self.dice_statement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 143
                self.expression()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 144
                self.if_statement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 145
                self.for_statement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 146
                self.while_statement()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 147
                self.input_statement()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 148
                self.print_statement()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 149
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
            self.state = 152
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24250) != 0)):
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
            self.state = 154
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
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [69, 70]:
                localctx = BoardGameParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.int_literal()
                pass
            elif token in [71]:
                localctx = BoardGameParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(BoardGameParser.FLOAT_LITERAL)
                pass
            elif token in [72]:
                localctx = BoardGameParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.match(BoardGameParser.STRING_LITERAL)
                pass
            elif token in [73]:
                localctx = BoardGameParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 159
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
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.object_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.list_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 167
                self.expression()
                self.state = 168
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 170
                self.method_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 171
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

        def assignment_expression(self):
            return self.getTypedRuleContext(BoardGameParser.Assignment_expressionContext,0)


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
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = BoardGameParser.ScoreParamContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(BoardGameParser.SCORE)
                self.state = 175
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 176
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 177
                self.match(BoardGameParser.DOT)
                self.state = 178
                self.match(BoardGameParser.CONDITIONS)
                self.state = 179
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                localctx = BoardGameParser.AllAnyNoneParamContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581394432) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 181
                self.match(BoardGameParser.COMMA)
                self.state = 182
                self.param_list()
                pass

            elif la_ == 3:
                localctx = BoardGameParser.AssignmentParamContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.assignment_expression()
                self.state = 184
                self.match(BoardGameParser.COMMA)
                self.state = 185
                self.param_list()
                pass

            elif la_ == 4:
                localctx = BoardGameParser.VariableParamContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 188
                self.match(BoardGameParser.COMMA)
                self.state = 189
                self.param_list()
                pass

            elif la_ == 5:
                localctx = BoardGameParser.LiteralParamContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.literal()
                self.state = 191
                self.match(BoardGameParser.COMMA)
                self.state = 192
                self.param_list()
                pass

            elif la_ == 6:
                localctx = BoardGameParser.ObjectAccessParamContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 194
                self.object_access()
                self.state = 195
                self.match(BoardGameParser.COMMA)
                self.state = 196
                self.param_list()
                pass

            elif la_ == 7:
                localctx = BoardGameParser.ListLiteralParamContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 198
                self.list_()
                self.state = 199
                self.match(BoardGameParser.COMMA)
                self.state = 200
                self.param_list()
                pass

            elif la_ == 8:
                localctx = BoardGameParser.SingleParamContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 210
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 202
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 2:
                    self.state = 203
                    self.match(BoardGameParser.ANY)
                    pass

                elif la_ == 3:
                    self.state = 204
                    self.match(BoardGameParser.NONE)
                    pass

                elif la_ == 4:
                    self.state = 205
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 5:
                    self.state = 206
                    self.literal()
                    pass

                elif la_ == 6:
                    self.state = 207
                    self.object_access()
                    pass

                elif la_ == 7:
                    self.state = 208
                    self.list_()
                    pass

                elif la_ == 8:
                    self.state = 209
                    self.assignment_expression()
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
            self.state = 214
            self.match(BoardGameParser.OPEN_BRACKET)
            self.state = 215
            self.param_list()
            self.state = 216
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_access" ):
                return visitor.visitObject_access(self)
            else:
                return visitor.visitChildren(self)




    def object_access(self):

        localctx = BoardGameParser.Object_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_object_access)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 219
                self.match(BoardGameParser.DOT)
                self.state = 220
                self.game_entities()
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 224
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [60]:
                            self.state = 221
                            self.match(BoardGameParser.DOT)
                            self.state = 222
                            self.game_entities()
                            pass
                        elif token in [74]:
                            self.state = 223
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 228
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.game_entities()
                self.state = 230
                self.match(BoardGameParser.DOT)
                self.state = 231
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 235
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [60]:
                            self.state = 232
                            self.match(BoardGameParser.DOT)
                            self.state = 233
                            self.game_entities()
                            pass
                        elif token in [74]:
                            self.state = 234
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 239
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 241
                self.match(BoardGameParser.DOT)
                self.state = 242
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 246
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [60]:
                            self.state = 243
                            self.match(BoardGameParser.DOT)
                            self.state = 244
                            self.game_entities()
                            pass
                        elif token in [74]:
                            self.state = 245
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 250
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


    class BoardPosRosColContext(Board_posContext):

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
            if hasattr( listener, "enterBoardPosRosCol" ):
                listener.enterBoardPosRosCol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoardPosRosCol" ):
                listener.exitBoardPosRosCol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoardPosRosCol" ):
                return visitor.visitBoardPosRosCol(self)
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
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = BoardGameParser.BoardPosIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 254
                self.match(BoardGameParser.BOARD)
                self.state = 255
                self.match(BoardGameParser.DOT)
                self.state = 256
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = BoardGameParser.BoardPosRosColContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 257
                self.match(BoardGameParser.BOARD)
                self.state = 258
                self.match(BoardGameParser.DOT)
                self.state = 259
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 260
                self.match(BoardGameParser.DOT)

                self.state = 261
                self.int_literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.BoardPosRangeContext(self, BoardGameParser.Board_posContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_board_pos)
                    self.state = 264
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 265
                    self.match(BoardGameParser.ELIPSIS)
                    self.state = 266
                    self.board_pos(2) 
                self.state = 271
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
            self.state = 272
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
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.base_expression()
                self.state = 275
                self.logical_opt()
                self.state = 276
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
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

        def game_entities(self):
            return self.getTypedRuleContext(BoardGameParser.Game_entitiesContext,0)


        def DOT(self):
            return self.getToken(BoardGameParser.DOT, 0)

        def COUNT(self):
            return self.getToken(BoardGameParser.COUNT, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_entity_count_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity_count_expression" ):
                listener.enterEntity_count_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity_count_expression" ):
                listener.exitEntity_count_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntity_count_expression" ):
                return visitor.visitEntity_count_expression(self)
            else:
                return visitor.visitChildren(self)




    def entity_count_expression(self):

        localctx = BoardGameParser.Entity_count_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_entity_count_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.game_entities()
            self.state = 282
            self.match(BoardGameParser.DOT)
            self.state = 283
            self.match(BoardGameParser.COUNT)
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


        def primary(self):
            return self.getTypedRuleContext(BoardGameParser.PrimaryContext,0)


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
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.assignment_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.math_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.in_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 288
                self.at_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 289
                self.conditional_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 290
                self.move_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 291
                self.any_expression()
                self.state = 292
                self.expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 294
                self.primary()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 295
                self.match(BoardGameParser.NOT_OPT)
                self.state = 296
                self.expression()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 297
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjects" ):
                return visitor.visitObjects(self)
            else:
                return visitor.visitChildren(self)




    def objects(self):

        localctx = BoardGameParser.ObjectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_objects)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.object_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.board_pos(0)
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
            self.state = 305
            self.match(BoardGameParser.DEFINE)
            self.state = 306
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 307
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 308
            self.param_list()
            self.state = 309
            self.match(BoardGameParser.CLOSE_PAR)
            self.state = 310
            self.match(BoardGameParser.COLON)
            self.state = 311
            self.code_block()
            self.state = 312
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
            self.state = 314
            self.objects()
            self.state = 315
            self.match(BoardGameParser.DOT)
            self.state = 316
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 317
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581418682) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 2017) != 0):
                self.state = 318
                self.param_list()
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 324
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
            self.state = 326
            self.match(BoardGameParser.DEFINE)
            self.state = 327
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 328
            self.match(BoardGameParser.COLON)
            self.state = 330 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 329
                self.class_statement()
                self.state = 332 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==74):
                    break

            self.state = 334
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
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [74]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.assignment_expression()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_expression" ):
                return visitor.visitConditional_expression(self)
            else:
                return visitor.visitChildren(self)




    def conditional_expression(self):

        localctx = BoardGameParser.Conditional_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_conditional_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.primary()
            self.state = 341
            self.conditional_opt()
            self.state = 342
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
            self.state = 344
            self.primary()
            self.state = 345
            self.match(BoardGameParser.IN)
            self.state = 346
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
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 348
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 349
                self.object_access()
                pass


            self.state = 352
            self.match(BoardGameParser.AT)
            self.state = 353
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
            self.state = 355
            self.match(BoardGameParser.ANY)
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 356
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 357
                self.object_access()
                pass

            elif la_ == 3:
                self.state = 358
                self.list_()
                pass

            elif la_ == 4:
                self.state = 359
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BoardGameParser.IDENTIFIER)
            else:
                return self.getToken(BoardGameParser.IDENTIFIER, i)

        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)

        def literal(self):
            return self.getTypedRuleContext(BoardGameParser.LiteralContext,0)


        def method_call(self):
            return self.getTypedRuleContext(BoardGameParser.Method_callContext,0)


        def expression(self):
            return self.getTypedRuleContext(BoardGameParser.ExpressionContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_expression" ):
                return visitor.visitAssignment_expression(self)
            else:
                return visitor.visitChildren(self)




    def assignment_expression(self):

        localctx = BoardGameParser.Assignment_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignment_expression)
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 363
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 364
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 366
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 367
                self.method_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 373
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 368
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 369
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 370
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 371
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 372
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 375
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 376
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 382
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 377
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 378
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 379
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 380
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 381
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 384
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 385
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponent" ):
                return visitor.visitExponent(self)
            else:
                return visitor.visitChildren(self)




    def exponent(self):

        localctx = BoardGameParser.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exponent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.primary()
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 389
                    self.match(BoardGameParser.EXP_OPT)
                    self.state = 390
                    self.primary() 
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)



    def multiplicative(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BoardGameParser.MultiplicativeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_multiplicative, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.exponent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 404
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.MultiplicativeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative)
                    self.state = 399
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 400
                    _la = self._input.LA(1)
                    if not(_la==56 or _la==57):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 401
                    self.exponent() 
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)



    def additive(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BoardGameParser.AdditiveContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_additive, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.multiplicative(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.AdditiveContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                    self.state = 410
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 411
                    _la = self._input.LA(1)
                    if not(_la==54 or _la==55):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 412
                    self.multiplicative(0) 
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_expression" ):
                return visitor.visitMath_expression(self)
            else:
                return visitor.visitChildren(self)




    def math_expression(self):

        localctx = BoardGameParser.Math_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_math_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_opt" ):
                return visitor.visitLogical_opt(self)
            else:
                return visitor.visitChildren(self)




    def logical_opt(self):

        localctx = BoardGameParser.Logical_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_logical_opt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGame_entities_statement" ):
                return visitor.visitGame_entities_statement(self)
            else:
                return visitor.visitChildren(self)




    def game_entities_statement(self):

        localctx = BoardGameParser.Game_entities_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_game_entities_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.game_entities()
            self.state = 423
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 424
            self.param_list()
            self.state = 425
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayer_statement" ):
                return visitor.visitPlayer_statement(self)
            else:
                return visitor.visitChildren(self)




    def player_statement(self):

        localctx = BoardGameParser.Player_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_player_statement)
        try:
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(BoardGameParser.PLAYER)
                self.state = 428
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 429
                self.match(BoardGameParser.COLOR)
                self.state = 430
                self.object_access()
                self.state = 431
                self.match(BoardGameParser.AT)
                self.state = 432
                self.board_pos(0)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.match(BoardGameParser.ORDER)
                self.state = 435
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 436
                self.list_()
                self.state = 437
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
        self.enterRule(localctx, 68, self.RULE_condition_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(BoardGameParser.CONDITION)
            self.state = 442
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 443
            self.expression()
            self.state = 444
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
        self.enterRule(localctx, 70, self.RULE_rule_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(BoardGameParser.RULE)
            self.state = 447
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 448
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 449
            self.expression()
            self.state = 450
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
        self.enterRule(localctx, 72, self.RULE_piece_statement)
        self._la = 0 # Token type
        try:
            self.state = 518
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.match(BoardGameParser.PIECE)
                self.state = 460
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 453
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 454
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 455
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 4:
                    self.state = 456
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 457
                    self.param_list()
                    self.state = 458
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 462
                self.match(BoardGameParser.COUNT)
                self.state = 463
                self.int_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.match(BoardGameParser.PIECE)
                self.state = 472
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 465
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 466
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 467
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 4:
                    self.state = 468
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 469
                    self.param_list()
                    self.state = 470
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 474
                self.match(BoardGameParser.ACTION)
                self.state = 475
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 476
                self.param_list()
                self.state = 477
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 486
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 478
                    self.match(BoardGameParser.COMMA)
                    self.state = 479
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 480
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 481
                    self.param_list()
                    self.state = 482
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 488
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 489
                self.match(BoardGameParser.PIECE)
                self.state = 499
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 490
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 491
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 492
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 4:
                    self.state = 493
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 494
                    self.param_list()
                    self.state = 495
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass

                elif la_ == 5:
                    self.state = 497
                    self.match(BoardGameParser.ANY)
                    pass

                elif la_ == 6:
                    self.state = 498
                    self.match(BoardGameParser.NONE)
                    pass


                self.state = 501
                self.match(BoardGameParser.ACTION)
                self.state = 502
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 503
                self.expression()
                self.state = 504
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 505
                    self.match(BoardGameParser.COMMA)
                    self.state = 506
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 507
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 508
                    self.expression()
                    self.state = 509
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 515
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 516
                self.match(BoardGameParser.PIECE)
                self.state = 517
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoard_statement" ):
                return visitor.visitBoard_statement(self)
            else:
                return visitor.visitChildren(self)




    def board_statement(self):

        localctx = BoardGameParser.Board_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_board_statement)
        self._la = 0 # Token type
        try:
            self.state = 583
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 520
                    self.match(BoardGameParser.PLAYER)
                    self.state = 521
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 526
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 527
                self.match(BoardGameParser.PIECE)
                self.state = 531
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 528
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 529
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 530
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 533
                self.match(BoardGameParser.SETUP)
                self.state = 534
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 537
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                if la_ == 1:
                    self.state = 535
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 536
                    self.board_pos(0)
                    pass


                self.state = 539
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 545
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 541
                    self.match(BoardGameParser.PLAYER)
                    self.state = 542
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 547
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 548
                self.match(BoardGameParser.OBSTACLE)
                self.state = 552
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 549
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 550
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 551
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 554
                self.match(BoardGameParser.SETUP)
                self.state = 555
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 558
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 556
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 557
                    self.board_pos(0)
                    pass


                self.state = 560
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 566
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 562
                    self.match(BoardGameParser.PLAYER)
                    self.state = 563
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 568
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 569
                self.match(BoardGameParser.BOOSTER)
                self.state = 573
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 570
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 571
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 572
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 575
                self.match(BoardGameParser.SETUP)
                self.state = 576
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 579
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 577
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 578
                    self.board_pos(0)
                    pass


                self.state = 581
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
        self.enterRule(localctx, 76, self.RULE_obstacle_statement)
        self._la = 0 # Token type
        try:
            self.state = 615
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 585
                self.match(BoardGameParser.OBSTACLE)
                self.state = 589
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 586
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 587
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 588
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 591
                self.match(BoardGameParser.COUNT)
                self.state = 592
                self.int_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 593
                self.match(BoardGameParser.OBSTACLE)
                self.state = 597
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 594
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 595
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 596
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 599
                self.match(BoardGameParser.ACTION)
                self.state = 600
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 601
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 602
                self.param_list()
                self.state = 603
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 612
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 604
                    self.match(BoardGameParser.COMMA)
                    self.state = 605
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 606
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 607
                    self.param_list()
                    self.state = 608
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 614
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
        self.enterRule(localctx, 78, self.RULE_booster_statement)
        self._la = 0 # Token type
        try:
            self.state = 647
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 617
                self.match(BoardGameParser.BOOSTER)
                self.state = 621
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 618
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 619
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 620
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 623
                self.match(BoardGameParser.COUNT)
                self.state = 624
                self.int_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 625
                self.match(BoardGameParser.BOOSTER)
                self.state = 629
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                if la_ == 1:
                    self.state = 626
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 627
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 628
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 631
                self.match(BoardGameParser.ACTION)
                self.state = 632
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 633
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 634
                self.param_list()
                self.state = 635
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 644
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 636
                    self.match(BoardGameParser.COMMA)
                    self.state = 637
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 638
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 639
                    self.param_list()
                    self.state = 640
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 646
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
        self.enterRule(localctx, 80, self.RULE_move_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.match(BoardGameParser.MOVE)
            self.state = 653
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 650
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 651
                self.object_access()
                pass

            elif la_ == 3:
                self.state = 652
                self.match(BoardGameParser.ALL)
                pass


            self.state = 655
            self.match(BoardGameParser.TO)
            self.state = 656
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
        self.enterRule(localctx, 82, self.RULE_turn_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            self.match(BoardGameParser.TURN)
            self.state = 659
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 660
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
        self.enterRule(localctx, 84, self.RULE_if_statement)
        try:
            self.state = 675
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 662
                self.match(BoardGameParser.IF)
                self.state = 663
                self.expression()
                self.state = 664
                self.match(BoardGameParser.COLON)
                self.state = 665
                self.code_block()
                self.state = 666
                self.match(BoardGameParser.ELSE)
                self.state = 667
                self.match(BoardGameParser.COLON)
                self.state = 668
                self.code_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 670
                self.match(BoardGameParser.IF)
                self.state = 671
                self.expression()
                self.state = 672
                self.match(BoardGameParser.COLON)
                self.state = 673
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
        self.enterRule(localctx, 86, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
            self.match(BoardGameParser.FOR)
            self.state = 678
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 679
            self.match(BoardGameParser.IN)
            self.state = 680
            self.list_()
            self.state = 681
            self.match(BoardGameParser.COLON)
            self.state = 682
            self.code_block()
            self.state = 683
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
        self.enterRule(localctx, 88, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self.match(BoardGameParser.WHILE)
            self.state = 686
            self.expression()
            self.state = 687
            self.match(BoardGameParser.COLON)
            self.state = 688
            self.code_block()
            self.state = 689
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_statement" ):
                return visitor.visitInput_statement(self)
            else:
                return visitor.visitChildren(self)




    def input_statement(self):

        localctx = BoardGameParser.Input_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_input_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 691
            self.match(BoardGameParser.INPUT)
            self.state = 692
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 696
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==72:
                self.state = 693
                self.match(BoardGameParser.STRING_LITERAL)
                self.state = 698
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 699
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
        self.enterRule(localctx, 92, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 701
            self.match(BoardGameParser.PRINT)
            self.state = 702
            self.match(BoardGameParser.OPEN_PAR)

            self.state = 703
            self.param_list()
            self.state = 704
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
        self.enterRule(localctx, 94, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(BoardGameParser.RETURN)
            self.state = 707
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimer_statement" ):
                return visitor.visitTimer_statement(self)
            else:
                return visitor.visitChildren(self)




    def timer_statement(self):

        localctx = BoardGameParser.Timer_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_timer_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            self.match(BoardGameParser.TIMER)
            self.state = 710
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 711
            self.match(BoardGameParser.POSITIVE_INT_LITERAL)
            self.state = 712
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDice_statement" ):
                return visitor.visitDice_statement(self)
            else:
                return visitor.visitChildren(self)




    def dice_statement(self):

        localctx = BoardGameParser.Dice_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_dice_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self.match(BoardGameParser.DICE)
            self.state = 715
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 716
            self.int_literal()
            self.state = 717
            self.match(BoardGameParser.COMMA)
            self.state = 718
            self.int_literal()
            self.state = 719
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
        self._predicates[28] = self.multiplicative_sempred
        self._predicates[29] = self.additive_sempred
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
         




