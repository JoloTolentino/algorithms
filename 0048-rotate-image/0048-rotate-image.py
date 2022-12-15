class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        
    # \

        row,col = len(matrix),len(matrix[0])

        # reverse
        matrix.reverse() 

        '''
        7 8 9 
        4 5 6
        1 2 3 
        '''
        #symmetry swap 

        '''
        case 1      case 2
        (1, 0)      (1, 0)
        (2, 0)      (2, 0)
        (2, 1)      (2, 1)
                    (3, 0)
                    (3, 1)
                    (3, 2)
        '''
        for r in range(row):
            for c in range(r):
                print(r,c)     
                matrix[r][c],matrix[c][r]= matrix[c][r],matrix[r][c]
                

