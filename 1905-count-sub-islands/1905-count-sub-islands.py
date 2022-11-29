class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        
        row,col = len(grid1),len(grid1[0])
        
        def dfs(y,x):
            
            directions = ((y+1,x),(y-1,x),(y,x+1),(y,x-1))
            
            if grid2[y][x] ==0:
                return True
            if grid2[y][x] ==1 and grid1[y][x] != grid2[y][x]:
                return False
            if grid2[y][x] == 1 and grid1[y][x] == grid2[y][x]:
                grid1[y][x]= 0
                grid2[y][x] = 0 
                
                temp = [] 
                for move in directions:
                    if 0<=move[0]<row and 0<=move[1]<col:
                        temp.append(dfs(move[0],move[1]))
            
            return all(temp)
            
    
        count =0 
        for y in range(row):
            for x in range(col):
                if grid2[y][x] == 1 and dfs(y,x): 
                    count+=1
        
        return count