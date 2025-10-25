class Solution:
    def calculate(self, s: str) -> int:

        s = s.replace(" ","")
        len_s = len(s)
        num = 0
        sign = "+"
        st = []

        for i,n in enumerate(s):

            if n.isdigit():
                num = num*10 + int(n)
            if not n.isdigit() or i == len_s-1:

                if sign == "+":
                    st.append(num)
                elif sign == "-":
                    st.append(-num)
                elif sign == "*":
                    st[-1] = st[-1]*num
                elif sign == '/':
                    st[-1] = int(st[-1]/num)
            
                num = 0
                sign = n
        return sum(st)
