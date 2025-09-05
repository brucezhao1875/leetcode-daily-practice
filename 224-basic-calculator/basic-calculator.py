class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        result = 0
        length = len(s)
        i = 0
        while i<length:
            ch = s[i]
            if ch == ' ':
                i = i + 1
            elif ch.isdigit():
                value = ord(s[i]) - ord('0')
                while i+1 < length and s[i+1].isdigit():
                    i = i + 1
                    value = value*10 + ord(s[i]) - ord('0')
                result += value*sign
                i = i + 1
            elif ch == '+':
                sign = 1
                i = i + 1
            elif ch == '-':
                sign = -1
                i = i + 1
            elif ch == '(':
                stack.append(result)
                result = 0
                stack.append(sign)
                sign = 1
                i = i + 1
            elif ch == ')':
                formerSign = stack.pop()
                formerResult = stack.pop()
                result = formerResult + formerSign*result
                i = i + 1
              
        return result