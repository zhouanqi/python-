def subsets( nums):
        """ 
        :type nums: List[int] 
        :rtype: List[List[int]] 
        """
        output = [[]]
        for i in range(len(nums)):
                for j in range(len(output)):
                        output.append(sorted(output[j] + [nums[i]]))
        return output  
