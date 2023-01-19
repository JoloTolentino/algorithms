class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagram = {}
        for string in strs:
            temp = ''
            temp+=string 
            key = list(temp)
            key.sort()
            key = ''.join(key)
            if key in anagram:
                anagram[key].append(string)
            else: 
                anagram[key] = [string] 

        
        return [anagram[key] for key in anagram]