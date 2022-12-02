class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
       
        row,col = len(grid),len(grid[0])    
        q = deque()
        q.append([0,0,1])
        while q: 
            node = q.popleft()
            steps = node[2]
            if node[0] == row-1 and node[1] == col-1:
                return steps
            
            directions = ((node[0]+1,node[1]-1),(node[0]-1,node[1]+1),# r-l diagonal
                          (node[0]+1,node[1]+1),(node[0]-1,node[1]-1),# l-r diagonal
                          (node[0]+1,node[1])  ,(node[0], node[1]+1) ,# 4 connected
                          (node[0]-1,node[1])  ,(node[0], node[1]-1))
            
            
            for moves in directions: 
                if 0<= moves[0] <row and 0<= moves[1]<col and grid[moves[0]][moves[1]] == 0:
                    grid[moves[0]][moves[1]] = 1
                    q.append([moves[0],moves[1],steps+1])
        
        return -1
