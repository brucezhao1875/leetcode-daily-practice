
class Solution:

    '''
        我想为这个解法写个注释，它包含了算法思路不少
        1、分治：它把所有可能的串分解为 "以right pointer为结尾的、不含重复字符的子串"，所以说是分治的思想
        2、动态规划：回顾数学归纳法的思路，为了满足一个条件，则：初始满足该条件；if n-1 step 满足条件，则n step 满足条件。这是数学归纳法，数学归纳法是动态规划的一种特例。
        在这里体现在：left = max(left,...) 为何这么说？ left不会退，表示在此之前的所有字符都不会重复；然后再保证s[right]也不重复。
        动态规划在这里，就是表现得如此朴素无华。

        好了，这题的另外一个方法是用set()，涉及到set()的操作：remove(item),add(item) -- 那个解法更直观。

        但是我做日常算法题的目标是维持逻辑思维，我的目标就是：脑袋里有什么想法，我就尝试把它落到纸面上，不背套路、不强调技巧，主打一个力大砖头飞。

    '''

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        result = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            if c in char_index :
                left = max(left,char_index[c] + 1)
            char_index[c] = right
            result = max(result,right-left+1)

        return result