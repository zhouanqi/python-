# # -*- coding: utf-8 -*-
#给一个字符串类型的数字, 写一个方法去找到最大值, 你可以在任意两个数字间加 + 或 *
class Solution:
    """
    @param str: the given string
    @return: the maximum value
    """
    # def __init__(self,str):
    #     self.str=str
    def calcMaxValue(self,str1):
        # write your code here
        if isinstance(str1, str):
            if len(str1) == 0 :
                return 0
            list1 = list(str1)
            m=int(list1[0])
            for i in list1[1:]:
                i = int(i)
                if i <= 1 or m <= 1:
                    m = m + i
                else:
                    m = m * i
            return m
        else:
            return False
#test:
truenum={'01231':10,'891':73,'0':0,'5201':11,'':0}
b=Solution()
#正确数据：
for i in truenum.keys() :
    assert b.calcMaxValue(i) == truenum[i],'计算错误：%s:%s'%(i,b.calcMaxValue(i))
#错误数据：
falsenum={'':1,'00':1,1:1}
for i in falsenum.keys() :
    assert b.calcMaxValue(i) != falsenum[i],'计算错误：%s:%s'%(i,b.calcMaxValue(i))