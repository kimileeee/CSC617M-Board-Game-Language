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
        4,1,77,756,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,1,0,1,0,1,0,4,
        0,94,8,0,11,0,12,0,95,1,0,1,0,1,1,1,1,1,1,3,1,103,8,1,1,1,1,1,1,
        1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,4,3,115,8,3,11,3,12,3,116,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,138,8,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,3,7,148,8,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,159,8,8,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,5,9,170,8,9,10,9,12,9,173,9,9,1,9,1,9,1,9,5,9,178,
        8,9,10,9,12,9,181,9,9,1,9,1,9,1,9,5,9,186,8,9,10,9,12,9,189,9,9,
        1,9,1,9,1,9,1,9,1,9,5,9,196,8,9,10,9,12,9,199,9,9,1,9,1,9,1,9,1,
        9,1,9,5,9,206,8,9,10,9,12,9,209,9,9,1,9,1,9,1,9,5,9,214,8,9,10,9,
        12,9,217,9,9,1,9,1,9,1,9,5,9,222,8,9,10,9,12,9,225,9,9,1,9,1,9,1,
        9,5,9,230,8,9,10,9,12,9,233,9,9,1,9,1,9,1,9,5,9,238,8,9,10,9,12,
        9,241,9,9,3,9,243,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
        11,1,11,5,11,255,8,11,10,11,12,11,258,9,11,1,11,1,11,1,11,1,11,1,
        11,1,11,5,11,266,8,11,10,11,12,11,269,9,11,1,11,1,11,1,11,1,11,1,
        11,1,11,5,11,277,8,11,10,11,12,11,280,9,11,3,11,282,8,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,293,8,12,1,12,1,12,1,
        12,5,12,298,8,12,10,12,12,12,301,9,12,1,13,1,13,1,14,1,14,1,14,1,
        14,5,14,309,8,14,10,14,12,14,312,9,14,1,14,1,14,1,14,1,14,5,14,318,
        8,14,10,14,12,14,321,9,14,1,14,1,14,1,14,1,14,5,14,327,8,14,10,14,
        12,14,330,9,14,1,14,1,14,1,14,1,14,5,14,336,8,14,10,14,12,14,339,
        9,14,1,14,1,14,1,14,1,14,1,14,5,14,346,8,14,10,14,12,14,349,9,14,
        1,14,1,14,1,14,1,14,5,14,355,8,14,10,14,12,14,358,9,14,1,14,1,14,
        1,14,1,14,1,14,5,14,365,8,14,10,14,12,14,368,9,14,1,14,1,14,1,14,
        1,14,5,14,374,8,14,10,14,12,14,377,9,14,1,14,1,14,1,14,1,14,5,14,
        383,8,14,10,14,12,14,386,9,14,3,14,388,8,14,1,15,1,15,1,15,3,15,
        393,8,15,1,16,1,16,1,16,1,16,1,16,5,16,400,8,16,10,16,12,16,403,
        9,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,
        3,19,417,8,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,3,20,427,8,
        20,1,21,1,21,1,21,1,21,1,21,3,21,434,8,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,3,21,443,8,21,1,21,1,21,3,21,447,8,21,1,22,1,22,1,22,
        5,22,452,8,22,10,22,12,22,455,9,22,1,23,1,23,1,23,1,23,1,23,1,23,
        5,23,463,8,23,10,23,12,23,466,9,23,1,24,1,24,1,24,1,24,1,24,1,24,
        5,24,474,8,24,10,24,12,24,477,9,24,1,25,1,25,1,26,1,26,1,27,1,27,
        1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,3,28,500,8,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,
        1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,521,
        8,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,533,
        8,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,
        546,8,31,10,31,12,31,549,9,31,1,31,1,31,3,31,553,8,31,1,32,1,32,
        5,32,557,8,32,10,32,12,32,560,9,32,1,32,1,32,1,32,1,32,3,32,566,
        8,32,1,32,1,32,1,32,1,32,3,32,572,8,32,1,32,1,32,1,32,1,32,5,32,
        578,8,32,10,32,12,32,581,9,32,1,32,1,32,1,32,1,32,3,32,587,8,32,
        1,32,1,32,1,32,1,32,3,32,593,8,32,1,32,1,32,1,32,1,32,5,32,599,8,
        32,10,32,12,32,602,9,32,1,32,1,32,1,32,1,32,3,32,608,8,32,1,32,1,
        32,1,32,1,32,3,32,614,8,32,1,32,1,32,3,32,618,8,32,1,33,1,33,1,33,
        1,33,3,33,624,8,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,632,8,33,1,
        33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,5,33,645,8,
        33,10,33,12,33,648,9,33,3,33,650,8,33,1,34,1,34,1,34,1,34,3,34,656,
        8,34,1,34,1,34,1,34,1,34,1,34,1,34,3,34,664,8,34,1,34,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,5,34,677,8,34,10,34,12,34,
        680,9,34,3,34,682,8,34,1,35,1,35,1,35,1,35,3,35,688,8,35,1,35,1,
        35,1,35,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,
        37,1,37,1,37,1,37,1,37,1,37,3,37,710,8,37,1,38,1,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,5,
        40,729,8,40,10,40,12,40,732,9,40,1,40,1,40,1,41,1,41,1,41,1,41,1,
        41,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,
        44,1,44,1,44,1,44,0,3,24,46,48,45,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,70,72,74,76,78,80,82,84,86,88,0,7,4,0,3,5,7,7,9,12,14,14,1,0,
        69,70,1,0,29,30,2,0,48,48,50,53,1,0,56,57,1,0,54,55,1,0,45,46,837,
        0,90,1,0,0,0,2,99,1,0,0,0,4,108,1,0,0,0,6,114,1,0,0,0,8,137,1,0,
        0,0,10,139,1,0,0,0,12,141,1,0,0,0,14,147,1,0,0,0,16,158,1,0,0,0,
        18,242,1,0,0,0,20,244,1,0,0,0,22,281,1,0,0,0,24,292,1,0,0,0,26,302,
        1,0,0,0,28,387,1,0,0,0,30,392,1,0,0,0,32,394,1,0,0,0,34,406,1,0,
        0,0,36,410,1,0,0,0,38,416,1,0,0,0,40,421,1,0,0,0,42,446,1,0,0,0,
        44,448,1,0,0,0,46,456,1,0,0,0,48,467,1,0,0,0,50,478,1,0,0,0,52,480,
        1,0,0,0,54,482,1,0,0,0,56,499,1,0,0,0,58,501,1,0,0,0,60,506,1,0,
        0,0,62,552,1,0,0,0,64,617,1,0,0,0,66,649,1,0,0,0,68,681,1,0,0,0,
        70,683,1,0,0,0,72,692,1,0,0,0,74,709,1,0,0,0,76,711,1,0,0,0,78,719,
        1,0,0,0,80,725,1,0,0,0,82,735,1,0,0,0,84,740,1,0,0,0,86,743,1,0,
        0,0,88,748,1,0,0,0,90,91,5,1,0,0,91,93,5,74,0,0,92,94,3,2,1,0,93,
        92,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,
        0,97,98,3,4,2,0,98,1,1,0,0,0,99,102,5,2,0,0,100,103,5,74,0,0,101,
        103,3,22,11,0,102,100,1,0,0,0,102,101,1,0,0,0,103,104,1,0,0,0,104,
        105,5,59,0,0,105,106,3,6,3,0,106,107,5,25,0,0,107,3,1,0,0,0,108,
        109,5,24,0,0,109,110,5,59,0,0,110,111,3,6,3,0,111,112,5,25,0,0,112,
        5,1,0,0,0,113,115,3,8,4,0,114,113,1,0,0,0,115,116,1,0,0,0,116,114,
        1,0,0,0,116,117,1,0,0,0,117,7,1,0,0,0,118,138,3,54,27,0,119,138,
        3,64,32,0,120,138,3,56,28,0,121,138,3,58,29,0,122,138,3,60,30,0,
        123,138,3,62,31,0,124,138,3,66,33,0,125,138,3,68,34,0,126,138,3,
        72,36,0,127,138,3,70,35,0,128,138,3,86,43,0,129,138,3,88,44,0,130,
        138,3,28,14,0,131,138,3,74,37,0,132,138,3,76,38,0,133,138,3,78,39,
        0,134,138,3,80,40,0,135,138,3,82,41,0,136,138,3,84,42,0,137,118,
        1,0,0,0,137,119,1,0,0,0,137,120,1,0,0,0,137,121,1,0,0,0,137,122,
        1,0,0,0,137,123,1,0,0,0,137,124,1,0,0,0,137,125,1,0,0,0,137,126,
        1,0,0,0,137,127,1,0,0,0,137,128,1,0,0,0,137,129,1,0,0,0,137,130,
        1,0,0,0,137,131,1,0,0,0,137,132,1,0,0,0,137,133,1,0,0,0,137,134,
        1,0,0,0,137,135,1,0,0,0,137,136,1,0,0,0,138,9,1,0,0,0,139,140,7,
        0,0,0,140,11,1,0,0,0,141,142,7,1,0,0,142,13,1,0,0,0,143,148,3,12,
        6,0,144,148,5,71,0,0,145,148,5,72,0,0,146,148,5,73,0,0,147,143,1,
        0,0,0,147,144,1,0,0,0,147,145,1,0,0,0,147,146,1,0,0,0,148,15,1,0,
        0,0,149,159,3,14,7,0,150,159,3,22,11,0,151,159,3,20,10,0,152,159,
        5,74,0,0,153,154,5,62,0,0,154,155,3,28,14,0,155,156,5,63,0,0,156,
        159,1,0,0,0,157,159,3,32,16,0,158,149,1,0,0,0,158,150,1,0,0,0,158,
        151,1,0,0,0,158,152,1,0,0,0,158,153,1,0,0,0,158,157,1,0,0,0,159,
        17,1,0,0,0,160,161,5,7,0,0,161,162,5,62,0,0,162,163,5,74,0,0,163,
        164,5,60,0,0,164,165,5,5,0,0,165,243,5,63,0,0,166,171,5,40,0,0,167,
        168,5,61,0,0,168,170,3,18,9,0,169,167,1,0,0,0,170,173,1,0,0,0,171,
        169,1,0,0,0,171,172,1,0,0,0,172,243,1,0,0,0,173,171,1,0,0,0,174,
        179,5,41,0,0,175,176,5,61,0,0,176,178,3,18,9,0,177,175,1,0,0,0,178,
        181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,243,1,0,0,0,181,
        179,1,0,0,0,182,187,5,42,0,0,183,184,5,61,0,0,184,186,3,18,9,0,185,
        183,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,
        243,1,0,0,0,189,187,1,0,0,0,190,191,5,74,0,0,191,192,5,49,0,0,192,
        197,3,14,7,0,193,194,5,61,0,0,194,196,3,18,9,0,195,193,1,0,0,0,196,
        199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,243,1,0,0,0,199,
        197,1,0,0,0,200,201,5,74,0,0,201,202,5,49,0,0,202,207,3,30,15,0,
        203,204,5,61,0,0,204,206,3,18,9,0,205,203,1,0,0,0,206,209,1,0,0,
        0,207,205,1,0,0,0,207,208,1,0,0,0,208,243,1,0,0,0,209,207,1,0,0,
        0,210,215,5,74,0,0,211,212,5,61,0,0,212,214,3,18,9,0,213,211,1,0,
        0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,243,1,0,
        0,0,217,215,1,0,0,0,218,223,3,14,7,0,219,220,5,61,0,0,220,222,3,
        18,9,0,221,219,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,
        0,0,0,224,243,1,0,0,0,225,223,1,0,0,0,226,231,3,22,11,0,227,228,
        5,61,0,0,228,230,3,18,9,0,229,227,1,0,0,0,230,233,1,0,0,0,231,229,
        1,0,0,0,231,232,1,0,0,0,232,243,1,0,0,0,233,231,1,0,0,0,234,239,
        3,20,10,0,235,236,5,61,0,0,236,238,3,18,9,0,237,235,1,0,0,0,238,
        241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,243,1,0,0,0,241,
        239,1,0,0,0,242,160,1,0,0,0,242,166,1,0,0,0,242,174,1,0,0,0,242,
        182,1,0,0,0,242,190,1,0,0,0,242,200,1,0,0,0,242,210,1,0,0,0,242,
        218,1,0,0,0,242,226,1,0,0,0,242,234,1,0,0,0,243,19,1,0,0,0,244,245,
        5,64,0,0,245,246,3,18,9,0,246,247,5,65,0,0,247,21,1,0,0,0,248,249,
        5,74,0,0,249,250,5,60,0,0,250,256,3,10,5,0,251,252,5,60,0,0,252,
        255,3,10,5,0,253,255,5,74,0,0,254,251,1,0,0,0,254,253,1,0,0,0,255,
        258,1,0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,282,1,0,0,0,258,
        256,1,0,0,0,259,260,3,10,5,0,260,261,5,60,0,0,261,267,5,74,0,0,262,
        263,5,60,0,0,263,266,3,10,5,0,264,266,5,74,0,0,265,262,1,0,0,0,265,
        264,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,
        282,1,0,0,0,269,267,1,0,0,0,270,271,5,74,0,0,271,272,5,60,0,0,272,
        278,5,74,0,0,273,274,5,60,0,0,274,277,3,10,5,0,275,277,5,74,0,0,
        276,273,1,0,0,0,276,275,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,
        278,279,1,0,0,0,279,282,1,0,0,0,280,278,1,0,0,0,281,248,1,0,0,0,
        281,259,1,0,0,0,281,270,1,0,0,0,282,23,1,0,0,0,283,284,6,12,-1,0,
        284,285,5,3,0,0,285,286,5,60,0,0,286,293,5,74,0,0,287,288,5,3,0,
        0,288,289,5,60,0,0,289,290,7,2,0,0,290,291,5,60,0,0,291,293,3,12,
        6,0,292,283,1,0,0,0,292,287,1,0,0,0,293,299,1,0,0,0,294,295,10,1,
        0,0,295,296,5,68,0,0,296,298,3,24,12,2,297,294,1,0,0,0,298,301,1,
        0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,25,1,0,0,0,301,299,1,0,
        0,0,302,303,7,3,0,0,303,27,1,0,0,0,304,310,3,42,21,0,305,306,3,52,
        26,0,306,307,3,28,14,0,307,309,1,0,0,0,308,305,1,0,0,0,309,312,1,
        0,0,0,310,308,1,0,0,0,310,311,1,0,0,0,311,388,1,0,0,0,312,310,1,
        0,0,0,313,319,3,50,25,0,314,315,3,52,26,0,315,316,3,28,14,0,316,
        318,1,0,0,0,317,314,1,0,0,0,318,321,1,0,0,0,319,317,1,0,0,0,319,
        320,1,0,0,0,320,388,1,0,0,0,321,319,1,0,0,0,322,328,3,36,18,0,323,
        324,3,52,26,0,324,325,3,28,14,0,325,327,1,0,0,0,326,323,1,0,0,0,
        327,330,1,0,0,0,328,326,1,0,0,0,328,329,1,0,0,0,329,388,1,0,0,0,
        330,328,1,0,0,0,331,337,3,38,19,0,332,333,3,52,26,0,333,334,3,28,
        14,0,334,336,1,0,0,0,335,332,1,0,0,0,336,339,1,0,0,0,337,335,1,0,
        0,0,337,338,1,0,0,0,338,388,1,0,0,0,339,337,1,0,0,0,340,341,3,40,
        20,0,341,347,3,28,14,0,342,343,3,52,26,0,343,344,3,28,14,0,344,346,
        1,0,0,0,345,342,1,0,0,0,346,349,1,0,0,0,347,345,1,0,0,0,347,348,
        1,0,0,0,348,388,1,0,0,0,349,347,1,0,0,0,350,356,3,16,8,0,351,352,
        3,52,26,0,352,353,3,28,14,0,353,355,1,0,0,0,354,351,1,0,0,0,355,
        358,1,0,0,0,356,354,1,0,0,0,356,357,1,0,0,0,357,388,1,0,0,0,358,
        356,1,0,0,0,359,360,5,47,0,0,360,366,3,28,14,0,361,362,3,52,26,0,
        362,363,3,28,14,0,363,365,1,0,0,0,364,361,1,0,0,0,365,368,1,0,0,
        0,366,364,1,0,0,0,366,367,1,0,0,0,367,388,1,0,0,0,368,366,1,0,0,
        0,369,375,3,34,17,0,370,371,3,52,26,0,371,372,3,28,14,0,372,374,
        1,0,0,0,373,370,1,0,0,0,374,377,1,0,0,0,375,373,1,0,0,0,375,376,
        1,0,0,0,376,388,1,0,0,0,377,375,1,0,0,0,378,384,3,70,35,0,379,380,
        3,52,26,0,380,381,3,28,14,0,381,383,1,0,0,0,382,379,1,0,0,0,383,
        386,1,0,0,0,384,382,1,0,0,0,384,385,1,0,0,0,385,388,1,0,0,0,386,
        384,1,0,0,0,387,304,1,0,0,0,387,313,1,0,0,0,387,322,1,0,0,0,387,
        331,1,0,0,0,387,340,1,0,0,0,387,350,1,0,0,0,387,359,1,0,0,0,387,
        369,1,0,0,0,387,378,1,0,0,0,388,29,1,0,0,0,389,393,5,74,0,0,390,
        393,3,22,11,0,391,393,3,24,12,0,392,389,1,0,0,0,392,390,1,0,0,0,
        392,391,1,0,0,0,393,31,1,0,0,0,394,395,3,30,15,0,395,396,5,60,0,
        0,396,397,5,74,0,0,397,401,5,62,0,0,398,400,3,18,9,0,399,398,1,0,
        0,0,400,403,1,0,0,0,401,399,1,0,0,0,401,402,1,0,0,0,402,404,1,0,
        0,0,403,401,1,0,0,0,404,405,5,63,0,0,405,33,1,0,0,0,406,407,3,16,
        8,0,407,408,3,26,13,0,408,409,3,16,8,0,409,35,1,0,0,0,410,411,3,
        16,8,0,411,412,5,43,0,0,412,413,3,16,8,0,413,37,1,0,0,0,414,417,
        5,74,0,0,415,417,3,22,11,0,416,414,1,0,0,0,416,415,1,0,0,0,417,418,
        1,0,0,0,418,419,5,44,0,0,419,420,3,24,12,0,420,39,1,0,0,0,421,426,
        5,41,0,0,422,427,5,74,0,0,423,427,3,22,11,0,424,427,3,20,10,0,425,
        427,3,10,5,0,426,422,1,0,0,0,426,423,1,0,0,0,426,424,1,0,0,0,426,
        425,1,0,0,0,427,41,1,0,0,0,428,434,5,74,0,0,429,430,5,74,0,0,430,
        431,5,62,0,0,431,432,5,74,0,0,432,434,5,63,0,0,433,428,1,0,0,0,433,
        429,1,0,0,0,434,435,1,0,0,0,435,436,5,49,0,0,436,447,3,28,14,0,437,
        443,5,74,0,0,438,439,5,74,0,0,439,440,5,62,0,0,440,441,5,74,0,0,
        441,443,5,63,0,0,442,437,1,0,0,0,442,438,1,0,0,0,443,444,1,0,0,0,
        444,445,5,49,0,0,445,447,3,80,40,0,446,433,1,0,0,0,446,442,1,0,0,
        0,447,43,1,0,0,0,448,453,3,16,8,0,449,450,5,58,0,0,450,452,3,16,
        8,0,451,449,1,0,0,0,452,455,1,0,0,0,453,451,1,0,0,0,453,454,1,0,
        0,0,454,45,1,0,0,0,455,453,1,0,0,0,456,457,6,23,-1,0,457,458,3,44,
        22,0,458,464,1,0,0,0,459,460,10,2,0,0,460,461,7,4,0,0,461,463,3,
        44,22,0,462,459,1,0,0,0,463,466,1,0,0,0,464,462,1,0,0,0,464,465,
        1,0,0,0,465,47,1,0,0,0,466,464,1,0,0,0,467,468,6,24,-1,0,468,469,
        3,46,23,0,469,475,1,0,0,0,470,471,10,2,0,0,471,472,7,5,0,0,472,474,
        3,46,23,0,473,470,1,0,0,0,474,477,1,0,0,0,475,473,1,0,0,0,475,476,
        1,0,0,0,476,49,1,0,0,0,477,475,1,0,0,0,478,479,3,48,24,0,479,51,
        1,0,0,0,480,481,7,6,0,0,481,53,1,0,0,0,482,483,3,10,5,0,483,484,
        5,62,0,0,484,485,3,18,9,0,485,486,5,63,0,0,486,55,1,0,0,0,487,488,
        5,13,0,0,488,489,5,74,0,0,489,490,5,14,0,0,490,491,3,22,11,0,491,
        492,5,44,0,0,492,493,3,24,12,0,493,500,1,0,0,0,494,495,5,15,0,0,
        495,496,5,62,0,0,496,497,3,20,10,0,497,498,5,63,0,0,498,500,1,0,
        0,0,499,487,1,0,0,0,499,494,1,0,0,0,500,57,1,0,0,0,501,502,5,16,
        0,0,502,503,5,62,0,0,503,504,3,28,14,0,504,505,5,63,0,0,505,59,1,
        0,0,0,506,507,5,17,0,0,507,508,5,74,0,0,508,509,5,62,0,0,509,510,
        3,28,14,0,510,511,5,63,0,0,511,61,1,0,0,0,512,520,5,18,0,0,513,521,
        5,74,0,0,514,521,3,22,11,0,515,521,5,40,0,0,516,517,5,62,0,0,517,
        518,3,18,9,0,518,519,5,63,0,0,519,521,1,0,0,0,520,513,1,0,0,0,520,
        514,1,0,0,0,520,515,1,0,0,0,520,516,1,0,0,0,521,522,1,0,0,0,522,
        523,5,19,0,0,523,553,3,12,6,0,524,532,5,18,0,0,525,533,5,74,0,0,
        526,533,3,22,11,0,527,533,5,40,0,0,528,529,5,62,0,0,529,530,3,18,
        9,0,530,531,5,63,0,0,531,533,1,0,0,0,532,525,1,0,0,0,532,526,1,0,
        0,0,532,527,1,0,0,0,532,528,1,0,0,0,533,534,1,0,0,0,534,535,5,20,
        0,0,535,536,5,74,0,0,536,537,5,62,0,0,537,538,3,18,9,0,538,547,5,
        63,0,0,539,540,5,61,0,0,540,541,5,74,0,0,541,542,5,62,0,0,542,543,
        3,18,9,0,543,544,5,63,0,0,544,546,1,0,0,0,545,539,1,0,0,0,546,549,
        1,0,0,0,547,545,1,0,0,0,547,548,1,0,0,0,548,553,1,0,0,0,549,547,
        1,0,0,0,550,551,5,18,0,0,551,553,3,42,21,0,552,512,1,0,0,0,552,524,
        1,0,0,0,552,550,1,0,0,0,553,63,1,0,0,0,554,555,5,13,0,0,555,557,
        5,74,0,0,556,554,1,0,0,0,557,560,1,0,0,0,558,556,1,0,0,0,558,559,
        1,0,0,0,559,561,1,0,0,0,560,558,1,0,0,0,561,565,5,18,0,0,562,566,
        5,74,0,0,563,566,3,22,11,0,564,566,5,40,0,0,565,562,1,0,0,0,565,
        563,1,0,0,0,565,564,1,0,0,0,566,567,1,0,0,0,567,568,5,21,0,0,568,
        571,5,62,0,0,569,572,3,18,9,0,570,572,3,24,12,0,571,569,1,0,0,0,
        571,570,1,0,0,0,572,573,1,0,0,0,573,574,5,63,0,0,574,618,1,0,0,0,
        575,576,5,13,0,0,576,578,5,74,0,0,577,575,1,0,0,0,578,581,1,0,0,
        0,579,577,1,0,0,0,579,580,1,0,0,0,580,582,1,0,0,0,581,579,1,0,0,
        0,582,586,5,22,0,0,583,587,5,74,0,0,584,587,3,22,11,0,585,587,5,
        40,0,0,586,583,1,0,0,0,586,584,1,0,0,0,586,585,1,0,0,0,587,588,1,
        0,0,0,588,589,5,21,0,0,589,592,5,62,0,0,590,593,3,18,9,0,591,593,
        3,24,12,0,592,590,1,0,0,0,592,591,1,0,0,0,593,594,1,0,0,0,594,595,
        5,63,0,0,595,618,1,0,0,0,596,597,5,13,0,0,597,599,5,74,0,0,598,596,
        1,0,0,0,599,602,1,0,0,0,600,598,1,0,0,0,600,601,1,0,0,0,601,603,
        1,0,0,0,602,600,1,0,0,0,603,607,5,23,0,0,604,608,5,74,0,0,605,608,
        3,22,11,0,606,608,5,40,0,0,607,604,1,0,0,0,607,605,1,0,0,0,607,606,
        1,0,0,0,608,609,1,0,0,0,609,610,5,21,0,0,610,613,5,62,0,0,611,614,
        3,18,9,0,612,614,3,24,12,0,613,611,1,0,0,0,613,612,1,0,0,0,614,615,
        1,0,0,0,615,616,5,63,0,0,616,618,1,0,0,0,617,558,1,0,0,0,617,579,
        1,0,0,0,617,600,1,0,0,0,618,65,1,0,0,0,619,623,5,22,0,0,620,624,
        5,74,0,0,621,624,3,22,11,0,622,624,5,40,0,0,623,620,1,0,0,0,623,
        621,1,0,0,0,623,622,1,0,0,0,624,625,1,0,0,0,625,626,5,19,0,0,626,
        650,3,12,6,0,627,631,5,22,0,0,628,632,5,74,0,0,629,632,3,22,11,0,
        630,632,5,40,0,0,631,628,1,0,0,0,631,629,1,0,0,0,631,630,1,0,0,0,
        632,633,1,0,0,0,633,634,5,20,0,0,634,635,5,74,0,0,635,636,5,62,0,
        0,636,637,3,18,9,0,637,646,5,63,0,0,638,639,5,61,0,0,639,640,5,74,
        0,0,640,641,5,62,0,0,641,642,3,18,9,0,642,643,5,63,0,0,643,645,1,
        0,0,0,644,638,1,0,0,0,645,648,1,0,0,0,646,644,1,0,0,0,646,647,1,
        0,0,0,647,650,1,0,0,0,648,646,1,0,0,0,649,619,1,0,0,0,649,627,1,
        0,0,0,650,67,1,0,0,0,651,655,5,23,0,0,652,656,5,74,0,0,653,656,3,
        22,11,0,654,656,5,40,0,0,655,652,1,0,0,0,655,653,1,0,0,0,655,654,
        1,0,0,0,656,657,1,0,0,0,657,658,5,19,0,0,658,682,3,12,6,0,659,663,
        5,23,0,0,660,664,5,74,0,0,661,664,3,22,11,0,662,664,5,40,0,0,663,
        660,1,0,0,0,663,661,1,0,0,0,663,662,1,0,0,0,664,665,1,0,0,0,665,
        666,5,20,0,0,666,667,5,74,0,0,667,668,5,62,0,0,668,669,3,18,9,0,
        669,678,5,63,0,0,670,671,5,61,0,0,671,672,5,74,0,0,672,673,5,62,
        0,0,673,674,3,18,9,0,674,675,5,63,0,0,675,677,1,0,0,0,676,670,1,
        0,0,0,677,680,1,0,0,0,678,676,1,0,0,0,678,679,1,0,0,0,679,682,1,
        0,0,0,680,678,1,0,0,0,681,651,1,0,0,0,681,659,1,0,0,0,682,69,1,0,
        0,0,683,687,5,26,0,0,684,688,5,74,0,0,685,688,3,22,11,0,686,688,
        5,40,0,0,687,684,1,0,0,0,687,685,1,0,0,0,687,686,1,0,0,0,688,689,
        1,0,0,0,689,690,5,27,0,0,690,691,3,24,12,0,691,71,1,0,0,0,692,693,
        5,28,0,0,693,694,5,74,0,0,694,695,3,70,35,0,695,73,1,0,0,0,696,697,
        5,31,0,0,697,698,3,28,14,0,698,699,5,59,0,0,699,700,3,6,3,0,700,
        701,5,32,0,0,701,702,5,59,0,0,702,703,3,6,3,0,703,710,1,0,0,0,704,
        705,5,31,0,0,705,706,3,28,14,0,706,707,5,59,0,0,707,708,3,6,3,0,
        708,710,1,0,0,0,709,696,1,0,0,0,709,704,1,0,0,0,710,75,1,0,0,0,711,
        712,5,33,0,0,712,713,5,74,0,0,713,714,5,43,0,0,714,715,3,20,10,0,
        715,716,5,59,0,0,716,717,3,6,3,0,717,718,5,25,0,0,718,77,1,0,0,0,
        719,720,5,34,0,0,720,721,3,28,14,0,721,722,5,59,0,0,722,723,3,6,
        3,0,723,724,5,25,0,0,724,79,1,0,0,0,725,726,5,35,0,0,726,730,5,62,
        0,0,727,729,5,72,0,0,728,727,1,0,0,0,729,732,1,0,0,0,730,728,1,0,
        0,0,730,731,1,0,0,0,731,733,1,0,0,0,732,730,1,0,0,0,733,734,5,63,
        0,0,734,81,1,0,0,0,735,736,5,36,0,0,736,737,5,62,0,0,737,738,3,18,
        9,0,738,739,5,63,0,0,739,83,1,0,0,0,740,741,5,37,0,0,741,742,3,28,
        14,0,742,85,1,0,0,0,743,744,5,6,0,0,744,745,5,62,0,0,745,746,5,69,
        0,0,746,747,5,63,0,0,747,87,1,0,0,0,748,749,5,8,0,0,749,750,5,62,
        0,0,750,751,3,12,6,0,751,752,5,61,0,0,752,753,3,12,6,0,753,754,5,
        63,0,0,754,89,1,0,0,0,71,95,102,116,137,147,158,171,179,187,197,
        207,215,223,231,239,242,254,256,265,267,276,278,281,292,299,310,
        319,328,337,347,356,366,375,384,387,392,401,416,426,433,442,446,
        453,464,475,499,520,532,547,552,558,565,571,579,586,592,600,607,
        613,617,623,631,646,649,655,663,678,681,687,709,730
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
                   "timer_statement", "dice_statement" ]

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
            self.state = 90
            self.match(BoardGameParser.GAME)
            self.state = 91
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 93 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                self.define_block()
                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 97
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
            self.state = 99
            self.match(BoardGameParser.DEFINE)
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 100
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 101
                self.object_access()
                pass


            self.state = 104
            self.match(BoardGameParser.COLON)
            self.state = 105
            self.code_block()
            self.state = 106
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
            self.state = 108
            self.match(BoardGameParser.START)
            self.state = 109
            self.match(BoardGameParser.COLON)
            self.state = 110
            self.code_block()
            self.state = 111
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
            self.state = 114 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 113
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 116 
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
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.game_entities_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.board_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.player_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.condition_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 122
                self.rule_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 123
                self.piece_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 124
                self.obstacle_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 125
                self.booster_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 126
                self.turn_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 127
                self.move_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 128
                self.timer_statement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 129
                self.dice_statement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 130
                self.expression()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 131
                self.if_statement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 132
                self.for_statement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 133
                self.while_statement()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 134
                self.input_statement()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 135
                self.print_statement()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 136
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
            self.state = 139
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
            self.state = 141
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
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [69, 70]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.int_literal()
                pass
            elif token in [71]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(BoardGameParser.FLOAT_LITERAL)
                pass
            elif token in [72]:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.match(BoardGameParser.STRING_LITERAL)
                pass
            elif token in [73]:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.object_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.list_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 152
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 153
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 154
                self.expression()
                self.state = 155
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 157
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

        def ALL(self):
            return self.getToken(BoardGameParser.ALL, 0)

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


        def ANY(self):
            return self.getToken(BoardGameParser.ANY, 0)

        def NONE(self):
            return self.getToken(BoardGameParser.NONE, 0)

        def ASSIGN_OPT(self):
            return self.getToken(BoardGameParser.ASSIGN_OPT, 0)

        def literal(self):
            return self.getTypedRuleContext(BoardGameParser.LiteralContext,0)


        def objects(self):
            return self.getTypedRuleContext(BoardGameParser.ObjectsContext,0)


        def object_access(self):
            return self.getTypedRuleContext(BoardGameParser.Object_accessContext,0)


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
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(BoardGameParser.SCORE)
                self.state = 161
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 162
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 163
                self.match(BoardGameParser.DOT)
                self.state = 164
                self.match(BoardGameParser.CONDITIONS)
                self.state = 165
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(BoardGameParser.ALL)
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 167
                        self.match(BoardGameParser.COMMA)
                        self.state = 168
                        self.param_list() 
                    self.state = 173
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.match(BoardGameParser.ANY)
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 175
                        self.match(BoardGameParser.COMMA)
                        self.state = 176
                        self.param_list() 
                    self.state = 181
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                self.match(BoardGameParser.NONE)
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 183
                        self.match(BoardGameParser.COMMA)
                        self.state = 184
                        self.param_list() 
                    self.state = 189
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 191
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 192
                self.literal()
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 193
                        self.match(BoardGameParser.COMMA)
                        self.state = 194
                        self.param_list() 
                    self.state = 199
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 200
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 201
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 202
                self.objects()
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 203
                        self.match(BoardGameParser.COMMA)
                        self.state = 204
                        self.param_list() 
                    self.state = 209
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 210
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 211
                        self.match(BoardGameParser.COMMA)
                        self.state = 212
                        self.param_list() 
                    self.state = 217
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 218
                self.literal()
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 219
                        self.match(BoardGameParser.COMMA)
                        self.state = 220
                        self.param_list() 
                    self.state = 225
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 226
                self.object_access()
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 227
                        self.match(BoardGameParser.COMMA)
                        self.state = 228
                        self.param_list() 
                    self.state = 233
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 234
                self.list_()
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 235
                        self.match(BoardGameParser.COMMA)
                        self.state = 236
                        self.param_list() 
                    self.state = 241
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
            self.state = 244
            self.match(BoardGameParser.OPEN_BRACKET)
            self.state = 245
            self.param_list()
            self.state = 246
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
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 249
                self.match(BoardGameParser.DOT)
                self.state = 250
                self.game_entities()
                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 254
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [60]:
                            self.state = 251
                            self.match(BoardGameParser.DOT)
                            self.state = 252
                            self.game_entities()
                            pass
                        elif token in [74]:
                            self.state = 253
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 258
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.game_entities()
                self.state = 260
                self.match(BoardGameParser.DOT)
                self.state = 261
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 265
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [60]:
                            self.state = 262
                            self.match(BoardGameParser.DOT)
                            self.state = 263
                            self.game_entities()
                            pass
                        elif token in [74]:
                            self.state = 264
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 269
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 271
                self.match(BoardGameParser.DOT)
                self.state = 272
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 276
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [60]:
                            self.state = 273
                            self.match(BoardGameParser.DOT)
                            self.state = 274
                            self.game_entities()
                            pass
                        elif token in [74]:
                            self.state = 275
                            self.match(BoardGameParser.IDENTIFIER)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 280
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
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 284
                self.match(BoardGameParser.BOARD)
                self.state = 285
                self.match(BoardGameParser.DOT)
                self.state = 286
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 287
                self.match(BoardGameParser.BOARD)
                self.state = 288
                self.match(BoardGameParser.DOT)
                self.state = 289
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 290
                self.match(BoardGameParser.DOT)

                self.state = 291
                self.int_literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.Board_posContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_board_pos)
                    self.state = 294
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 295
                    self.match(BoardGameParser.ELIPSIS)
                    self.state = 296
                    self.board_pos(2) 
                self.state = 301
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
            self.state = 302
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
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.assignment_expression()
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 305
                        self.logical_opt()
                        self.state = 306
                        self.expression() 
                    self.state = 312
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.math_expression()
                self.state = 319
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 314
                        self.logical_opt()
                        self.state = 315
                        self.expression() 
                    self.state = 321
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.in_expression()
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 323
                        self.logical_opt()
                        self.state = 324
                        self.expression() 
                    self.state = 330
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 331
                self.at_expression()
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 332
                        self.logical_opt()
                        self.state = 333
                        self.expression() 
                    self.state = 339
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 340
                self.any_expression()
                self.state = 341
                self.expression()
                self.state = 347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 342
                        self.logical_opt()
                        self.state = 343
                        self.expression() 
                    self.state = 349
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 350
                self.primary()
                self.state = 356
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 351
                        self.logical_opt()
                        self.state = 352
                        self.expression() 
                    self.state = 358
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 359
                self.match(BoardGameParser.NOT_OPT)
                self.state = 360
                self.expression()
                self.state = 366
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 361
                        self.logical_opt()
                        self.state = 362
                        self.expression() 
                    self.state = 368
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 369
                self.conditional_expression()
                self.state = 375
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 370
                        self.logical_opt()
                        self.state = 371
                        self.expression() 
                    self.state = 377
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 378
                self.move_statement()
                self.state = 384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 379
                        self.logical_opt()
                        self.state = 380
                        self.expression() 
                    self.state = 386
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
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.object_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 391
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
            self.state = 394
            self.objects()
            self.state = 395
            self.match(BoardGameParser.DOT)
            self.state = 396
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 397
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581418680) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 2017) != 0):
                self.state = 398
                self.param_list()
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 404
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
            self.state = 406
            self.primary()
            self.state = 407
            self.conditional_opt()
            self.state = 408
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
            self.state = 410
            self.primary()
            self.state = 411
            self.match(BoardGameParser.IN)
            self.state = 412
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
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 414
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 415
                self.object_access()
                pass


            self.state = 418
            self.match(BoardGameParser.AT)
            self.state = 419
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
            self.state = 421
            self.match(BoardGameParser.ANY)
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 422
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 423
                self.object_access()
                pass

            elif la_ == 3:
                self.state = 424
                self.list_()
                pass

            elif la_ == 4:
                self.state = 425
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
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 428
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 429
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 430
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 431
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 432
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 435
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 436
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 437
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 438
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 439
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 440
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 441
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 444
                self.match(BoardGameParser.ASSIGN_OPT)
                self.state = 445
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
            self.state = 448
            self.primary()
            self.state = 453
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 449
                    self.match(BoardGameParser.EXP_OPT)
                    self.state = 450
                    self.primary() 
                self.state = 455
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
            self.state = 457
            self.exponent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 464
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.MultiplicativeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative)
                    self.state = 459
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 460
                    _la = self._input.LA(1)
                    if not(_la==56 or _la==57):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 461
                    self.exponent() 
                self.state = 466
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
            self.state = 468
            self.multiplicative(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 475
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BoardGameParser.AdditiveContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                    self.state = 470
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 471
                    _la = self._input.LA(1)
                    if not(_la==54 or _la==55):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 472
                    self.multiplicative(0) 
                self.state = 477
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
            self.state = 478
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
            self.state = 480
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
            self.state = 482
            self.game_entities()
            self.state = 483
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 484
            self.param_list()
            self.state = 485
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
            self.state = 499
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self.match(BoardGameParser.PLAYER)
                self.state = 488
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 489
                self.match(BoardGameParser.COLOR)
                self.state = 490
                self.object_access()
                self.state = 491
                self.match(BoardGameParser.AT)
                self.state = 492
                self.board_pos(0)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.match(BoardGameParser.ORDER)
                self.state = 495
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 496
                self.list_()
                self.state = 497
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
            self.state = 501
            self.match(BoardGameParser.CONDITION)
            self.state = 502
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 503
            self.expression()
            self.state = 504
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
            self.state = 506
            self.match(BoardGameParser.RULE)
            self.state = 507
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 508
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 509
            self.expression()
            self.state = 510
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
            self.state = 552
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.match(BoardGameParser.PIECE)
                self.state = 520
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 513
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 514
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 515
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 4:
                    self.state = 516
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 517
                    self.param_list()
                    self.state = 518
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 522
                self.match(BoardGameParser.COUNT)
                self.state = 523
                self.int_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
                self.match(BoardGameParser.PIECE)
                self.state = 532
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 525
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 526
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 527
                    self.match(BoardGameParser.ALL)
                    pass

                elif la_ == 4:
                    self.state = 528
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 529
                    self.param_list()
                    self.state = 530
                    self.match(BoardGameParser.CLOSE_PAR)
                    pass


                self.state = 534
                self.match(BoardGameParser.ACTION)
                self.state = 535
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 536
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 537
                self.param_list()
                self.state = 538
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 547
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 539
                    self.match(BoardGameParser.COMMA)
                    self.state = 540
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 541
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 542
                    self.param_list()
                    self.state = 543
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 549
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 550
                self.match(BoardGameParser.PIECE)
                self.state = 551
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
            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 554
                    self.match(BoardGameParser.PLAYER)
                    self.state = 555
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 560
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 561
                self.match(BoardGameParser.PIECE)
                self.state = 565
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 562
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 563
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 564
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 567
                self.match(BoardGameParser.SETUP)
                self.state = 568
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 571
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 569
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 570
                    self.board_pos(0)
                    pass


                self.state = 573
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 579
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 575
                    self.match(BoardGameParser.PLAYER)
                    self.state = 576
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 581
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 582
                self.match(BoardGameParser.OBSTACLE)
                self.state = 586
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                if la_ == 1:
                    self.state = 583
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 584
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 585
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 588
                self.match(BoardGameParser.SETUP)
                self.state = 589
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 592
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 590
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 591
                    self.board_pos(0)
                    pass


                self.state = 594
                self.match(BoardGameParser.CLOSE_PAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 600
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 596
                    self.match(BoardGameParser.PLAYER)
                    self.state = 597
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 602
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 603
                self.match(BoardGameParser.BOOSTER)
                self.state = 607
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 604
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 605
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 606
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 609
                self.match(BoardGameParser.SETUP)
                self.state = 610
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 613
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                if la_ == 1:
                    self.state = 611
                    self.param_list()
                    pass

                elif la_ == 2:
                    self.state = 612
                    self.board_pos(0)
                    pass


                self.state = 615
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
            self.state = 649
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                self.match(BoardGameParser.OBSTACLE)
                self.state = 623
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 620
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 621
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 622
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 625
                self.match(BoardGameParser.COUNT)
                self.state = 626
                self.int_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 627
                self.match(BoardGameParser.OBSTACLE)
                self.state = 631
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                if la_ == 1:
                    self.state = 628
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 629
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 630
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 633
                self.match(BoardGameParser.ACTION)
                self.state = 634
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 635
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 636
                self.param_list()
                self.state = 637
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 646
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 638
                    self.match(BoardGameParser.COMMA)
                    self.state = 639
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 640
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 641
                    self.param_list()
                    self.state = 642
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 648
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
            self.state = 681
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 651
                self.match(BoardGameParser.BOOSTER)
                self.state = 655
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 652
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 653
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 654
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 657
                self.match(BoardGameParser.COUNT)
                self.state = 658
                self.int_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 659
                self.match(BoardGameParser.BOOSTER)
                self.state = 663
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                if la_ == 1:
                    self.state = 660
                    self.match(BoardGameParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 661
                    self.object_access()
                    pass

                elif la_ == 3:
                    self.state = 662
                    self.match(BoardGameParser.ALL)
                    pass


                self.state = 665
                self.match(BoardGameParser.ACTION)
                self.state = 666
                self.match(BoardGameParser.IDENTIFIER)
                self.state = 667
                self.match(BoardGameParser.OPEN_PAR)
                self.state = 668
                self.param_list()
                self.state = 669
                self.match(BoardGameParser.CLOSE_PAR)
                self.state = 678
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 670
                    self.match(BoardGameParser.COMMA)
                    self.state = 671
                    self.match(BoardGameParser.IDENTIFIER)
                    self.state = 672
                    self.match(BoardGameParser.OPEN_PAR)
                    self.state = 673
                    self.param_list()
                    self.state = 674
                    self.match(BoardGameParser.CLOSE_PAR)
                    self.state = 680
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
            self.state = 683
            self.match(BoardGameParser.MOVE)
            self.state = 687
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.state = 684
                self.match(BoardGameParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 685
                self.object_access()
                pass

            elif la_ == 3:
                self.state = 686
                self.match(BoardGameParser.ALL)
                pass


            self.state = 689
            self.match(BoardGameParser.TO)
            self.state = 690
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
            self.state = 692
            self.match(BoardGameParser.TURN)
            self.state = 693
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 694
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
            self.state = 709
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 696
                self.match(BoardGameParser.IF)
                self.state = 697
                self.expression()
                self.state = 698
                self.match(BoardGameParser.COLON)
                self.state = 699
                self.code_block()
                self.state = 700
                self.match(BoardGameParser.ELSE)
                self.state = 701
                self.match(BoardGameParser.COLON)
                self.state = 702
                self.code_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 704
                self.match(BoardGameParser.IF)
                self.state = 705
                self.expression()
                self.state = 706
                self.match(BoardGameParser.COLON)
                self.state = 707
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
            self.state = 711
            self.match(BoardGameParser.FOR)
            self.state = 712
            self.match(BoardGameParser.IDENTIFIER)
            self.state = 713
            self.match(BoardGameParser.IN)
            self.state = 714
            self.list_()
            self.state = 715
            self.match(BoardGameParser.COLON)
            self.state = 716
            self.code_block()
            self.state = 717
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
            self.state = 719
            self.match(BoardGameParser.WHILE)
            self.state = 720
            self.expression()
            self.state = 721
            self.match(BoardGameParser.COLON)
            self.state = 722
            self.code_block()
            self.state = 723
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
            self.state = 725
            self.match(BoardGameParser.INPUT)
            self.state = 726
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 730
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==72:
                self.state = 727
                self.match(BoardGameParser.STRING_LITERAL)
                self.state = 732
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 733
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
            self.state = 735
            self.match(BoardGameParser.PRINT)
            self.state = 736
            self.match(BoardGameParser.OPEN_PAR)

            self.state = 737
            self.param_list()
            self.state = 738
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
            self.state = 740
            self.match(BoardGameParser.RETURN)
            self.state = 741
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
            self.state = 743
            self.match(BoardGameParser.TIMER)
            self.state = 744
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 745
            self.match(BoardGameParser.POSITIVE_INT_LITERAL)
            self.state = 746
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
            self.state = 748
            self.match(BoardGameParser.DICE)
            self.state = 749
            self.match(BoardGameParser.OPEN_PAR)
            self.state = 750
            self.int_literal()
            self.state = 751
            self.match(BoardGameParser.COMMA)
            self.state = 752
            self.int_literal()
            self.state = 753
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
         




