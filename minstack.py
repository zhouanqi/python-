# # -*- coding: utf-8 -*-
from functools import wraps
def min0(origin_func):
    @wraps(origin_func)#把原函数的元信息拷贝到装饰器函数中，使得装饰器函数和原函数有一样的元信息
    def wrapper(self,*args,**kwargs):
        if len(self.zhan):
            return origin_func(self,*args,**kwargs)
        else:
            return False
    return wrapper
class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.zhan=[]

    """
    @param: number: An integer
    @return: nothing
    """


    def push(self, number):
        # write your code here
        self.zhan.insert(0,number)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        no0 = self.zhan[0]
        del self.zhan[0]
        return no0

    """
    @return: An integer
    """

    @min0
    def min(self):
        # write your code here

        print('min:self.zhan', self.zhan)
        return min(self.zhan)


