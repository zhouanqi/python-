# # -*- coding: utf-8 -*-
def nthUglyNumber(n):
    if not isinstance(n, int): return 0
    if n <= 0 : return 0
    ugly=[n]
    ugly[0] = 1
    step_two = 0
    step_three = 0
    step_five = 0
    for i in range(1,n ):
        two=ugly[step_two] * 2
        three=ugly[step_three] * 3
        five=ugly[step_five] * 5
        Min = min(two,three ,five )
        ugly.append(Min)

        if ugly[i] == ugly[step_two] * 2:
            step_two = step_two + 1
        if ugly[i] == ugly[step_three] * 3:
            step_three += 1
        if ugly[i] == ugly[step_five] * 5:
            step_five += 1
    return ugly[n-1]

assert nthUglyNumber(9)==10,'Calculation error,True:10 , yours:%s'%nthUglyNumber(9)
assert nthUglyNumber(105)==1875,'Calculation error,True:1875 , yours:%s'%nthUglyNumber(105)
assert nthUglyNumber(0)==0,'Calculation error,True:0 , yours:%s'%nthUglyNumber(0)
assert nthUglyNumber('*')==0,'Calculation error,True:0 , yours:%s'%nthUglyNumber('*')

