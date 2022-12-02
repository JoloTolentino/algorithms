class Solution:
    def fib(self, n: int) -> int:
        
        
        
        seen = {0:0,1:1}
        
        
        def memoization(val=2):
            if val not in seen:
                seen[val] = seen[val-1]+seen[val-2]
            
            if val!= n:
                memoization(val+1)
                
                
        
        if n <=1:
            return seen[n]
        
        else:
            memoization()
            return seen[n]
                
                
        
        
        
            
            
            
            
            
            
                
                
                
            
            