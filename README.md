
关于lintcode一些题的解法
#### 1.python -爬楼梯 (climbStairs.py)

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
#### 2.python -计算最大值 (calcMaxValue.py)
题目：给一个字符串类型的数字, 写一个方法去找到最大值, 你可以在任意两个数字间加 + 或 *

样例:
```
给出 str = 01231, 返回 10 ((((0 + 1) + 2) * 3) + 1) = 10 我们得到了最大值 10
给出 str = 891, 返回 73 因为 8 * 9 * 1 = 72 和 8 * 9 + 1 = 73, 所以73是最大值
```
* 解法：

只要当前的数字和即将计算的数字比1大，就是用乘法，每一个已计算的数字都是当前数字
当前的数字和即将计算的数字比1小（包括1 和 0），就是用加法

#### 3.python -尾部的零 (trailingZeros.py)

题目：设计一个算法，计算出n阶乘中尾部零的个数

样例
`11! = 39916800，因此应该返回 2`

* 解法：

数的阶乘中只要出现关于5和5的倍数比如说：5/10/15/15/35的数字都会依次出现1~5个零，所以就使用递归的方法，让余数除以5取整直到当前的被除数为0，将每一次的余数相加得到最后的值

#### 4.python -统计数字 (digitCounts.py)

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

#### 5. python -丑数② (nthUglyNumber.py)

题目:设计一个算法，找出只含素因子`2`，`3`，`5` 的第 *n* 小的数。

符合条件的数如：`1, 2, 3, 4, 5, 6, 8, 9, 10, 12...`

** 注意事项

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
#### 6.python -二叉树的序列化和反序列化 (TreeNode.py)
题目：设计一个算法，并编写代码来序列化和反序列化二叉树。将树写入一个文件被称为“序列化”，读取文件后重建同样的二叉树被称为“反序列化”。

如何反序列化或序列化二叉树是没有限制的，你只需要确保可以将二叉树序列化为一个字符串，并且可以将字符串反序列化为原来的树结构。

样例

给出一个测试数据样例， 二叉树{3,9,20,#,#,15,7}，表示如下的树结构：

  3
 / \
9  20
  /  \
 15   7

* 解法
  对于一个二叉树它的序列化就是不断它的节点放在数组中，然后遇到None就赋值为#
  反序列化就是拿出字符串中的一个值，将其变成一个树的节点，但是要记录这个字符串当时的位置
  因为这个题的树遍历顺序是不会改变的，所以可以使用此方式
#### 7.python -旋转字符串 (rotateString.py)
题目：给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)


样例

对于字符串 "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"

* 解法

使用切片

####  8.python -Fizz Buzz问题 (fizzBuzz.py)

题目：给你一个整数*n*。从*1*到*Ñ*按照下面的规则打印每个数：

- 如果这个数被3整除，打印`fizz`。
- 如果这个数被5整除，打印`buzz`。
- 如果数这个能同时被`3`状语从句：`5`整除，打印`fizz buzz`。

样例

比如*n* = `15`，返回一个字符串数组：

```python
[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz", "11", "fizz",
  "13", "14", "fizz buzz"
]
```

* 解法

fizz字符创串的长度为4，bizz字符串的长度为4，

`print('fizz'[x%3*4:]+'bizz'[x%5*4:]or x)`,首先判断or前的两个字符串是否未空，不为空 打印对应的字符串，为空则打印x

使用`[x%z*4:]`的方式,若想打印这两个字符串，必须要[0*4]才行

#### 9.python -二叉查找树中搜索区间 (searchRange.py)

题目：

给定两个值 k1 和 k2（k1 < k2）和一个二叉查找树的根节点。找到树中所有值在 k1 到 k2 范围内的节点。即打印所有x (k1 <= x <= k2) 其中 x 是二叉查找树的中的节点值。返回所有升序的节点值。

样例

如果有 k1 = `10` 和 k2 = `22`, 你的程序应该返回 `[12, 20, 22]`.

```python
    20
   /  \
  8   22
 / \
4   12
```

* 解法

遍历二叉树，判断值

#### 10.python -带最小值操作的栈 (MinStack.py)

题目：实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。

你实现的栈将支持**push**，**pop** 和 **min** 操作，所有操作要求都在O(1)时间内完成。

##### ** 注意事项

如果堆栈中没有数字则不能进行min方法的调用

样例

如下操作：`push(1)，pop()，push(2)，push(3)，min()， push(1)，min() 返回 **1，2，1**`

* 解法

使用一个列表假代栈，push操作使用列表的插入函数：`list.insert(index, obj)`，参数`index`代表插入的位置，参数`obj`代表需要插入的参数。
pop操作使用列表的删除函数：`del list[index]`参数`index`代表需要删除的位置，删除之前记录列表的第一个元素然后返回。
min操作使用列表的最小值函数：`min(list)`参数`list`代表列表。使用装饰器来判断栈的大小，如果栈长度＞0，则继续操作，如果小于0，则返回False，其中`@wraps`作用为：把原函数的元信息拷贝到装饰器函数中，使得装饰器函数和原函数有一样的元信息，如此可以使得栈长度＞0时，正确返回应该执行的函数。

#### 11. python -字符串查找 (strStr.py)

题目：对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 `-1`。

样例

如果 source = `"source"` 和 target = `"target"`，返回 `-1`。如果 source = `"abcdabcdefg"` 和 target = `"bcd"`，返回 `1`。

* 解法

使用find函数，同时判断source和target的空值情况

#### 12.python -二分查找 (binarySearch.py)

题目：给定一个排序的整数数组（升序）和一个要查找的整数`target`，用`O(logn)`的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回`-1`。

样例

在数组 `[1, 2, 3, 3, 4, 5, 10]` 中二分查找`3`，返回`2`。

* 解法

将数组分成两边查找，如果中间的值>左边的值，那么左边的数组就要右移一位，如果中间的值<左边的值，那么右边的数组就要左移一位。如果判断到左边的数组和右边的数组重合，则停止判断，这个时候还没有找到相等的值就输出-1，同时为了兼顾重复数字，判断中间的值，是否和左边的值相等，如果想等就把左边的数组再减小一个。

为了提高速度，先判断空值和极限值相同的情况。

#### 13.python -全排列 (permute.py)

题目：给定一个数字列表，返回其所有可能的排列。

##### ** 注意事项

你可以假设没有重复数字。

样例

给出一个列表[1,2,3]，其全排列为：[

  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

* 解法

使用函数：`itertools.permutations`它是返回可迭代对象的所有数学全排列方式。

#### 14.python -带重复元素的排列 (permuteUnique.py)

题目：给出一个具有重复数字的列表，找出列表所有不同的排列。

样例

给出列表 `[1,2,2]`，不同的排列有：`[  [1,2,2],  [2,1,2],  [2,2,1]]`

* 解法：

使用`itertools.permutations`函数返回全排列方式，然后去重。

#### 15.python -子集 (subsets.py) 

题目：给定一个含不同整数的集合，返回其所有的子集

##### ** 注意事项

子集中的元素排列必须是非降序的，解集必须不包含重复的子集

样例

如果 S = [1,2,3]，有如下的解：[

  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

* 解法

一个比较笨的方法，就是循环每一个值，将其加入到新的列表中。

#### 16.python -平面列表 (flatten.py)

给定一个列表，该列表中的每个要素要么是个列表，要么是整数。将其变成一个只包含整数的简单列表。

##### ** 注意事项

如果给定的列表中的要素本身也是一个列表，那么它也可以包含列表。

您在真实的面试中是否遇到过这个题？ Yes

**样例**

给定 `[1,2,[1,2]]`，返回 `[1,2,1,2]`。给定 `[4,[3,[2,[1]]]]`，返回 `[4,3,2,1]`。

* 解法

​	1.判断给的列表为空值或者不可迭代

​	2.使用map将列表原素转化为字符串

​	3.使用正则匹配负号和数字












  ​