# -*- coding: utf-8 -*-
def traillingZeros(s):
    x=s//5  #取
    x+=traillingZeros(x) if x else 0
    return x
#测试
assert traillingZeros(11)==2,'Calculation error,True:2 , yours:%s'%traillingZeros(11)
assert traillingZeros(105)==25,'Calculation error,True:25 , yours:%s'%traillingZeros(105)
assert traillingZeros(121212345624)==30303086396,'Calculation error,True:2 , yours:%s'%traillingZeros(121212345624)
assert traillingZeros(3)==0,'Calculation error,True:0 , yours:%s'%traillingZeros(3)