def searchMatrix(matrix, target):
	# write your code here
	end=len(matrix)-1
	begin=0
	mid=0
	if target  in matrix[begin]:return True
	if target  in matrix[end-1]:return True
	while begin<end:
		mid=(begin+(end-begin))//2
		if target in matrix[mid]:
			return True
			
		elif target>matrix[begin][0]:
			begin=begin+1
		else:
			end=end-1
	if target not in matrix[mid]:return False


#测试
assert searchMatrix([
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50]
                    ],3)==True,\
    'Calculation error,True:True , yours:%s' % searchMatrix([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]],3)
assert searchMatrix([[5]],2)==False,'Calculation error,True:False , yours:%s' % searchMatrix([[5]],2)