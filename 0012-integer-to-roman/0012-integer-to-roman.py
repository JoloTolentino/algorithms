class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        roman = []
        dictionary = {
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M",
        }
        
    
        def backtrack(num): 
            if num == 0 :
                return 0
            if num>=1000:
                num-=1000
                roman.append(dictionary[1000])
            
            if 900 <= num <1000 :
                num-= 900
                roman.append(dictionary[100])
                roman.append(dictionary[1000])
            if 500<= num <900:
                num -=500
                roman.append( dictionary[500])
                
            if 400<=num< 500:
                num-=400
                roman.append(dictionary[100])
                roman.append(dictionary[500])
                
            if 100<=num<400: 
                num-=100
                roman.append(dictionary[100])
                
            if 90<= num <100:
                num-=90
                roman.append(dictionary[10])
                roman.append(dictionary[100])
                
            if 50<=num <90:
                num-=50
                roman.append(dictionary[50])
               
            
            if 40<=num<50:
                num-=40
                roman.append( dictionary[10]+ dictionary[50])
            
            if 10 <= num < 40:
                num-=10
                roman.append(dictionary[10])
            if 9<=num<10:
                num-=9
                roman.append(dictionary[1]+dictionary[10])
            if 5<=num<9:
                num-=5
                roman.append(dictionary[5])
                
            if 4<=num<5: 
                num-=4
                roman.append( dictionary[1]+dictionary[5])
            if 1<=num<4:
                num-=1
                roman.append(dictionary[1])
            backtrack(num)
                
            
        
        backtrack(num)
        string = ''
        
        for val in roman:
            string+=val
        return string
        
        
        
        
        