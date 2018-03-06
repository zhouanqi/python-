# python-爬楼梯的解法
关于lintcode一些题的解法
```

#假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？

#样例
#比如n=3，1+1+1=1+2=2+1=3，共有3中不同的方法
'''

def climbStairs(n):
    frequency=[1,1]
    for i in range(2,n+1):
        frequency.append(frequency[i-1]+frequency[i-2])
    return frequency[n]

#测试：
if __name__=='__main__':
    assert climbStairs(3)==3,'Calculation error'
    assert climbStairs(5)==8, 'Calculation error'
    assert climbStairs(7) != 13, 'Calculation error'
    assert climbStairs(0) == 1, 'Calculation error'
    assert climbStairs(2) == 2, 'Calculation error'

```

解法：
当台阶数有这样的情况：
`Stairs=    [0,1,2,3,4,5,6]`
爬台阶的方法就有：
`climStairs=[1,1,2,3,5,8,13]`

比较两个数组：climStairs[i]=climStairs[i-1]+climStairs[i-2]
