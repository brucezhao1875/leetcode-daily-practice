class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost) : return -1

        n = len(gas)
        tap = [0 for _ in range(n)]
        
        
        tap[0] = gas[0] - cost[0]
        index = 0
        min_left = tap[0]

        for i in range(1,n):
            tap[i] = tap[i-1] + gas[i] - cost[i]
            if tap[i] < min_left:
                index = i
                min_left = tap[i]
        return (index+1)%n