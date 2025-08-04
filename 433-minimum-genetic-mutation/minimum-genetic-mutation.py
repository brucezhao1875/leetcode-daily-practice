class Solution:
    '''
     很有代表性的一个题呀，关于graph bfs的逻辑.
    '''
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        bank = set(bank)
        visited = set()
        queue = deque([(startGene,0)])
        visited.add(startGene)
        genes = ['A','C','G','T']
        while queue:
            current,steps = queue.popleft()
            if current == endGene:
                return steps
            for i in range(len(current)):
                for gene in genes:
                    if gene is not current[i]:
                        next_seq = current[:i] + gene + current[i+1:]
                        if next_seq in bank and next_seq not in visited:
                            visited.add(next_seq)
                            queue.append((next_seq,steps+1))
        return -1