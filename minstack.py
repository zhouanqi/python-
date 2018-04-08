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
    #

a=MinStack()
print(a.push(1),'/n',a.pop(),'/n',a.push(2),'/n',a.push(3),'/n',a.min(),'/n',a.push(1),'pop',a.pop(),a.pop(),a.pop(),'/n',a.min())
# a.push(1)
# print(a.pop())
# a.push(2)
# a.push(3)
# a.min()
# a.push(1)
# print(a.min())

# def catch_exception(origin_func):
#     def wrapper(self, *args, **kwargs):
#         try:
#             u = origin_func(self, *args, **kwargs)
#             return u
#         except Exception:
#             print('here3')
#
#             self.revive() #不用顾虑，直接调用原来的类的方法
#             return 'an Exception raised.'
#     return wrapper
#
#
# class Test(object):
#     def __init__(self):
#         pass
#
#     def revive(self):
#         print('revive from exception.')
#         # do something to restore
#
#     @catch_exception
#     def read_value(self):
#         print('here I will do something.')
#         # do something.
#
# a=Test()
# a.revive()
# a.read_value()