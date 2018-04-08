# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)
# def fizzBuzz( n):
#     fizz=[]
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             logging.info('15# i=%d' % i)
#             fizz.append('fizz')
#             fizz.append('buzz')
#
#         elif i%3==0:
#             logging.info('3 # i=%d'%i)
#             fizz.append('fizz')
#         elif i%5==0:
#             logging.info('3 # i=%d' % i)
#             fizz.append('buzz')
#         else:
#             logging.info('# # i=%d' % i)
#             fizz.append(str(i))
#
#     return fizz
# print(fizzBuzz(15))
for x in range(1,101):
    print('fizz'[x%3*4:]+'bizz'[x%5*4:]or x)


