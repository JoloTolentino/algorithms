class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        Map  = {}
        words = s.split(' ')
        seen = [] 

        if len(words) != len(pattern): return False

        for index,char in enumerate(pattern):
            if char not in Map:
                if words[index] not in seen:
                    Map[char] = words[index]
                    seen.append(words[index])
                else:
                    return False
            if char in Map:
                if Map[char] != words[index]:
                    return False 
                continue
        
        return True