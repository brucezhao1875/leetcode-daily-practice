class Solution:
    hash = {
        1:'I',
        4:'IV',
        5:'V',
        9:'IX',
        10:'X',
        40:'XL',
        50:'L',
        90:'XC',
        100:'C',
        400:'CD',
        500:'D',
        900:'CM',
        1000:'M'
    }
    sorted_list = sorted(hash.items(),key = lambda x:x[0],reverse = True)
    sorted_hash = {k:v for k,v in sorted_list}


    def intToRoman(self, num: int) -> str:
        def find_max_item(num):
            for item in self.sorted_list:
                if num >= item[0]:
                    return item
            return None
    
        result = ''
        while num > 0:
            item = find_max_item(num)
            result += item[1]
            num -= item[0]
        return result
        