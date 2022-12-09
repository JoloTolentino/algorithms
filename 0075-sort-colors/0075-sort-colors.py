class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
     
        
        count = {0:0,1:0,2:0}
        
        for val in nums:
            count[val]+=1
        
        index = 0 
        
        for key in count: 
            while count[key]:
                nums[index] = key
                count[key]-=1
                index+=1
                