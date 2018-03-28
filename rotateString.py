# -*- coding: utf-8 -*-
def rotateString(str, offset):
    return (str[-offset:]+str[:-offset])

assert rotateString("abcdefg",3)=='efgabcd','Calculation error,True:"efgabcd" , yours:%s'%rotateString("abcdefg",3)
assert rotateString("abcdefg",0)=="abcdefg",'Calculation error,True:"abcdefg" , yours:%s'%rotateString("abcdefg",0)
assert rotateString("abcdefg",1)=="gabcdef",'Calculation error,True:"gabcdef" , yours:%s'%rotateString("abcdefg",1)
assert rotateString("abcdefg",2)=="fgabcde",'Calculation error,True:"fgabcde" , yours:%s'%rotateString("abcdefg",2)
