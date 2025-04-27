class Solution:
    # 维持一个stat[]，其中元素状态：未处理(0)/已处理(1)
    # 维持一个reach[]，其中元素状态：不可达(0)/可达(1)
    # 返回结果是： return any(not arr[i] and reach[i] for i in range(n))
    def canReach(self, arr: List[int], start: int) -> bool:
        debug = 0
        n = len(arr)
        stat = [ 0 for _ in range(n) ]  
        reach = [ 0 for _ in range(n) ]
        dq = collections.deque()
        dq.append(start)
        stat[start] = 1 
        while dq:
            x = dq.popleft()
            reach[x] = 1
            index = x - arr[x]
            if index >= 0 and stat[index]!=1 : 
                dq.append(index)
                stat[index] = 1
            index = x + arr[x]
            if index <= n-1 and stat[index]!=1 : 
                dq.append(index)
                stat[index] = 1
            debug and print("x:",x,";stat:",stat,";reach:",reach,";dq:",dq) 
        
        return any(not arr[i] and reach[i] for i in range(n))


