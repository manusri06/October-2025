class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        visited = []

        def dfs(city):
            for neig in range(n):
                if isConnected[city][neig] == 1 and neig not in visited:
                    visited.append(neig)
                    dfs(neig)

        group = 0
        for city in range(n):
            if city not in visited:
                visited.append(city)
                group += 1
                dfs(city)
        return group