class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row,col = len(grid),len(grid[0])
        rotten_orange_stack =deque()
        fresh_orange_count = 0
        m =0 
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1: 
                    fresh_orange_count +=1        
                if grid[r][c] == 2: 
                    rotten_orange_stack.append((r,c,m))
        
        if fresh_orange_count == 0: return 0
        
        total_minutes = 0
        while rotten_orange_stack:
            y,x,minute = rotten_orange_stack.popleft()

            total_minutes = max(minute,total_minutes)

            directions = ((y+1,x),(y-1,x),
                          (y,x+1),(y,x-1))

            
            for dy,dx in directions:
                if 0<=dy<row and 0<=dx<col and grid[dy][dx] == 1:
                    rotten_orange_stack.append((dy,dx,minute+1))
                    grid[dy][dx] = 2
                    fresh_orange_count-=1
        
        return total_minutes if fresh_orange_count == 0 else -1
            






