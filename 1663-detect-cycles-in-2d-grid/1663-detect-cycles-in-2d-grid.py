class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        rows,cols=len(grid),len(grid[0])
        visited=[[False]*cols for _ in range(rows)]
        def dfs(r,c,pr,pc,char):
            if visited[r][c]:
                return True
            visited[r][c]=True
            d=[(0,1),(1,0),(-1,0),(0,-1)]
            for dr,dc in d:
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==char:
                    if(nr,nc)==(pr,pc):
                        continue
                    if dfs(nr,nc,r,c,char):
                        return True
            return False
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    if dfs(r,c,-1,-1,grid[r][c]):
                        return True
        return False
