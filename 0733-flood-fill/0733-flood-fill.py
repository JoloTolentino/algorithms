class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        row,col = len(image),len(image[0])
        start_color = image[sr][sc]
        if start_color == color : return image
        
        
        def dfs(y,x):
            
            directions = ((y+1,x),(y-1,x),(y,x+1),(y,x-1))
            
            if image[y][x] == start_color: 
                image[y][x] = color
                for move in directions:
                    if 0<=move[0]<row and 0<= move[1]<col:
                        dfs(move[0],move[1])

            
            if image[y][x] != start_color:
                return 
            
           
    
        
        dfs(sr,sc)
        return image