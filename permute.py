# -*- coding: utf-8 -*-
import itertools
def permute(nums):
    re_list=[]
    for one in itertools.combinations('4644',4):
        re_list.append(one)
    return re_list
