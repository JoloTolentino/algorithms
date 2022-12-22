class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result,temp = [],[] 
        
        def backtracking(index=0):
            
            if temp not in result:
                result.append(temp[:])
            
            if index>= len(nums):
                return
            
            
            temp.append(nums[index])
            backtracking(index+1)
            temp.pop()
            backtracking(index+1)
            
        backtracking()
        return result
            
            
            
                
                
            
            