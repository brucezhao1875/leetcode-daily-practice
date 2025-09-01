class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        if len(digits) == 0 :
            return []

        result = [x for x in maps[digits[0]]]
        #print(result)

        for i in range(1,len(digits)):
            map = maps[digits[i]]
            tmp_result = []
            for x in map :
                for item in result:
                    tmp_result.append(item + x)
            result = tmp_result
            #print(result)
        return result