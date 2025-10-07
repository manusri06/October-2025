class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        strr = ""
        num = 0
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)

            elif i == '[':
                stack.append((num,strr))
                strr = ""
                num = 0
            
            elif i == ']':
                num1,prev = stack.pop()
                strr = prev+num1*strr

            else:
                strr += i

        return strr
