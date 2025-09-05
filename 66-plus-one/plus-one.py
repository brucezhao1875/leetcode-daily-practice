class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)
        carry = 1
        i = n-1
        while carry >=1 and i >= 0 :
            if digits[i] == 9 :
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                carry = 0
            i = i - 1
        return [1] + digits if carry == 1 else digits
