class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            # 获取当前位的数字
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # 计算当前位的和
            total = digit_a + digit_b + carry
            
            # 当前位的结果
            result.append(str(total % 2))
            
            # 进位
            carry = total // 2
            
            # 移动指针
            i -= 1
            j -= 1
        
        # 反转结果（因为我们是从低位开始计算的）
        return ''.join(reversed(result))