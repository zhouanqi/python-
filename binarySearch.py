class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if nums==None and target==None:
            return -1
        begin=0
        end=len(nums)
        find=0
        if nums[begin]==target:return begin
        if nums[end-1]==target:return end
        
        while begin<end:
            mid=begin+(end-begin)//2
            if target==nums[mid]:
                find= mid
                break
            elif target>nums[mid]:
                begin+=1
            else: 
                end-=1
        if nums[mid]!=target:
            return -1
        while nums[mid]==nums[find-1]:  
            find-=1
        return find