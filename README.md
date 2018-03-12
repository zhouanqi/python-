
关于lintcode一些题的解法
####1.python-爬楼梯（climbStairs.py）
题目：假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？

样例n=3，1+1+1=1+2=2+1=3，共有3中不同的方法

*解法：*
当台阶数有这样的情况：
`Stairs=    [0,1,2,3,4,5,6]`
爬台阶的方法就有：
`climStairs=[1,1,2,3,5,8,13]`
比较两个数组：climStairs[i]=climStairs[i-1]+climStairs[i-2]

####2.python -计算最大值(calcMaxValue.py)
题目：给一个字符串类型的数字, 写一个方法去找到最大值, 你可以在任意两个数字间加 + 或 *

样例
给出 str = 01231, 返回 10 ((((0 + 1) + 2) * 3) + 1) = 10 我们得到了最大值 10
给出 str = 891, 返回 73 因为 8 * 9 * 1 = 72 和 8 * 9 + 1 = 73, 所以73是最大值

*解法：*
只要当前的数字和即将计算的数字比1大，就是用乘法，每一个已计算的数字都是当前数字
当前的数字和即将计算的数字比1小（包括1 和 0），就是用加法