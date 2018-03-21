import itertools
#1.暴力解法
# def digitCounts(k,n):
#     # k_list=0
#     # for i in range(0,n+1):
#     #     i=str(i)
#     #     for q in range(len(i)):
#     #         if str(k)==i[q]:
#     #             k_list+=1
#     # return k_list
#2.简单解法
def digitCounts(k,n):
    n1=[str(i)for i in range(n+1)]
    n_str=''.join(n1)
    return n_str.count(str(k))



#测试
assert  digitCounts(1,11)==4,'Calculation error,True:4 , yours:%s' % digitCounts(1,11)
assert  digitCounts(0,19)==2,'Calculation error,True:2 , yours:%s' % digitCounts(0,19)
assert  digitCounts(1,1)==1,'Calculation error,True:1 , yours:%s' % digitCounts(1,1)
assert  digitCounts(0,305)==57,'Calculation error,True:57 , yours:%s' % digitCounts(0,305)
assert  digitCounts(2,1)==0,'Calculation error,True:0 , yours:%s' % digitCounts(0,305)