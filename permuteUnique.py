import itertools
def permuteUnique(nums):
        # write your code here
        a = []
        if len(nums) == 0:
                return [a]
        for i in itertools.permutations(nums):
                if list(i) not in a:
                        a.append(list(i))
        return a


assert permuteUnique([1,2,2])==[[1,2,2],[2,1,2],[2,2,1]],'Calculation error,True:2 , yours:%s' % permuteUnique([1,2,2])
assert permuteUnique([2,2,2])==[[2,2,2]],'Calculation error,True:2 , yours:%s' % permuteUnique([2,2,2])
assert permuteUnique([1,2,2,2])==[[1,2,2,2],[2,1,2,2],[2,2,1,2], [2, 2, 2, 1]],'Calculation error,True:2 , yours:%s' % permuteUnique([1,2,2,2])
assert permuteUnique([])==[[]],'Calculation error,True:2 , yours:%s' % permuteUnique([])
