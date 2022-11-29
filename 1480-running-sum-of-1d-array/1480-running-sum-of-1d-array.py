class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        
        
        Sum = 0 
        res = []
        
    
        
        for val in nums:
            Sum+=val
            res.append(Sum)
        
        return res