
关于lintcode一些题的解法
#### 1.python -爬楼梯（climbStairs.py）

题目：假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？

样例n=3，1+1+1=1+2=2+1=3，共有3中不同的方法

* 解法：
```
#当台阶数有这样的情况：
Stairs=    [0,1,2,3,4,5,6]
#爬台阶的方法就有：
climStairs=[1,1,2,3,5,8,13]
#比较两个数组：climStairs[i]=climStairs[i-1]+climStairs[i-2]
```
#### 2.python -计算最大值(calcMaxValue.py)
题目：给一个字符串类型的数字, 写一个方法去找到最大值, 你可以在任意两个数字间加 + 或 *

样例:
```
给出 str = 01231, 返回 10 ((((0 + 1) + 2) * 3) + 1) = 10 我们得到了最大值 10
给出 str = 891, 返回 73 因为 8 * 9 * 1 = 72 和 8 * 9 + 1 = 73, 所以73是最大值
```
* 解法：

只要当前的数字和即将计算的数字比1大，就是用乘法，每一个已计算的数字都是当前数字
当前的数字和即将计算的数字比1小（包括1 和 0），就是用加法

#### 3.python -尾部的零

题目：设计一个算法，计算出n阶乘中尾部零的个数

样例
`11! = 39916800，因此应该返回 2`

* 解法：

数的阶乘中只要出现关于5和5的倍数比如说：10/15/15/35的数字都会一次出现1个0~5个零，所以就使用递归的方法，让余数除以5取整指导当前的被除数为0，将每一次的余数相加得到最后的值

#### 4.python -
题目：给定一个数字列表，返回其所有可能的排列。

 注意事项
你可以假设没有重复数字。

样例
给出一个列表[1,2,3]，其全排列为：

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

* 解法：
  使用python自带函数：itertools.combinations

#### 5.python -统计数字
题目：计算数字k在0到n中的出现的次数，k可能是0~9的一个值

样例
例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1, 10, 11, 12)

* 解法：
  第一种暴力解法：
  1.首先取数
  2.将数字转化为string，然后使用切片对比
  第二种简单解法：
  1.取数，将其整合成字符串
  2.使用cout方法

##### 6. python 丑数②

题目:设计一个算法，找出只含素因子`2`，`3`，`5` 的第 *n* 小的数。

符合条件的数如：`1, 2, 3, 4, 5, 6, 8, 9, 10, 12...`

##### ** 注意事项

我们可以认为`1`也是一个丑数

样例

如果`n = 9`， 返回 `10`

* 解法

  1.成为丑数标准：只包含因子2,3,5的正整数被称作丑数，比如4,10,12都是丑数，而7,23,111则不是丑数。也就是丑数总能=2*x+3*y+5z得来

  2.借鉴网络的丑数推倒:](https://blog.csdn.net/caicai617/article/details/51345540),当前丑数（丑数2）一定等于之前的一个丑数 （丑数1）`*2/*3/*5`得来，所以就要前一个丑数`*2/*3/*5`,取一个最小值，这时丑数3也一定等于丑数1或者是丑数3）`*2/*3/*5`得来

  3.丑数2因为已经在丑数1的基础上乘了一个数，占了一个位置，丑数1再乘的时候就不需要重复在乘一遍已经乘过的数。

  ​	例如：丑数1=1，丑数2=`min(1*2,1*3,1*5)`=2,这个时候2已经被乘过了

  ​	丑数3=`min(丑数1*3，丑数1*5,丑数2*2)`

  ​	以此类推

  ​		

  ​