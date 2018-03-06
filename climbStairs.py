def climbStairs(n):
    frequency=[1,1]
    '''计数从0开始'''
    for i in range(2,n+1):
        frequency.append(frequency[i-1]+frequency[i-2])
    return frequency[n]

'''测试：'''
if __name__=='__main__':
    assert climbStairs(3)==3,'Calculation error'
    assert climbStairs(5)==8, 'Calculation error'
    assert climbStairs(7) != 13, 'Calculation error'
    assert climbStairs(0) == 1, 'Calculation error'
    assert climbStairs(2) == 2, 'Calculation error'