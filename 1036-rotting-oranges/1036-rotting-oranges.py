class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        res = 0
        q = deque()
        rows, cols = len(grid),len(grid[0])
        fresh = 0
        direc = [(0,1),(1,0),(-1,0),(0,-1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j,0))

                if grid[i][j] == 1:
                    fresh+=1
        
        while q:
            row,col,g = q.popleft()
            for dr,dc in direc:
                r,c = row+dr,col+dc

                if 0<=r<rows and 0<=c<cols and grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r,c,g+1))
                    res = max(res,g+1)
        if fresh == 0:
            return res
        else:
            return -1