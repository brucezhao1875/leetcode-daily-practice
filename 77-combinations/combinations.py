class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrace(start, path):
            if len(path) == k :
                result.append(path[:])
                return
            
            for i in range(start, n + 1) :
                if n - start + 1 < k - len(path):
                    continue
                path.append(i)
                backtrace(i + 1, path)
                path.pop()
        
        backtrace(1,[])
        return result
