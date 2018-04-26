 # -*- coding: utf-8 -*-
import re
from collections import Iterable

from datetime import datetime
def flatten(nestedList):
    #a=datetime.now()
    if nestedList != None and isinstance(nestedList, Iterable):
        # print(nestedList)
        # print(isinstance(nestedList, Iterable))
        str1 = ''.join(map(change, nestedList))
        str2 = re.compile(r'-?\d+')
        str3 = str2.findall(str1)
        return list(map(int, str3))
    else:
        a=[]
        a.append(nestedList)
        return a

def change( nestedList):
    return str(nestedList) + ','
a=[
    [[1,1],2,[1,1]],
    [1,2,[1,2]],
    [4,[3,[2,[1]]]],
    [],
    10,
    [-68,[[-97,-66],85,81,[[-63],[-71]],[-97,[166]]],[[35,136],[[125],[104]],[134,71],[154,[29]],32],[[[-2],31],164,139,[-52,[15]],[-53,25]],[-71,[[66],[139]],155,[[102],[-44]],[156,17]],[[29,-30],75,[-92,14],[1,159],76],[[133,[43]],[[-88],128],139,2,[182,[-45]]],52,[[[197],[151]],[[58],131],[[-21],[144]],[[-97],108],[147,[147]]],[[[180],[-1]],[129,[67]],[-20,-42],179,-83]]
   ]
b=[
    [1,1,2,1,1],
    [1,2,1,2],
    [4,3,2,1],
    [],
    [10],
    [-68,-97,-66,85,81,-63,-71,-97,166,35,136,125,104,134,71,154,29,32,-2,31,164,139,-52,15,-53,25,-71,66,139,155,102,-44,156,17,29,-30,75,-92,14,1,159,76,133,43,-88,128,139,2,182,-45,52,197,151,58,131,-21,144,-97,108,147,147,180,-1,129,67,-20,-42,179,-83]
    ]
for i in range(len(a)):
    assert flatten(a[i])==b[i],'Calculation error,True:%s , yours:%s'% (b[i],flatten(a[i]))
