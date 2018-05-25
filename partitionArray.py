class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        nums.sort()
        if len(nums)==0:
            return 0
        elif  k >nums[-1]:
            return len(nums)
        elif k<nums[0]:
            return 0
        
        else:
            return nums.index(k)
            
