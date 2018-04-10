# def subsets( nums):
#         # write your code here
#         n = len(nums)
#         # print('n',n)
#         if n == 0:
#             return [[]]
#         nums.sort()
#         print(nums)
#         result1 = subsets(nums[:n - 1])
#         # print('result1',result1)
#         result2 = subsets(nums[:n - 1])
#         print('result2',result2)
#         # for sub in result1:
#         #     sub.append(nums[-1])
#         # result1.extend(result2)
#         # return result1
# 
# 
def subsets( nums):
        """ 
        :type nums: List[int] 
        :rtype: List[List[int]] 
        """
        output = [[]]
        c=[]
        for i in range(len(nums)):
                for j in range(len(output)):
                        output.append(sorted(output[j] + [nums[i]]))


        return output  
subsets([1,2,3,4])