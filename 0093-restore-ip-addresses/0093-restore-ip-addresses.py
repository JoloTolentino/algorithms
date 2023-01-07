class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
    
        if len(s) > 12: return []

        res = []

        def backtrack(index = 0 , dots = 0, curIp = ''):
            if index == len(s) and dots == 4:
                res.append(curIp[:-1])  # discarding the last 4th dot
                return 
         

            for j in range(index, min(index+3, len(s))):  
                part = s[index:j+1]
                if int(part) <= 255 and (index == j or s[index] != '0'):
                    backtrack(j+1, dots+1, curIp + part + '.')
            
        backtrack()
        return res 