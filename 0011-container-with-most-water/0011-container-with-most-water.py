class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        A 2 pointer problem 
        
        '''
        MAX =float('-inf')
        l,r = 0, len(height)-1
        while l<r:
            currMaxHeight = min(height[l],height[r])
            currLength = r-l
            currMaxArea= currMaxHeight*currLength
            MAX = max(MAX,currMaxArea)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1 
        return MAX  
