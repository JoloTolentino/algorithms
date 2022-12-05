class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col  = len(grid),len(grid[0])
        
        def dfs(y,x):
    
            if 0<= y<row and 0<=x< col and grid[y][x]=='1': 
                grid[y][x] = '0'
                directions= ((y+1,x),(y-1,x),
                             (y,x+1), (y,x-1))
                for direction in directions: 
                    dfs(direction[0],direction[1])
            
            return 
                
        count=0
        for y in range(row):
            for x in range(col):
                if grid[y][x] =='1':
                    dfs(y,x)
                    count+=1
        return count