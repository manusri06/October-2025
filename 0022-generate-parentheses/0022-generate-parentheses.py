class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        ans = self.generateParenthesis(n-1)
        res = set()
        for i in ans:
            for j in range(len(i)):
                if i[j] == '(':
                    res.add(i[:j+1]+"()"+i[j+1:])
            res.add("()"+i)
        
        return list(res)
    
        